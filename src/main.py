#Group Members: Johnathon Monson, Armando Mercado, Ryan Sparks
#Most new code is in P3
#Added ability to define iteration count as well as movement delays. Setting movement delays too low (<.1) may cause some synchronization issues and will allow collisions to occur.
import threading
import time
import planeX
import planeY
import planeZ
import P1
import P2
import P3
import random


class main:
    rows = 8
    columns = 7
    bufferA = [[0 for x in range(columns)] for y in range(rows)]

    #varables at bottom to randomly generate coordinates for bufferA, nonzero chance of hitting an already taken coordinate set
    bufferAXVarX = random.randint(0,rows-1)
    bufferAXVarY = random.randint(0,columns-1)
    bufferAYVarX = random.randint(0,rows-1)
    bufferAYVarY = random.randint(0,columns-1)
    bufferAZVarX = random.randint(0, rows-1)
    bufferAZVarY = random.randint(0, columns-1)
    if((bufferAXVarX==bufferAYVarX or bufferAXVarX==bufferAZVarX or bufferAYVarX==bufferAZVarX) and (bufferAXVarY==bufferAYVarY or bufferAXVarY==bufferAZVarY or bufferAYVarX==bufferAZVarX)):#generate again if equal
        bufferAXVarX = random.randint(0, rows - 1)
        bufferAXVarY = random.randint(0, columns - 1)
        bufferAYVarX = random.randint(0, rows - 1)
        bufferAYVarY = random.randint(0, columns - 1)
        bufferAZVarX = random.randint(0, rows - 1)
        bufferAZVarY = random.randint(0, columns - 1)

    bufferA[bufferAXVarX][bufferAXVarY] = 'X'
    bufferA[bufferAYVarX][bufferAYVarY] = 'Y'
    bufferA[bufferAZVarX][bufferAZVarY] = 'Z'

    bufferB = [[0 for x in range(columns)] for y in range(rows)]
    bufferC = [[0 for x in range(3)] for y in range (3)]
    bufferD = [[0 for x in range(3)] for y in range (3)]
    bufferC[0][0] = 'X'
    bufferC[0][1] = 'Y'
    bufferC[0][2] = 'Z'
    bufferD[0][0] = 'X'
    bufferD[0][1] = 'Y'
    bufferD[0][2] = 'Z'
    interval = input("How long of a delay between train movements in seconds? ")
    itterations = input("How many times would you like the trains to move? ")
    semA = threading.Semaphore()
    semB = threading.Semaphore()
    semC = threading.Semaphore()
    semD = threading.Semaphore()
   

    plane_X = planeX.planeX(0,0)
    plane_Y = planeY.planeY(0,2)
    plane_Z = planeZ.planeZ(3,6)

    p1 = P1.P1(0, plane_X, plane_Y, plane_Z, bufferA, bufferB, semA, semB)
    p2 = P2.P2(0, bufferC, bufferD, semA, semB, semC, semD)
    p3 = P3.P3(bufferC, bufferD, plane_X, plane_Y, plane_Z,bufferAZVarX,bufferAYVarY)
    

    #thread class declarations
    i = 0
    t1 = threading.Thread(target=p1.proc1,args=(i, plane_X, plane_Y, plane_Z, bufferA, bufferB, semA, semB,semC, semD, interval, itterations))
    t2 = threading.Thread(target=p2.proc, args=(i,bufferA,bufferB, bufferC, bufferD, semA, semB, semC, semD, interval, itterations)) 
    t3 = threading.Thread(target=p3.check, args=(i, bufferC, bufferD, semC, semD,plane_X,plane_Y,plane_Z, semA, semB, interval, itterations))
   
    t1.start()

    t2.start()
    
    t3.start()
    

    


