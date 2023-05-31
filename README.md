# python 3D wireframe renderer package
## overview
this is a 3D wireframe rendering package that use the turtle package to draw the wirefraem to the screen. the renderer can render any wirefraem and can have it be at any position with any rotation (the rotation is based upond the 3 major axies and not the object itself and may result in odd distortion). it also supports a cappera position and orentation. it can handle any number of objects but may result in low frame times
## functions
the package has many functions to render shapes or other functions do do with 3D rendering.
the (current) list of functions is:
### render_object
(line 63 to 87 in renderer.py)
this is the main function of the renderer that renders the objects. it has 3 arguments for position, 3 arguments for orentation and 2 for the objects wireframe data 
```py
def render_object(x_pos, y_pos, z_pos, yaw, pitch, roll, points_list, connections_list):  # object renderer
    temp_points = []
    temp_connections = connections_list
    for index in range(len(points_list)):
        temp_sub_points = []
        temp_x = rotate_for_x(points_list[index][0], points_list[index][1], points_list[index][2], yaw, pitch,
                              roll) + x_pos - cam_x
        temp_y = rotate_for_y(points_list[index][0], points_list[index][1], points_list[index][2], yaw, pitch,
                              roll) + y_pos - cam_y
        temp_z = rotate_for_z(points_list[index][0], points_list[index][1], points_list[index][2], yaw, pitch,
                              roll) + z_pos - cam_z
        temp_sub_points.append(rotate_for_x(temp_x, temp_y, temp_z, cam_yaw, cam_pitch, cam_roll))
        temp_sub_points.append(rotate_for_y(temp_x, temp_y, temp_z, cam_yaw, cam_pitch, cam_roll))
        temp_sub_points.append(rotate_for_z(temp_x, temp_y, temp_z, cam_yaw, cam_pitch, cam_roll))
        temp_points.append(temp_sub_points)
    for line in temp_connections:
        if temp_points[line[0] - 1][2] >= -focal_length and temp_points[line[1] - 1][2] >= -focal_length:
            x1 = project_x(temp_points[line[0] - 1][0], temp_points[line[0] - 1][2], focal_length)
            y1 = project_y(temp_points[line[0] - 1][1], temp_points[line[0] - 1][2], focal_length)
            x2 = project_x(temp_points[line[1] - 1][0], temp_points[line[1] - 1][2], focal_length)
            y2 = project_y(temp_points[line[1] - 1][1], temp_points[line[1] - 1][2], focal_length)
            t.pu()
            t.goto(x1, y1)
            t.pd()
            t.goto(x2, y2)
```
### set_camera_pos
(line 17 to 31 in renderer.py) this willl change the cameras position in the 3D space. it has 3 arguments for position and 3 arguments for orentation
```py
def set_camera_pos(x, y, z, roll, pitch, yaw, focallength):
    global cam_x
    global cam_y
    global cam_z
    global cam_pitch
    global cam_roll
    global cam_yaw
    global focal_length
    cam_x = x
    cam_y = y
    cam_z = z
    cam_pitch = pitch
    cam_roll = roll
    cam_yaw = yaw
    focal_length = focallength
```
### next_frame
(line 57 to 60) this will update the frame buffer and clear the screen of any objects
```py
def next_frame():
    time.sleep(0.0166666)
    t.update()
    t.clear()
```
### rotate_for_x,y,z
(line 42 to 54) this will rotate any vertex based upon the orign of 0,0,0 
```py
def rotate_for_x(x, y, z, yaw, pitch, roll):  # rotation matrix's yaw = y axis, pitch = x axis, roll = y axis
    x = (x * m.cos(roll)) - (y * m.sin(roll))
    return (x * m.cos(yaw)) + (z * m.sin(yaw))


def rotate_for_y(x, y, z, yaw, pitch, roll):
    y = (x * m.sin(roll)) + (y * m.cos(roll))
    return (y * m.cos(pitch)) - (z * m.sin(pitch))


def rotate_for_z(x, y, z, yaw, pitch, roll):
    z = (y * m.sin(pitch)) + (z * m.cos(pitch))
    return (z * m.cos(yaw)) - (x * m.sin(yaw))
```
### project_x,y
(line 34 to 39) this will project any vertex to a 2d screen/display using weak perspectave projection
```py
def project_x(x, z, focal):  # projection matrix's
    return (x * focal) / (focal + z + 0.01)


def project_y(y, z, focal):
    return (y * focal) / (focal + z + 0.01)
```
## usage exsamples
### spining cubes
this is a demo to show 2 spining cubes orbiting eachother 
```py
import math as m
import renderer as r
cube_points = [  # vertex data for objects
    [-50, -50, -50],
    [-50, -50, 50],
    [50, -50, 50],
    [50, -50, -50],
    [-50, 50, -50],
    [-50, 50, 50],
    [50, 50, 50],
    [50, 50, -50]
]

cube_connections = [  # connection data for objects
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 1],
    [5, 6],
    [6, 7],
    [7, 8],
    [8, 5],
    [5, 1],
    [6, 2],
    [7, 3],
    [8, 4]
]

for i in range(100000):
    r.set_camera_pos(0, 0, 0, 0, 0, 0, 200)
    posx = m.sin(i / 100) * 100
    posy = m.sin((i / 100) + 1.570795) * 100
    posz = m.sin(i / 100) * 100
    r.render_object(posx, posy, posz + 100, 0, i / 100, 0, cube_points, cube_connections)
    posx = m.sin(i / 100 + 3.14159) * 100
    posy = m.sin((i / 100 + 3.14159) + 1.570795) * 100
    posz = m.sin(i / 100 + 3.14159) * 100
    r.render_object(posx, posy, posz + 100, i / 100, 0, 0, cube_points, cube_connections)
    r.next_frame()
```
### diagonal line
this will render a diagonal line and the camera will move along it 
```py
import renderer as r

cube_points = [  # vertex data for objects
    [-50, -50, -50],
    [-50, -50, 50],
    [50, -50, 50],
    [50, -50, -50],
    [-50, 50, -50],
    [-50, 50, 50],
    [50, 50, 50],
    [50, 50, -50]
]

cube_connections = [  # connection data for objects
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 1],
    [5, 6],
    [6, 7],
    [7, 8],
    [8, 5],
    [5, 1],
    [6, 2],
    [7, 3],
    [8, 4]
]

def render_cube(x, y, z):
    r.render_object(x*100, y*100, z*100, 0, 0, 0, cube_points, cube_connections)

for i in range(100000):
    r.set_camera_pos(i*2, 100, i*2, 0, 0, i/1000, 200)
    for j in range(10):
        render_cube(j, 0, j)
    r.next_frame()
```