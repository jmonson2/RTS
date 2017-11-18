import threading
import time

class P1:
    def __init__(self, time, planeX, planeY, planeZ, bufferA, bufferB, semA, semB):#, lockP1, lockP2, lockP3):
        self.bufferA = bufferA
        self.bufferB = bufferB
        self.plane_X = planeX
        self.plane_Y = planeY
        self.plane_Z = planeZ
       


    def proc1(self,time,plane_X,plane_Y,plane_Z,bufferA,bufferB, semA, semB,semC, semD, interval, itterations):
        
        semC.acquire()
        semD.acquire()
        i = time
        for i in range(0,itterations):
            threading._sleep(interval)
            
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
            semC.release()
            semD.release()
            
    
      

