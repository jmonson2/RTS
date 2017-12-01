import time
import random
class planeZ:
    def __init__(self, positionRow, positionCol):
        self.currentPos_Row = positionRow
        self.currentPos_Col = positionCol
        self.lastPos_Col = 0
        self.futurePos_Col = 0
        self.futureFuturePos_Col = 0
#Moves Row+=3 | Col+=(Col+1) % 7

    flag = False

    def move(self, positionMatrix):
        if self.flag is False: 
         #   lastPos_Col = (self.currentPos_Col-1) % 7
        #self.subCheck(positionMatrix, self.currentPos_Row, lastPos_Col, self.currentPos_Row, self.currentPos_Col)

        #if self.flag is False:
            self.currentPos_Col = self.changeUpDown()
            self.addCheck(positionMatrix)
            self.subCheck(positionMatrix, self.currentPos_Row, self.lastPos_Col, self.currentPos_Row, self.currentPos_Col)
     
    def getRow(self):
        return self.currentPos_Row

    def getCol(self):
        return self.currentPos_Col

    def getLastRow(self):
        return self.lastPos_Row

    def getLastCol(self):
        return self.lastPos_Col

    def getFutureRow(self):
        return self.futurePos_Row

    def getFutureCol(self):
        return self.futurePos_Col
    def getFutureFutureCol(self):
        return self.futureFuturePos_Col

    def addCheck(self, positionMatrix):
        if positionMatrix[self.currentPos_Row][self.currentPos_Col] == 0:
            positionMatrix[self.currentPos_Row][self.currentPos_Col] =  'Z'
            return
        elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'X':
            positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'XZ'
            return
        elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'Y':
            positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'YZ'
            return
        elif positionMatrix[self.currentPos_Row][self.currentPos_Col] == 'XY':
            positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'XYZ'
            return

    def subCheck(self, positionMatrix, lastPos_Row, lastPos_Col,currentPos_Row, currentPos_Col):
        count = 0
        
        for i in range (0,7):
          
        
            for j in range (0,6):

                if (i != currentPos_Row or j != currentPos_Col) and positionMatrix[i][j] == 'Z':
                    positionMatrix[i][j] = 0

        
                
        if positionMatrix[lastPos_Row][lastPos_Col] == 'Z':
            positionMatrix[lastPos_Row][lastPos_Col] = 0
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'XZ':
            positionMatrix[lastPos_Row][lastPos_Col] = 'X'
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'YZ':
            positionMatrix[lastPos_Row][lastPos_Col] = 'Y'
            return
        elif positionMatrix[lastPos_Row][lastPos_Col] == 'XYZ':
            positionMatrix[lastPos_Row][lastPos_Col] = 'XY'
            return

    def changeUpDown(self):
        dir = random.randint(0, 2)
        if dir == 1:
            self.lastPos_Col = (self.currentPos_Col - 1) % 7
            self.futurePos_Col = (self.currentPos_Col + 2) % 7
            self.futureFuturePos_Col = (self.currentPos_Col +3) % 7
            return (self.currentPos_Col + 1) % 7
        elif dir == 2:
            self.lastPos_Col = (self.currentPos_Col + 1) % 7
            self.futurePos_Col = (self.currentPos_Col - 2) % 7
            self.futureFuturePos_Col = (self.currentPos_Col - 3) % 7
            return (self.currentPos_Col - 1) % 7
        elif dir == 0:
            #self.lastPos_Col = (self.currentPos_Col - 1) % 7
            #self.futurePos_Col = (self.currentPos_Col + 2) % 7
            #self.futureFuturePos_Col = (self.currentPos_Col + 3) % 7
            return self.currentPos_Col

    def stop(self):
        if random.randint(0,99) >= 0:
            self.flag = True
        else:
            print "Failed to stop Z"

    def start(self):
        self.flag = False
    def getflag(self):
        return self.flag
