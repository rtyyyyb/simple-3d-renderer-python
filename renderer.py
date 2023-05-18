import turtle as t
t.speed(0)
t.ht()
focal = 200
t.tracer(0, 0)
points = [  
    [
    [100,100,100],
    [100,100,200],
    [200,100,200],
    [200,100,100],
    [100,200,100],
    [100,200,200],
    [200,200,200],
    [200,200,100]
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

def projectx(x,y,z,focal): #projection matrixes 
    return(x*focal)/(focal+z) 
def projecty(x,y,z,focal):
    return(y*focal)/(focal+z)

def rendershape(xpos,ypos,zpos,yaw,pitch,roll,shape): #object renderer
    temppoints = points[shape]
    tempconnections = connections[shape]
    for index in range(len(temppoints)):
        temppoints[index][0] = temppoints[index][0] + xpos
        temppoints[index][1] = temppoints[index][1] + ypos
        temppoints[index][2] = temppoints[index][2] + zpos
    for line in tempconnections:
        x1 = projectx(temppoints[line[0]-1][0],temppoints[line[0]-1][1],temppoints[line[0]-1][2],focal)
        y1 = projecty(temppoints[line[0]-1][0],temppoints[line[0]-1][1],temppoints[line[0]-1][2],focal)
        x2 = projectx(temppoints[line[1]-1][0],temppoints[line[1]-1][1],temppoints[line[1]-1][2],focal)
        y2 = projecty(temppoints[line[1]-1][0],temppoints[line[1]-1][1],temppoints[line[1]-1][2],focal)
        t.pu()
        t.goto(x1,y1)
        t.pd()
        t.goto(x2,y2)
    temppoints = []
    tempconnections = []
print(points)
rendershape(-150,-150,-100,0,0,0,0)
print(points)
rendershape(-150,-150,-100,0,0,0,0)
print(points)

