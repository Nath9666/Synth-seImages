import numpy as np

def euler_rotate(theta, phi):
    # create the rotation matrix
    cost=np.cos(theta)
    sint=np.sin(theta)
    cosp=np.cos(phi)
    sinp=np.sin(phi)
    rot = np.array([[cost*sinp, cost, sint*sinp,0],
                    [-cost*cosp, sint, -cost*sinp,0],
                    [-sinp, 0, cosp,0],
                    [0,0,0,1]])

    return rot