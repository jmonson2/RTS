import time
import random
class planeY:
    def __init__(self, positionRow, positionCol):
        self.currentPos_Row = positionRow
        self.currentPos_Col = positionCol
#Moves Row+=(Row+1) % 8 | Col+=2

    flag = False

    def move(self, positionMatrix):
        if self.flag is False:
            lastPos_Row = (self.currentPos_Row-1)%8
        self.subCheck(positionMatrix, lastPos_Row, self.currentPos_Col, self.currentPos_Row, self.currentPos_Col)
        
        if self.flag is False:
            self.currentPos_Row = (self.currentPos_Row + 1) % 8
        self.subCheck(positionMatrix, (lastPos_Row-1)%8, self.currentPos_Col, self.currentPos_Row, self.currentPos_Col) 
        self.addCheck(positionMatrix)
        
        

    def getRow(self):
        return self.currentPos_Row

    def getCol(self):
        return self.currentPos_Col

    def addCheck(self, positionMatrix):
       if positionMatrix[self.currentPos_Row][self.currentPos_Col] == 0:
            positionMatrix[self.currentPos_Row][self.currentPos_Col] =  'Y'
            return
       elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'X':
           positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'XY'
           return
       elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'Z':
           positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'YZ'
           return
       elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'XZ':
           positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'XYZ'
           return

    def subCheck(self, positionMatrix, lastPos_Row, lastPos_Col, currentPos_Row, currentPos_Col):
        #temprow
        #tempcol
        count = 0
        for i in range (0,7):
          
        
            for j in range (0,6):

                if (i != currentPos_Row or j != currentPos_Col) and positionMatrix[i][j] == 'Y':
                    positionMatrix[i][j] = 0
       
        
                
        if positionMatrix[lastPos_Row][lastPos_Col] == 'Y':
            positionMatrix[lastPos_Row][lastPos_Col] = 0
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'XY':
            positionMatrix[lastPos_Row][lastPos_Col] = 'X'
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'YZ':
            positionMatrix[lastPos_Row][lastPos_Col] = 'Z'
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'XYZ':
            positionMatrix[lastPos_Row][lastPos_Col] = 'XZ'
            return

    def stop(self):
        if random.randint(0,99) > 5:
            self.flag=True
        else:
            print "failed to stop Y"
       

    def start(self):
        self.flag=False
    def getflag(self):
        return self.flag
    

        
