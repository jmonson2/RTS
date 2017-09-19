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


#def fillBufferC(plane_X, plane_Y, plane_Z):
    #Plane X
    #bufferC[0][1] = plane_X.getRow()
    #Plane Y
    #Plane Z

     
    #Process 3 Work
    


