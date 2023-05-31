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
