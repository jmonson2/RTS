import time
class planeY:
    def __init__(self, positionRow, positionCol):
        self.currentPos_Row = positionRow
        self.currentPos_Col = positionCol
#Moves Row+=(Row+1) % 8 | Col+=2

    flag = False

    def move(self, positionMatrix):
        lastPos_Row = (self.currentPos_Row-1)%8
        self.subCheck(positionMatrix, lastPos_Row, self.currentPos_Col)
        #positionMatrix[lastPos_Row][self.currentPos_Col] = 0
        if self.flag is False:
            self.currentPos_Row = (self.currentPos_Row + 1) % 8 
        self.addCheck(positionMatrix)
        #positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'Y'
     #   print("PLANE Y")
     #   print("Row:", self.currentPos_Row)
     #   print("Column:", self.currentPos_Col)

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

    def subCheck(self, positionMatrix, lastPos_Row, lastPos_Col):
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
       self.flag=True

    def start(self):
        self.flag=False
    def getflag(self):
        return self.flag

        
