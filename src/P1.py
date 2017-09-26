import threading
class P1(threading.Thread):
    
    def __init__(self, time, planeX, planeY, planeZ, bufferA, bufferB):
        threadNum = 1
        self.bufferA = bufferA
        self.bufferB = bufferB
        self.plane_X = planeX
        self.plane_Y = planeY
        self.plane_Z = planeZ

    def proc1(self,time,plane_X,plane_Y,plane_Z,bufferA,bufferB):
        i = time
        if i % 2 == 0:
            plane_X.move(bufferB)
            plane_Y.move(bufferB)
            plane_Z.move(bufferB)
        else:
            plane_X.move(bufferA)
            plane_Y.move(bufferA)
            plane_Z.move(bufferA)


        #print("BUFFER A", bufferA)
      #  print("BUFFER B", bufferB)

