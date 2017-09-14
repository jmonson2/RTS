class planeZ:
    def __init__(self, positionRow, positionCol):
        self.currentPos_X = positionRow
        self.currentPos_Col = positionCol
#Moves Row+=3 | Col+=(Col+1) % 7
    def move(self, positionMatrix):
        positionMatrix[self.currentPos_X][self.currentPos_Col] = 0
        
        self.currentPos_Col = (self.currentPos_Col + 1) % 7
        positionMatrix[self.currentPos_X][self.currentPos_Col] = 'Z'
        print("PLANE Z")
        print("Row:", self.currentPos_X)
        print("Column:", self.currentPos_Col)