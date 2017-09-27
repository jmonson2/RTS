import threading
import time
class P1:
    def __init__(self, time, planeX, planeY, planeZ, bufferA, bufferB, semA, semB):
        self.bufferA = bufferA
        self.bufferB = bufferB
        self.plane_X = planeX
        self.plane_Y = planeY
        self.plane_Z = planeZ
        self.semA = threading.Semaphore()
        self.semB = threading.Semaphore()

    def proc1(self,time,plane_X,plane_Y,plane_Z,bufferA,bufferB, semA, semB):
        i = time
        for i in range(0,20):
            threading._sleep(1)
            if i % 2 == 0:
                semB.acquire()
                plane_X.move(bufferB)
                plane_Y.move(bufferB)
                plane_Z.move(bufferB)
                semB.release()
            else:
                semA.acquire()
                plane_X.move(bufferA)
                plane_Y.move(bufferA)
                plane_Z.move(bufferA)
                semA.release()
        #print("BUFFER A", bufferA)
        #print("BUFFER B", bufferB)

