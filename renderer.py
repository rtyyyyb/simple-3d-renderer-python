import turtle as t
import math as m
import time

# renderer functions
t.speed(0)
t.ht()
t.tracer(0, 0)
cam_x = 0
cam_y = 0
cam_z = 0
cam_pitch = 0
cam_roll = 0
cam_yaw = 0
focal_length = 0


def set_camera_pos(x, y, z, roll, pitch, yaw, focal_length):
    global cam_x
    global cam_y
    global cam_z
    global cam_pitch
    global cam_roll
    global cam_yaw
    cam_x = x
    cam_y = y
    cam_z = z
    cam_pitch = pitch
    cam_roll = roll
    cam_yaw = yaw
    focal_length = focal_length


def project_x(x, z, focal):  # projection matrix's
    return (x * focal) / (focal + z)


def project_y(y, z, focal):
    return (y * focal) / (focal + z)


def rotate_for_x(x, y, z, yaw, pitch, roll):  # rotation matrix's yaw = y axis, pitch = x axis, roll = y axis
    x = (x * m.cos(roll)) - (y * m.sin(roll))
    return (x * m.cos(yaw)) + (z * m.sin(yaw))


def rotate_for_y(x, y, z, yaw, pitch, roll):
    y = (x * m.sin(roll)) + (y * m.cos(roll))
    return (y * m.cos(pitch)) - (z * m.sin(pitch))


def rotate_for_z(x, y, z, yaw, pitch, roll):
    z = (y * m.sin(pitch)) + (z * m.cos(pitch))
    return (z * m.cos(yaw)) - (x * m.sin(yaw))


def next_frame():
    time.sleep(0.005)
    t.update()
    t.clear()

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
        x1 = project_x(temp_points[line[0] - 1][0], temp_points[line[0] - 1][2], focal_length)
        y1 = project_y(temp_points[line[0] - 1][1], temp_points[line[0] - 1][2], focal_length)
        x2 = project_x(temp_points[line[1] - 1][0], temp_points[line[1] - 1][2], focal_length)
        y2 = project_y(temp_points[line[1] - 1][1], temp_points[line[1] - 1][2], focal_length)
        t.pu()
        t.goto(x1, y1)
        t.pd()
        t.goto(x2, y2)