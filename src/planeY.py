class planeY:
    def __init__(self, positionRow, positionCol):
        self.currentPos_Row = positionRow
        self.currentPos_Col = positionCol
#Moves Row+=(Row+1) % 8 | Col+=2
    def move(self, positionMatrix):
        lastPos_Row = (self.currentPos_Row-1)%8
        positionMatrix[lastPos_Row][self.currentPos_Col] = 0
        self.currentPos_Row = (self.currentPos_Row + 1) % 8
        positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'Y'

        print("PLANE Y")
        print("Row:", self.currentPos_Row)
        print("Column:", self.currentPos_Col)
