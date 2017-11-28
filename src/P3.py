#New additions here.
#Johnathon Monson - bug fixing, assisting with other modules. Wrote the code that allows looking at positions in the future
#Armando wrote code to stop trains and assisted with testing and debugging
#Ryan Sparks wrote code to detect future collisions
import threading
import random
class P3:
    def __init__(self, bufferC, bufferD, planeX, planeY,planeZ,zx1,yy1):
        self.bufferC = bufferC
        self.bufferD = bufferD
        self.f_Collision = False
        self.zx1=zx1
        self.yy1=yy1
    

    def check(self, time, bufferC, bufferD, semC, semD,planeX,planeY,planeZ, semA, semB, interval, itterations):
        
        
        time -= 1
        self.findSecondPosition(planeX, planeY, planeZ, time+2)
        for t in range(0,itterations+1):

            threading._sleep(interval)
            semA.acquire()
            semB.acquire()
            semC.acquire()
            semD.acquire()
           
            if(t%2==1):
                
                
                time += 1
                if self.getposX(bufferC) == self.getposY(bufferC) and self.getposX(bufferC) != self.getposZ(bufferC):
                    print "Collision at time ", time, " between X and Y location: (",bufferC[1][0],",",bufferC[2][0],")"
                    self.f_Collision = True

                elif self.getposX(bufferC) != self.getposY(bufferC) and self.getposX(bufferC) == self.getposZ(bufferC):
                    print "Collision at time ", time, " between X and Z location: (",bufferC[1][0],",",bufferC[2][0],")"
                    self.f_Collision = True

                elif self.getposX(bufferC) == self.getposY(bufferC) and self.getposX(bufferC) == self.getposZ(bufferC):
                    print "Collision at time ", time, " between X, Y, and Z location: (",bufferC[1][0],",",bufferC[2][0],")"
                    self.f_Collision = True

                elif self.getposY(bufferC) == self.getposZ(bufferC) and self.getposY(bufferC) != self.getposX(bufferC):
                    print "Collision at time ", time, " between Y and Z location: (",bufferC[1][1],",",bufferC[2][1],")"
                    self.f_Collision = True

                else:
                    print "No collision at time: ", time
                
                
            
            elif t is not 0 and t%2 is 0:
                
                
                time += 1
                if self.getposX(bufferD) == self.getposY(bufferD) and self.getposX(bufferD) != self.getposZ(bufferD):
                    print "Collision at time ", time, " between X and Y location: (", bufferD[1][0], ",", bufferD[2][0], ")"
                    self.f_Collision = True
                elif self.getposX(bufferD) != self.getposY(bufferD) and self.getposX(bufferD) == self.getposZ(bufferD):
                    print "Collision at time ", time, " between X and Z location: (", bufferD[1][0], ",", bufferD[2][0], ")"
                    self.f_Collision = True
                elif self.getposX(bufferD) == self.getposY(bufferD) and self.getposX(bufferD) == self.getposZ(bufferD):
                    print "Collision at time ", time, " between X, Y, and Z location: (", bufferD[1][0], ",", bufferD[2][0], ")"
                    self.f_Collision = True
                elif self.getposY(bufferD) == self.getposZ(bufferD) and self.getposY(bufferD) != self.getposX(bufferD):
                    print "Collision at time ", time, " between Y and Z location: (", bufferD[1][1], ",", bufferD[2][1], ")"
                    self.f_Collision = True
                else:
                    print "No collision at time: ", time
                
            else:
                time += 1
            
            
            self.lookahead(planeX, planeY, planeZ, time+2)
           
            semA.release()
            semB.release()
            semC.release()
            semD.release()
            if self.f_Collision:
                print "COMPLETE SYSTEM FAILURE"
            #print "X ROW:",planeX.getRow()
            #print "X COL:",planeX.getCol()
            #print "Y ROW:",planeY.getRow()
            #print "Y COL: ",planeY.getCol()
            #print "Z ROW: ",planeZ.getRow()
            #print "Z COL: ",planeZ.getCol()
            
    def findSecondPosition(self,planeX, planeY, planeZ, t):
        xRow1 = (planeX.getRow() + 1) % 8
        xCol1 = (planeX.getCol() + 1) % 7
        yRow1 = (planeY.getRow() + 1) % 8
        yCol1 = self.yy1
        zRow1 = self.zx1
        zCol1 = (planeZ.getCol() + 1) % 7
       
        xRow2 = (xRow1 + 1) % 8
        xCol2 = (xCol1 + 1) % 7
        yRow2 = (yRow1 + 1) % 8
        yCol2 = yCol1
        zRow2 = zRow1
        zCol2 = (zCol1 + 1) % 7
        l_xFlag = False
        l_yFlag = False
        l_zFlag = False

        if (xRow2 < xRow1 and xCol2 < xCol1):
            print "X starting at (", xRow1, ", ", xCol1, ") with initial velocity Southwest"
        elif (xRow2 < xRow1):
            print "X starting at (", xRow1, ", ", xCol1, ") with initial velocity West"
        elif (xCol2 < xCol1):
            print "X starting at (", xRow1, ", ", xCol1, ") with initial velocity South"
        elif (xRow2 > xRow1 and xCol2 > xCol1):
            print "X starting at (", xRow1, ", ", xCol1, ") with initial velocity Northeast"
        elif (xRow2 > xRow1):
            print "X starting at (", xRow1, ", ", xCol1, ") with initial velocity East"
        else:
            print "X starting at (", xRow1, ", ", xCol1, ") with initial velocity North"

        if (yRow2 < yRow1 and yCol2 < yCol1):
            print "Y starting at (", yRow1, ", ", yCol1, ") with initial velocity Southwest"
        elif (yRow2 < yRow1):
            print "Y starting at (", yRow1, ", ", yCol1, ") with initial velocity West"
        elif (yCol2 < yCol1):
            print "Y starting at (", yRow1, ", ", yCol1, ") with initial velocity South"
        elif (yRow2 > yRow1 and yCol2 > yCol1):
            print "Y starting at (", yRow1, ", ", yCol1, ") with initial velocity Northeast"
        elif (yRow2 > yRow1):
            print "Y starting at (", yRow1, ", ", yCol1, ") with initial velocity East"
        else:
            print "Y starting at (", yRow1, ", ", yCol1, ") with initial velocity North"

        if (zRow2 < zRow1 and zCol2 < zCol1):
            print "Z starting at (", zRow1, ", ", zCol1, ") with initial velocity Southwest"
        elif (zRow2 < zRow1):
            print "Z starting at (", zRow1, ", ", zCol1, ") with initial velocity West"
        elif (zCol2 < zCol1):
            print "Z starting at (", zRow1, ", ", zCol1, ") with initial velocity South"
        elif (zRow2 > zRow1 and zCol2 > zCol1):
            print "Z starting at (", zRow1, ", ", zCol1, ") with initial velocity Northeast"
        elif (zRow2 > zRow1):
            print "Z starting at (", zRow1, ", ", zCol1, ") with initial velocity East"
        else:
            print "Z starting at (", zRow1, ", ", zCol1, ") with initial velocity North"
            
    #Looks ahead 2 moves        
    def lookahead(self,planeX, planeY, planeZ,t):
       
        xRow1 = (planeX.getRow() + 1) % 8
        xCol1 = (planeX.getCol() + 1) % 7
        yRow1 = (planeY.getRow() + 1) % 8
        yCol1 = 2
        zRow1 = 3
        zCol1 = (planeZ.getCol() + 1) % 7
       
        xRow2 = (xRow1 + 1) % 8
        xCol2 = (xCol1 + 1) % 7
        yRow2 = (yRow1 + 1) % 8
        yCol2 = yCol1
        zRow2 = zRow1
        zCol2 = (zCol1 + 1) % 7
        l_xFlag = False
        l_yFlag = False
        l_zFlag = False
        
        if xRow1 == yRow1 and xCol1 == yCol1:
            if xRow2 == zRow2 and xCol2 == zCol2:
                
                planeX.stop()
                print "Future Collision detected between X and Y at time ", t,". Stopped plane X"
                if planeX.getflag is False:
                    planeY.stop()
                    planeZ.stop()
                    print ("Failure in train X brake detected. Stopped trains Y and Z")

                
                
            if yRow2 == zRow2 and yCol2 == zCol2:
                
                planeY.stop()
                print "Future collision detected between X and Y at time ", t,". Stopped plane Y"
                if planeY.getflag() is False:
                    planeX.stop()
                    planeZ.stop()
                    print "Failure in train Y brake detected. Stopped trains X and Z"
                
            else:
                planeX.stop()
                
                print "Future collision detected between X and Y at time ", t,". Stopped plane X"
                if planeX.getflag() is False:
                    planeY.stop()
                    print "Failure in train X brake detected. Stopped train Y"
        #This code is to sync the positions in case a train does stop.
       
            
        if xRow1 == zRow1 and xCol1 == zCol1:
            if xRow2 == yRow2 and xCol2 == yCol2:
            
                planeX.stop()
                print "Future collision detected between X and Z at time ",t,". Stopped plane X"
                if planeX.getflag is False:
                    planeY.stop()
                    planeZ.stop()
                    print "Failure in train X brake detected. Stopped train Y and train Z"
                
            if zRow2 == yRow2 and zCol2 == yCol2:
                
                planeZ.stop() 
                print "Future collision detected between X and Z at time ,",t,". Stopped plane Z"
                if planeZ.getflag() is False:
                    planeX.stop()
                    planeY.stop()
                    print "Failure in train Z brake detected. Stopped train X and train Y"
                
            else:   
                
                planeX.stop()
                print "Future collision detected between X and z at time ,",t,". Stopped plane X"
                if planeX.getflag() is False:
                    planeZ.stop()
                    print "Failure in train X brake detected. Stopped train Z"
                
  
        if yRow1 == zRow1 and yCol1 == zCol1:
            if yRow2 == xRow2 and yCol2 == xCol2:
                
                planeY.stop()
                print "Future collision detected between Y and Z at time ",t,". Stopped plane Y"
                if planeY.getflag() is False:
                    planeX.stop()
                    planeZ.stop()
                    print "Failure in train Y brake detected. Stopped train X and train Z"
                
            if zRow2 == xRow2 and zCol2 == xCol2:
                
                planeZ.stop()

                print "Future collision detected between Y and Z at time ",t,". Stopped plane Z"

                if planeZ.getflag() is False:
                    planeX.stop()
                    planeY.stop()
                    print "Failure in train Z brake detected. Stopped train X and train Y"
                
           
            else:
                
                planeY.stop() 
                
                print "Future collision detected between Y and Z at time ",t,". Stopped plane Y"

                if planeY.getflag() is False:
                    planeZ.stop()
                    print "Failure in train Y brake detected. Stopped train Z"
     
                  
       
        
        
        
        
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

    

