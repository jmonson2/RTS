import threading
class P2:
    def __init__(self, time, bufferC, bufferD):
        self.time = time
        self.bufferC = bufferC
        self.bufferD = bufferD

    def proc(self, time, bufferA,bufferB,bufferC, bufferD, semA, semB, semC, semD):
        
        for t in range(0,20):
            threading._sleep(1)
            if(t%2 == 0):
                semA.acquire()
                semC.acquire()

                for i in range(len(bufferA)):
                    for j in range(len(bufferA[i])):
                        if bufferA[i][j] == 'X':
                            bufferC[1][0] = i
                            bufferC[2][0] = j
                        elif bufferA[i][j] == 'Y':
                            bufferC[1][1] = i
                            bufferC[2][1] = j
                        elif bufferA[i][j] == 'Z':
                            bufferC[1][2] = i
                            bufferC[2][2] = j
                        elif bufferA[i][j] == 'XY':
                            bufferC[1][0] = i
                            bufferC[2][0] = j
                            bufferC[1][1] = i
                            bufferC[2][1] = j
                        elif bufferA[i][j] == 'XZ':
                            bufferC[1][0] = i
                            bufferC[2][0] = j
                            bufferC[1][2] = i
                            bufferC[2][2] = j
                        elif bufferA[i][j] == 'YZ':
                            bufferC[1][1] = i
                            bufferC[2][1] = j
                            bufferC[1][2] = i
                            bufferC[2][2] = j
                        elif bufferA[i][j] == 'XYZ':
                            bufferC[1][0] = i
                            bufferC[2][0] = j
                            bufferC[1][1] = i
                            bufferC[2][1] = j
                            bufferC[1][2] = i
                            bufferC[2][2] = j
                        else:
                            pass
                semA.release()
                semC.release()

            
                

            else:
                semB.acquire()
                semD.acquire()
                for i in range(len(bufferB)):
                    for j in range(len(bufferB[i])):
                        if bufferB[i][j] == 'X':
                            bufferD[1][0] = i
                            bufferD[2][0] = j
                        elif bufferB[i][j] == 'Y':
                            bufferD[1][1] = i
                            bufferD[2][1] = j
                        elif bufferB[i][j] == 'Z':
                            bufferD[1][2] = i
                            bufferD[2][2] = j
                        elif bufferB[i][j] == 'XY':
                            bufferD[1][0] = i
                            bufferD[2][0] = j
                            bufferD[1][1] = i
                            bufferD[2][1] = j
                        elif bufferB[i][j] == 'XZ':
                            bufferD[1][0] = i
                            bufferD[2][0] = j
                            bufferD[1][2] = i
                            bufferD[2][2] = j
                        elif bufferB[i][j] == 'YZ':
                            bufferD[1][1] = i
                            bufferD[2][1] = j
                            bufferD[1][2] = i
                            bufferD[2][2] = j
                        elif bufferB[i][j] == 'XYZ':
                            bufferD[1][0] = i
                            bufferD[2][0] = j
                            bufferD[1][1] = i
                            bufferD[2][1] = j
                            bufferD[1][2] = i
                            bufferD[2][2] = j
                        else:
                            pass
                semB.release()
                semD.release()
            

    def proc2BD(self, time, bufferB, bufferD, semB, semD):
        for t in range(0,20):
            semB.acquire()
            semD.acquire()
            for i in range(len(bufferB)):
                for j in range(len(bufferB[i])):
                    if bufferB[i][j] == 'X':
                        bufferD[1][0] = i
                        bufferD[2][0] = j
                    elif bufferB[i][j] == 'Y':
                        bufferD[1][1] = i
                        bufferD[2][1] = j
                    elif bufferB[i][j] == 'Z':
                        bufferD[1][2] = i
                        bufferD[2][2] = j
                    elif bufferB[i][j] == 'XY':
                        bufferD[1][0] = i
                        bufferD[2][0] = j
                        bufferD[1][1] = i
                        bufferD[2][1] = j
                    elif bufferB[i][j] == 'XZ':
                        bufferD[1][0] = i
                        bufferD[2][0] = j
                        bufferD[1][2] = i
                        bufferD[2][2] = j
                    elif bufferB[i][j] == 'YZ':
                        bufferD[1][1] = i
                        bufferD[2][1] = j
                        bufferD[1][2] = i
                        bufferD[2][2] = j
                    elif bufferB[i][j] == 'XYZ':
                        bufferD[1][0] = i
                        bufferD[2][0] = j
                        bufferD[1][1] = i
                        bufferD[2][1] = j
                        bufferD[1][2] = i
                        bufferD[2][2] = j
                    else:
                        pass
            semB.release()
            semD.release()

        
