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

    print (bufferA)

    plane_X = planeX.planeX(0,0)
    plane_Y = planeY.planeY(0,2)
    plane_Z = planeZ.planeZ(5,6)

    #Proc1 = P1(bufferA, bufferB, plane_X, plane_Y, plane_Z)
    for i in range(0,20):
        time.sleep(1)
        #Proc1.move(i)
        if i % 2 == 0:
            plane_X.move(bufferA)
            plane_Y.move(bufferA)
            plane_Z.move(bufferA)

            #if i > 1:
             #   bufferB = bufferA
        #Need P2 to write bufferC
        else:
            plane_X.move(bufferB)
            plane_Y.move(bufferB)
            plane_Z.move(bufferB)
            #Need P2 to write bufferD

    
        print (bufferA)




