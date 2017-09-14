class planeX:
    def __init__(self, positionRow, positionCol):
        self.currentPos_Row = positionRow
        self.currentPos_Col = positionCol
#Moves Row+=(Row+1) % 8 | Col+=(Col+1) % 7
    def move(self, Matrix):
        positionMatrix = Matrix
        positionMatrix[self.currentPos_Row][self.currentPos_Col] = 0
        self.currentPos_Row = (self.currentPos_Row + 1) % 8
        self.currentPos_Col = (self.currentPos_Col + 1) % 7
        positionMatrix[self.currentPos_Row][self.currentPos_Col] = 'X'
        print("PLANE X")
        print("Row:", self.currentPos_Row)
        print("Column:", self.currentPos_Col)




    

        
        

