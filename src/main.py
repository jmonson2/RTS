import sys
import planeX
import planeY
import planeZ
import time
import P1
import P2
import P3
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
   # print (bufferA)
    semA = threading.Semaphore()
    semB = threading.Semaphore()
    semC = threading.Semaphore()
    semD = threading.Semaphore()

    plane_X = planeX.planeX(0,0)
    plane_Y = planeY.planeY(0,2)
    plane_Z = planeZ.planeZ(3,6)
    p1 = P1.P1(0, plane_X, plane_Y, plane_Z, bufferA, bufferB, semA, semB)
    p2 = P2.P2(0, bufferC, bufferD)
    p3 = P3.P3(bufferC, bufferD)

    #thread class declarations
    i = 0
    t1 = threading.Thread(target=p1.proc1,args=(i, plane_X, plane_Y, plane_Z, bufferA, bufferB, semA, semB))
    t2ac = threading.Thread(target=p2.proc2AC, args=(i,bufferA,bufferC))
    t2bd = threading.Thread(target=p2.proc2BD, args=(i,bufferA,bufferC))
    t3c = threading.Thread(target=p3.checkC, args=(i, bufferC))
    t3d = threading.Thread(target=p3.checkD, args=(i, bufferC))

    t1.start()
    for i in range(0,20):
        print("")
      #  print("")
      #  print("")
      #  print("TIME ", i+1)
     #   print("")

        time.sleep(1)
        #Process 1 work
        
        #p1.proc1(i, plane_X, plane_Y, plane_Z, bufferA, bufferB)
        #t1.run()
        
        #Process 2 Work
        if i % 2 is 0:
            p2.proc2AC(i,bufferA,bufferC, semA, semC)
        else:
            p2.proc2BD(i, bufferB, bufferD, semB, semD)

        #Process 3 Work
        if i % 2 is 0:
            p3.checkC(i, bufferC)
        else:  
            p3.checkD(i, bufferD)
      #  print("BUFFER C")
      #  print(bufferC)
      #  print("BUFFER D")
      #  print(bufferD)

    


