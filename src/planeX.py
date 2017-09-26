class planeX:
    def __init__(self, positionRow, positionCol):
        self.currentPos_Row = positionRow
        self.currentPos_Col = positionCol
#Moves Row+=(Row+1) % 8 | Col+=(Col+1) % 7
    def move(self, positionMatrix):
        lastPos_Row = (self.currentPos_Row - 1) % 8
        lastPos_Col = (self.currentPos_Col - 1) % 7
        self.subCheck(positionMatrix, lastPos_Row, lastPos_Col)
        #positionMatrix[lastPos_Row][lastPos_Col] = 0
        self.currentPos_Row = (self.currentPos_Row + 1) % 8
        self.currentPos_Col = (self.currentPos_Col + 1) % 7
        self.addCheck(positionMatrix)
        #positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'X'
      #  print("PLANE X")
       # print("Row:", self.currentPos_Row)
        #print("Column:", self.currentPos_Col)

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

    def subCheck(self, positionMatrix, lastPos_Row, lastPos_Col):
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





    

        
        

