import turtle as t
import math as m
import time
import numpy
t.speed(0)
t.ht()
t.tracer(0,0)
focal = 200
points = [  
    [
    [-50,-50,-50],
    [-50,-50,50],
    [50,-50,50],
    [50,-50,-50],
    [-50,50,-50],
    [-50,50,50],
    [50,50,50],
    [50,50,-50]
    ],
    [
    [200,100,100],
    [200,100,200],
    [200,100,100],
    [200,100,100],
    [200,200,100],
    [200,200,200],
    [200,200,100],
    [200,200,100]
    ]
    ]

connections = [
    [
    [1,2],
    [2,3],
    [3,4],
    [4,1],
    [5,6],
    [6,7],
    [7,8],
    [8,5],
    [5,1],
    [6,2],
    [7,3],
    [8,4]
    ],
    [
    [1,2],
    [2,3],
    [3,4],
    [4,1],
    [5,6],
    [6,7],
    [7,8],
    [8,5],
    [5,1],
    [6,2],
    [7,3],
    [8,4]
    ]
    ]

def clear():
    t.clear()
    
def projectx(x,y,z,focal): #projection matrixes 
    return(x*focal)/(focal+z) 
def projecty(x,y,z,focal):
    return(y*focal)/(focal+z)

def rotatex(x,y,z,radian): #rotation matrix 
    t
    
def rendershape(xpos,ypos,zpos,yaw,pitch,roll,shape): #object renderer
    temppoints = []
    tempconnections = connections[shape]
    for index in range(len(points[shape])):
        tempsubpoints = []
        tempsubpoints.append(points[shape][index][0] + xpos)
        tempsubpoints.append(points[shape][index][1] + ypos)
        tempsubpoints.append(points[shape][index][2] + zpos)
        temppoints.append(tempsubpoints)
    for line in tempconnections:
        x1 = projectx(temppoints[line[0]-1][0],temppoints[line[0]-1][1],temppoints[line[0]-1][2],focal)
        y1 = projecty(temppoints[line[0]-1][0],temppoints[line[0]-1][1],temppoints[line[0]-1][2],focal)
        x2 = projectx(temppoints[line[1]-1][0],temppoints[line[1]-1][1],temppoints[line[1]-1][2],focal)
        y2 = projecty(temppoints[line[1]-1][0],temppoints[line[1]-1][1],temppoints[line[1]-1][2],focal)
        t.pu()
        t.goto(x1,y1)
        t.pd()
        t.goto(x2,y2)
#render code
for i in range(1000000):
    posx = math.sin(i/100)*100
    posy = math.sin((i/100)+1.570795)*100
    posz = math.sin(i/100)*100
    clear()
    rendershape(posx,posy,posz+50,0,0,0,0)
    posx = math.sin(i/100+3.14159)*100
    posy = math.sin((i/100+3.14159)+1.570795)*100
    posz = math.sin(i/100+3.14159)*100
    rendershape(posx,posy,posz+50,0,0,0,0)
    t.update()
    



