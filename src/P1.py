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
                if not plane_X.getflag():
                    plane_X.move(bufferB)
                if not plane_Y.getflag():
                    plane_Y.move(bufferB)
                if not plane_Z.getflag():
                    plane_Z.move(bufferB)
                semB.release()
            else:
                semA.acquire()
                if not plane_X.getflag():
                    plane_X.move(bufferA)
                if not plane_Y.getflag():
                    plane_Y.move(bufferA)
                if not plane_Z.getflag():
                    plane_Z.move(bufferA)
                semA.release()
            plane_X.start()
            plane_Y.start()
            plane_Z.start()
    
      

