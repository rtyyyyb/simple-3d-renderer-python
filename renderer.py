import turtle as t
import math as m
import time
t.speed(0)
t.ht()
t.tracer(0,0)

# object and renderer info
focal = 200
points = [ # vertex data for objects
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

connections = [ # connection data for objects
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

# renderer functions
def clear():
    t.clear()
def update():
    t.update()
def projectx(x,z,focal): #projection matrixes
    return(x*focal)/(focal+z) 
def projecty(y,z,focal):
    return(y*focal)/(focal+z)

def rotateforx(x,y,z,yaw,pitch,roll): #rotation matrixs yaw = y axis, pitch = x axis, roll = y axis
    x = (x*m.cos(roll))-(y*m.sin(roll))
    return (x*m.cos(yaw))+(z*m.sin(yaw))
def rotatefory(x,y,z,yaw,pitch,roll):
    y = (x*m.sin(roll))+(y*m.cos(roll))
    return (y*m.cos(pitch))-(z*m.sin(pitch))
def rotateforz(x,y,z,yaw,pitch,roll):
    z = (y*m.sin(pitch))+(z*m.cos(pitch))
    return (z*m.cos(yaw))-(x*m.sin(yaw))

def rendershape(xpos,ypos,zpos,yaw,pitch,roll,shape): #object renderer
    temppoints = []
    tempconnections = connections[shape]
    for index in range(len(points[shape])):
        tempsubpoints = []
        tempsubpoints.append(rotateforx(points[shape][index][0],points[shape][index][1],points[shape][index][2],yaw,pitch,roll) + xpos)
        tempsubpoints.append(rotatefory(points[shape][index][0],points[shape][index][1],points[shape][index][2],yaw,pitch,roll) + ypos)
        tempsubpoints.append(rotateforz(points[shape][index][0],points[shape][index][1],points[shape][index][2],yaw,pitch,roll) + zpos)
        temppoints.append(tempsubpoints)
    for line in tempconnections:
        x1 = projectx(temppoints[line[0]-1][0],temppoints[line[0]-1][2],focal)
        y1 = projecty(temppoints[line[0]-1][1],temppoints[line[0]-1][2],focal)
        x2 = projectx(temppoints[line[1]-1][0],temppoints[line[1]-1][2],focal)
        y2 = projecty(temppoints[line[1]-1][1],temppoints[line[1]-1][2],focal)
        t.pu()
        t.goto(x1,y1)
        t.pd()
        t.goto(x2,y2)
#render code
#for i in range(100000):
    #clear()
    #rendershape(180,0,0,i/100,0,0,0)
    #rendershape(0,0,0,0,i/100,0,0)
    #rendershape(-180,0,0,0,0,i/100,0)
    #rendershape(0,0,0,1,1,0,0)
    #time.sleep(0.005)
    #t.update()

for i in range(100000):
    posx = m.sin(i/100)*100
    posy = m.sin((i/100)+1.570795)*100
    posz = m.sin(i/100)*100
    clear()
    rendershape(posx,posy,posz+50,0,i/100,0,0)
    posx = m.sin(i/100+3.14159)*100
    posy = m.sin((i/100+3.14159)+1.570795)*100
    posz = m.sin(i/100+3.14159)*100
    rendershape(posx,posy,posz+50,i/100,0,0,0)
    time.sleep(0.005)
    t.update()
    



