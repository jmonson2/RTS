import threading
class P3:
    def __init__(self, bufferC, bufferD, planeX, planeY,planeZ):
        self.bufferC = bufferC
        self.bufferD = bufferD

    def check(self, time, bufferC, bufferD, semC, semD,planeX,planeY,planeZ):
        
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

            self.lookahead(planeX, planeY, planeZ)
            print "X Row: ", planeZ.getRow()
            print "Y Col: ", planeZ.getCol()

    #Looks ahead 2 moves        
    def lookahead(self,planeX, planeY, planeZ):
        
        #You will need to stop in this method. Find a way to cease threading on P1 and P2 (maybe acquire semaphores?)
        #PLANEX MOVEMENT
        #Moves Row+=(Row+1) % 8 | Col+=(Col+1) % 7 SIM ROW + COL
        #PLANEY MOVEMENT
        #Moves Row+=(Row+1) % 8 | Col=2 SIM ROW
        #PLANEZ MOVEMENT
        #Moves Row=3 | Col+=(Col+1) % 7 SIM COL
    #move 1:
        xRow1 = (planeX.getRow() + 1) % 8
        xCol1 = (planeX.getCol() + 1) % 7
        yRow1 = (planeY.getRow() + 1) % 8
        yCol1 = 2
        zRow1 = 3
        zCol1 = (planeZ.getCol() + 1) % 7
        #print "LOOKUP X ROW: ", xRow1
        #print "LOOKUP X COL: ", xCol1
        #print "LOOKUP Y ROW: ", yRow1
        #print "LOOKUP Y COL: ", yCol1
        #print "LOOKUP Z ROW: ", zRow1
        #print "LOOKUP Z COL: ", zCol1
        xRow2 = (xRow1 + 1) % 8
        xCol2 = (xCol1 + 1) % 7
        yRow2 = (yRow1 + 1) % 8
        yCol2 = yCol1
        zRow2 = zRow1
        zCol2 = (zCol1 + 1) % 7
        
        if xRow1 == yRow1 and xCol1 == yCol1:
            if xRow1 == zRow2 and xCol1 == zCol2:
                planeX.stop()
            elif yRow1 == zRow2 and yCol1 == zCol2:
                planeY.stop()
            else:
                planeX.stop()

        elif xRow1 == zRow1 and xCol1 == zCol1:
            if xRow1 == yRow2 and xCol1 == yCol2:
                planeX.stop()
            elif zRow1 == yRow2 and zCol1 == yCol2:
                planeZ.stop() 
            else:   
                planeZ.stop()

        elif yRow1 == zRow1 and yCol1 == zCol1:
            if yRow1 == xRow2 and yCol1 == xCol2:
                planeY.stop()
            elif zRow1 == xRow2 and zCol1 == xCol2:
                planeZ.stop() 
            else:
                planeY.stop()
        
        
        
    def getposX(self,buffer):
        return str(buffer[1][0]) + str(buffer[2][0])
    def getposY(self,buffer):
        return str(buffer[1][1]) + str(buffer[2][1])
    def getposZ(self,buffer):
        return str(buffer[1][2]) + str(buffer[2][2])

    

