import threading
class P3:
    def __init__(self, bufferC, bufferD):
        self.bufferC = bufferC
        self.bufferD = bufferD

    def check(self, time, bufferC, bufferD, semC, semD):
        
        time -= 1
        for t in range(0,21):
            threading._sleep(1)
            
                
            
            if(t%2==1):
                
                semC.acquire()
                time += 1
                if self.getposX(bufferC) == self.getposY(bufferC) and self.getposX(bufferC) != self.getposZ(bufferC):
                    print "Collision at time ", time, " between X and Y location: (",bufferC[1][0],",",bufferC[2][0],")"

                elif self.getposX(bufferC) != self.getposY(bufferC) and self.getposX(bufferC) == self.getposZ(bufferC):
                    print "Collision at time ", time, " between X and Z location: (",bufferC[1][0],",",bufferC[2][0],")"

                elif self.getposX(bufferC) == self.getposY(bufferC) and self.getposX(bufferC) == self.getposZ(bufferC):
                    print "Collision at time ", time, " between X, Y, and Z location: (",bufferC[1][0],",",bufferC[2][0],")"

                elif self.getposY(bufferC) == self.getposZ(bufferC) and self.getposY(bufferC) != self.getposX(bufferC):
                    print "Collision at time ", time, " between Y and Z location: (",bufferC[1][1],",",bufferC[2][1],")"

                else:
                    print "No collision at time: ", time
                semC.release()
            
            elif t is not 0 and t%2 is 0:
                
                semD.acquire()
                time += 1
                if self.getposX(bufferD) == self.getposY(bufferD) and self.getposX(bufferD) != self.getposZ(bufferD):
                    print "Collision at time ", time, " between X and Y location: (", bufferD[1][0], ",", bufferD[2][0], ")"
                elif self.getposX(bufferD) != self.getposY(bufferD) and self.getposX(bufferD) == self.getposZ(bufferD):
                    print "Collision at time ", time, " between X and Z location: (", bufferD[1][0], ",", bufferD[2][0], ")"
                elif self.getposX(bufferD) == self.getposY(bufferD) and self.getposX(bufferD) == self.getposZ(bufferD):
                    print "Collision at time ", time, " between X, Y, and Z location: (", bufferD[1][0], ",", bufferD[2][0], ")"
                elif self.getposY(bufferD) == self.getposZ(bufferD) and self.getposY(bufferD) != self.getposX(bufferD):
                    print "Collision at time ", time, " between Y and Z location: (", bufferD[1][1], ",", bufferD[2][1], ")"
                else:
                    print "No collision at time: ", time
                semD.release()
            else:
                time += 1
            
        
  


        

    def getposX(self,buffer):
        return str(buffer[1][0]) + str(buffer[2][0])
    def getposY(self,buffer):
        return str(buffer[1][1]) + str(buffer[2][1])
    def getposZ(self,buffer):
        return str(buffer[1][2]) + str(buffer[2][2])

    

