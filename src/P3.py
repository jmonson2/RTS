import threading
class P3:
    def __init__(self, bufferC, bufferD, planeX, planeY,planeZ):
        self.bufferC = bufferC
        self.bufferD = bufferD
    

    def check(self, time, bufferC, bufferD, semC, semD,planeX,planeY,planeZ, semA, semB, interval, itterations):
        
        time -= 1
        for t in range(0,itterations+1):
            threading._sleep(interval)
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
            semA.acquire()
            semB.acquire()
            semC.acquire()
            semD.acquire()
            self.lookahead(planeX, planeY, planeZ, time+2)
            semA.release()
            semB.release()
            semC.release()
            semD.release()
            #print "TIME:     ", time
            #print bufferD
            #print "X: ", planeX.getRow(), ", ", planeX.getCol()
            #print "Y: ", planeY.getRow(), ", ", planeY.getCol()
            #print "Z: ", planeZ.getRow(), ", ", planeZ.getCol()
            #print "BUFFERC :", bufferC
           # print "BUFFERD :", bufferD
            #threading._sleep(1)
        

    #Looks ahead 2 moves        
    def lookahead(self,planeX, planeY, planeZ,t):
        
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
        l_xFlag = False
        l_yFlag = False
        l_zFlag = False
        #Need to add code to check if xFlag is stopped so you don't stop y flag
        if xRow1 == yRow1 and xCol1 == yCol1:
            if xRow2 == zRow2 and xCol2 == zCol2:
                
                planeX.stop()
                print "Future Collision detected between X and Y at time ", t,". Stopped plane X"
                #threading._sleep(1)
                #planeX.start()
                
            if yRow2 == zRow2 and yCol2 == zCol2:
                
                planeY.stop()
                print "Future collision detected between X and Y at time ", t,". Stopped plane Y"
                #threading._sleep(1)
                #planeY.start()
            else:
                planeX.stop()
                print "Future collision detected between X and Y at time ", t,". Stopped plane X"
               # threading._sleep(1)
                #planeX.start()
        if planeX.getflag() != l_xFlag:
            xRow2 = xRow1
            xRow1 = planeX.getRow()
            xCol2 = xCol1
            xCol1 = planeX.getCol()
            l_xFlag = True #F->T
        if planeY.getflag() != l_yFlag:
            yRow2 = yRow1
            yRow1 = planeY.getRow()
            yCol2 = yCol1
            yCol1 = planeY.getCol()
            l_yFlag = True
        if planeZ.getflag() != l_zFlag:
            zRow2 = zRow1
            zRow1 = planeZ.getRow()
            zCol2 = zCol1
            zCol1 = planeZ.getCol()
            l_zFlag = True
            
        if xRow1 == zRow1 and xCol1 == zCol1:
            if xRow2 == yRow2 and xCol2 == yCol2:
            
                planeX.stop()
                print "Future collision detected between X and Z at time ",t,". Stopped plane X"
                #threading._sleep(1)
                #planeX.start()
            if zRow2 == yRow2 and zCol2 == yCol2:
                
                planeZ.stop() 
                print "Future collision detected between X and Z at time ,",t,". Stopped plane Z"
                #threading._sleep(1)
                #planeZ.start()
            else:   
                
                planeX.stop()
                print "Future collision detected between X and z at time ,",t,". Stopped plane X"
                #threading._sleep(1)
                #planeZ.start()
        if planeX.getflag() != l_xFlag:
            xRow2 = xRow1
            xRow1 = planeX.getRow()
            xCol2 = xCol1
            xCol1 = planeX.getCol()
            l_xFlag = True #F->T
        if planeY.getflag() != l_yFlag:
            yRow2 = yRow1
            yRow1 = planeY.getRow()
            yCol2 = yCol1
            yCol1 = planeY.getCol()
            l_yFlag = True
        if planeZ.getflag() != l_zFlag:
            zRow2 = zRow1
            zRow1 = planeZ.getRow()
            zCol2 = zCol1
            zCol1 = planeZ.getCol()
            l_zFlag = True
        if yRow1 == zRow1 and yCol1 == zCol1:
            if yRow2 == xRow2 and yCol2 == xCol2:
                
                planeY.stop()
                print "Future collision detected between Y and Z at time ",t,". Stopped plane Y"
                #threading._sleep(1)
                #planeY.start()
            if zRow2 == xRow2 and zCol2 == xCol2:
                
                planeZ.stop()

                print "Future collision detected between Y and Z at time ",t,". Stopped plane Z"
                #threading._sleep(1)
                #planeZ.start() 
           
            else:
                
                planeY.stop() 
                
                print "Future collision detected between Y and Z at time ",t,". Stopped plane Y"
                #threading._sleep(1)
                #planeY.start()    
       
        
        
        
        
    def getposX(self,buffer):
        return str(buffer[1][0]) + str(buffer[2][0])
    def getposY(self,buffer):
        return str(buffer[1][1]) + str(buffer[2][1])
    def getposZ(self,buffer):
        return str(buffer[1][2]) + str(buffer[2][2])
    def stopX(self):
        self.xRow2 = self.xRow1
        self.xRow1 = planeX.getRow()
        self.xCol2 = self.xCol1
        self.xCol1 = planeX.getCol()
        planeX.stop()
    def stopY(self):
        self.yRow2 = self.yRow1
        self.yRow1 = planeY.getRow()
        self.yCol2 = self.yCol1
        self.yCol1 = planeY.getCol()
        planeY.stop()
    def stopZ(self):
        self.zRow2 = self.zRow1
        self.zRow1 = planeZ.getRow()
        self.zCol2 = self.zCol1
        self.zCol1 = planeZ.getCol()
        planeZ.stop()

    

