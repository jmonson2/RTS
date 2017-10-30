import time
class planeZ:
    def __init__(self, positionRow, positionCol):
        self.currentPos_Row = positionRow
        self.currentPos_Col = positionCol
#Moves Row+=3 | Col+=(Col+1) % 7

    flag = False

    def move(self, positionMatrix):
        lastPos_Col = (self.currentPos_Col-1) % 7
        self.subCheck(positionMatrix, self.currentPos_Row, lastPos_Col)
        #positionMatrix[self.currentPos_Row][lastPos_Col] = 0
        if self.flag is False:
            self.currentPos_Col = (self.currentPos_Col + 1) % 7
        self.addCheck(positionMatrix)
        #positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'Z'
     #   print("PLANE Z")
     #   print("Row:", self.currentPos_Row)
     #   print("Column:", self.currentPos_Col)

    def getRow(self):
        return self.currentPos_Row

    def getCol(self):
        return self.currentPos_Col

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

    def subCheck(self, positionMatrix, lastPos_Row, lastPos_Col):
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

    def stop(self):
        self.flag = True

    def start(self):
        self.flag = False
