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
    posx = m.sin(i / 100) * 100
    posy = m.sin((i / 100) + 1.570795) * 100
    posz = m.sin(i / 100) * 100
    r.render_object(posx, posy, posz + 100, 0, i / 100, 0, cube_points, cube_connections)
    posx = m.sin(i / 100 + 3.14159) * 100
    posy = m.sin((i / 100 + 3.14159) + 1.570795) * 100
    posz = m.sin(i / 100 + 3.14159) * 100
    r.render_object(posx, posy, posz + 100, i / 100, 0, 0, cube_points, cube_connections)
    r.next_frame()
