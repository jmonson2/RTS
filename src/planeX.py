import time
import random
class planeX:
    def __init__(self, positionRow, positionCol):
        self.currentPos_Row = positionRow
        self.currentPos_Col = positionCol
#Moves Row+=(Row+1) % 8 | Col+=(Col+1) % 7
    flag = False #Flag is used to stop trains. The trains move if flag is false

    def move(self, positionMatrix):
        if self.flag is False:
            lastPos_Row = (self.currentPos_Row - 1) % 8
            lastPos_Col = (self.currentPos_Col - 1) % 7
        self.subCheck(positionMatrix, lastPos_Row, lastPos_Col, self.currentPos_Row, self.currentPos_Col)
        if self.flag is False:
            
            self.currentPos_Row = (self.currentPos_Row + 1) % 8
            self.currentPos_Col = (self.currentPos_Col + 1) % 7
        self.addCheck(positionMatrix)
        self.subCheck(positionMatrix, lastPos_Row, lastPos_Col, self.currentPos_Row, self.currentPos_Col)
        

    def getRow(self):
        return self.currentPos_Row

    def getCol(self):
        return self.currentPos_Col

    def addCheck(self, positionMatrix):
        if positionMatrix[self.currentPos_Row][self.currentPos_Col] == 0:
            positionMatrix[self.currentPos_Row][self.currentPos_Col] =  'X'
            return
        elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'Y':
            positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'XY'
            return
        elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'Z':
            positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'XZ'
            return
        elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'YZ':
            positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'XYZ'
            return
#New algorithm for removing past positions due to train stops. This is for planeX, planeY, and planeZ
    def subCheck(self, positionMatrix, lastPos_Row, lastPos_Col,currentPos_Row, currentPos_Col):
        count = 0
     
        for i in range (0,7):
          
        
            for j in range (0,6):

                if (i != currentPos_Row or j != currentPos_Col) and positionMatrix[i][j] == 'X':
                    positionMatrix[i][j] = 0
                        

        
                
        if positionMatrix[lastPos_Row][lastPos_Col] == 'X':
            positionMatrix[lastPos_Row][lastPos_Col] = 0
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'XY':
            positionMatrix[lastPos_Row][lastPos_Col] = 'Y'
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'XZ':
            positionMatrix[lastPos_Row][lastPos_Col] = 'Z'
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'XYZ':
            positionMatrix[lastPos_Row][lastPos_Col] = 'YZ'
            return

    def stop(self):
        if(random.randint(0,99) > -1):
            self.flag=True
        else:
            print "Failed to stop X"
            

    def start(self):
        self.flag=False
    def getflag(self):
        return self.flag
    
