import time
import random
class planeY:
    def __init__(self, positionRow, positionCol):
        self.currentPos_Row = positionRow
        self.currentPos_Col = positionCol
        self.lastPos_Row = 0
        self.futurePos_Row = 0
        self.futureFuturePos_Row=0
#Moves Row+=(Row+1) % 8 | Col+=2

    flag = False

    def move(self, positionMatrix):
        if self.flag is False:
            self.currentPos_Row = self.changeLeftRight()
            #lastPos_Row = (self.currentPos_Row-1)%8
            self.subCheck(positionMatrix, self.lastPos_Row, self.currentPos_Col, self.currentPos_Row, self.currentPos_Col)
        
        #if self.flag is False:

        self.subCheck(positionMatrix, self.lastLastPos_Row, self.currentPos_Col, self.currentPos_Row, self.currentPos_Col)
        self.addCheck(positionMatrix)
        
        

    def getRow(self):
        return self.currentPos_Row

    def getCol(self):
        return self.currentPos_Col

    def getLastRow(self):
        return self.lastPos_Row

    def getFutureRow(self):
        return self.futurePos_Row

    def getFutureFutureRow(self):
        return self.futureFuturePos_Row

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


    def changeLeftRight(self):
        dir = random.randint(0, 2)
        if dir == 1:
            self.lastPos_Row = (self.currentPos_Row - 1) % 8
            self.lastLastPos_Row = (self.lastPos_Row - 2) % 8
            self.futurePos_Row=(self.currentPos_Col + 2) % 8
            self.futureFuturePos_Row = (self.currentPos_Row + 3) % 8
            return (self.currentPos_Row + 1) % 8
        elif dir == 2:
            self.lastPos_Row = (self.currentPos_Row + 1) % 8
            self.lastLastPos_Row = (self.lastPos_Row + 2) % 8
            self.futurePos_Row=(self.currentPos_Col - 2) % 8
            self.futureFuturePos_Row = (self.currentPos_Row - 3) % 8
            return (self.currentPos_Row - 1) % 8
        elif dir == 0:
            return self.currentPos_Row

    def stop(self):
        if random.randint(0,99) > 5:
            self.flag=True
        else:
            print "failed to stop Y"
       

    def start(self):
        self.flag=False
    def getflag(self):
        return self.flag
    

        
