import sys
import planeX
import planeY
import planeZ
import time
import P1
import threading

class main:
    rows = 8
    columns = 7
    planeloc = [[0 for x in range(columns)] for y in range(rows)]
    planeloc[0][0] = 'X'
    planeloc[0][2] = 'Y'
    planeloc[3][6] = 'Z'
    bufferA = [[0 for x in range(columns)] for y in range(rows)]
    bufferA[0][0] = 'X'
    bufferA[0][2] = 'Y'
    bufferA[3][6] = 'Z'

    bufferB = [[0 for x in range(columns)] for y in range(rows)]
    bufferC = [[0 for x in range(3)] for y in range (3)]
    bufferD = [[0 for x in range(3)] for y in range (3)]
    bufferC[0][0] = 'X'
    bufferC[0][1] = 'Y'
    bufferC[0][2] = 'Z'
    bufferD[0][0] = 'X'
    bufferD[0][1] = 'Y'
    bufferD[0][2] = 'Z'
    print (bufferA)

    plane_X = planeX.planeX(0,0)
    plane_Y = planeY.planeY(0,2)
    plane_Z = planeZ.planeZ(3,6)

    
    for i in range(0,20):
        time.sleep(1)
        #Process 1 work
        if i % 2 == 0:
            plane_X.move(bufferB)
            plane_Y.move(bufferB)
            plane_Z.move(bufferB)
        else:
            plane_X.move(bufferA)
            plane_Y.move(bufferA)
            plane_Z.move(bufferA)

        print("BUFFER A", bufferA)
        print("BUFFER B", bufferB)
        
        for i in range(len(bufferA)):
            for j in range(len(bufferA[i])):
                if bufferA[i][j] == 'X' or bufferA[i][j] == 'XY' or bufferA[i][j] == 'XZ' or bufferA[i][j] == 'XYZ':
                    bufferC[1][0] = i
                    bufferC[2][0] = j
                elif bufferA[i][j] == 'Y' or bufferA[i][j] == 'XY' or bufferA[i][j] == 'YZ' or bufferA[i][j] == 'XYZ':
                    bufferC[1][1] = i
                    bufferC[2][1] = j
                elif bufferA[i][j] == 'Z' or bufferA[i][j] == 'XZ' or bufferA[i][j] == 'YZ' or bufferA[i][j] == 'XYZ':
                    bufferC[1][2] = i
                    bufferC[2][2] = j
                else:
                    pass

        for i in range(len(bufferB)):
            for j in range(len(bufferB[i])):
                if bufferB[i][j] == 'X' or bufferB[i][j] == 'XY' or bufferB[i][j] == 'XZ' or bufferB[i][j] == 'XYZ':
                    bufferD[1][0] = i
                    bufferD[2][0] = j
                elif bufferB[i][j] == 'Y' or bufferB[i][j] == 'XY' or bufferB[i][j] == 'YZ' or bufferB[i][j] == 'XYZ':
                    bufferD[1][1] = i
                    bufferD[2][1] = j
                elif bufferB[i][j] == 'Z' or bufferB[i][j] == 'XZ' or bufferB[i][j] == 'YZ' or bufferB[i][j] == 'XYZ':
                    bufferD[1][2] = i
                    bufferD[2][2] = j
                else:
                    pass

        print("BUFFER C")
        print(bufferC)
        print("BUFFER D")
        print(bufferD)


#def fillBufferC(plane_X, plane_Y, plane_Z):
    #Plane X
    #bufferC[0][1] = plane_X.getRow()
    #Plane Y
    #Plane Z

     
    #Process 3 Work
    


