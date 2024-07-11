import numpy as np
import matplotlib.pyplot as plt

def configure_plot():
    fig = plt.figure()
    #plt.clf()
    # add an ax for 3D projecting
    ax = fig.add_subplot(111, projection='3d')
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    # same scale for all axes
    crange = 1.5
    ax.set_xlim(-crange, crange)
    ax.set_ylim(-crange, crange)
    ax.set_zlim(-crange, crange)

    ax.quiver(0, 0, 0, 1, 0, 0, color='g', length=2, arrow_length_ratio=0.15)
    ax.quiver(0, 0, 0, 0, 1, 0, color='b', length=2, arrow_length_ratio=0.15)
    ax.quiver(0, 0, 0, 0, 0, 1, color='r', length=2, arrow_length_ratio=0.15)
    # display axes names near the quivers
    ax.text(2, 0, 0, 'X', color='g')
    ax.text(0, 2, 0, 'Y', color='b')
    ax.text(0, 0, 2, 'Z', color='r')
    return fig, ax

def draw_bounding_box(ax, bb):
    _bb=[]
    corners = np.array([[bb[0][0], bb[0][1], bb[0][2]],
                        [bb[0][0], bb[0][1], bb[1][2]],
                        [bb[0][0], bb[1][1], bb[0][2]],
                        [bb[0][0], bb[1][1], bb[1][2]],
                        [bb[1][0], bb[0][1], bb[0][2]],
                        [bb[1][0], bb[0][1], bb[1][2]],
                        [bb[1][0], bb[1][1], bb[0][2]],
                        [bb[1][0], bb[1][1], bb[1][2]]])
    # draw the bounding box
    # draw the rectangle with minimum z value
    _bb += ax.plot(corners[[0, 1, 3, 2, 0], 0], corners[[0, 1, 3, 2, 0], 1], corners[[0, 1, 3, 2, 0], 2], 'r', lw=2)
    # draw the rectangle with maximum z value
    _bb += ax.plot(corners[[4, 5, 7, 6, 4], 0], corners[[4, 5, 7, 6, 4], 1], corners[[4, 5, 7, 6, 4], 2], 'r', lw=2)

    # draw lines connecting the two rectangles
    for i in range(4):
        _bb += ax.plot([corners[i, 0], corners[i + 4, 0]], [corners[i, 1], corners[i + 4, 1]],
                [corners[i, 2], corners[i + 4, 2]], 'r', lw=2)
    return _bb

def scale_and_rotate(v,bb):
    theta = np.radians(90)
    rot = np.array([[np.cos(theta), 0, np.sin(theta)],
                    [0, 1, 0],
                    [-np.sin(theta), 0, np.cos(theta)]])

    v = np.dot(v, rot)
    bb = np.dot(bb, rot)
    # rotate the mesh : +90 degrees around the x-axis
    theta = np.radians(-90)
    rot = np.array([[1, 0, 0],
                    [0, np.cos(theta), -np.sin(theta)],
                    [0, np.sin(theta), np.cos(theta)]])
    v = np.dot(v, rot)
    bb = np.dot(bb, rot)
    scale = 2 / np.max(np.abs(v))
    v *= scale
    bb *= scale
    return v,bb