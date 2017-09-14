import threading
class P1(threading.Thread):
    
    def __init__(self, bufferA, bufferB, planeX, planeY, planeZ):
        threading.Thread.__init__(self)
        threadNum = 1
        self.bufferA = bufferA
        self.bufferB = bufferB
        self.planeX = planeX
        self.planeY = planeY
        self.planeZ = planeZ

    def move(self, time):
        if time % 2 == 0:
            self.planeX.move(self.bufferA)
            self.planeY.move(self.bufferA)
            self.planeZ.move(self.bufferA)
        else:
            self.planeX.move(self.bufferB)
            self.planeY.move(self.bufferB)
            self.planeZ.move(self.bufferB)

