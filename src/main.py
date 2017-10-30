import threading
import time
import planeX
import planeY
import planeZ
import P1
import P2
import P3


class main:
    rows = 8
    columns = 7
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

    semA = threading.Semaphore()
    semB = threading.Semaphore()
    semC = threading.Semaphore()
    semD = threading.Semaphore()

    plane_X = planeX.planeX(0,0)
    plane_Y = planeY.planeY(0,2)
    plane_Z = planeZ.planeZ(3,6)

    p1 = P1.P1(0, plane_X, plane_Y, plane_Z, bufferA, bufferB, semA, semB)
    p2 = P2.P2(0, bufferC, bufferD, semA, semB, semC, semD)
    p3 = P3.P3(bufferC, bufferD, plane_X, plane_Y, plane_Z)
    #plane_X.stop()
    #plane_Y.stop()
    #plane_Z.stop()

    #thread class declarations
    i = 0
    t1 = threading.Thread(target=p1.proc1,args=(i, plane_X, plane_Y, plane_Z, bufferA, bufferB, semA, semB))
    t2 = threading.Thread(target=p2.proc, args=(i,bufferA,bufferB, bufferC, bufferD, semA, semB, semC, semD))
    t3 = threading.Thread(target=p3.check, args=(i, bufferC, bufferD, semC, semD,plane_X,plane_Y,plane_Z))
   
    t1.start()

    t2.start()

    t3.start()
    

    


