#!/usr/bin/env python
import sys

import numpy as np

import robot_comm.srv
import rospy


def main():
    index = sys.argv[1]
    print index

    # Arm positions.
    P = []
    # Middle Bottom
    P.append(np.array([-86.8, 28.0, 20.2, 2.1, -88.5, 134.2]))
    # Middle Top
    P.append(np.array([-85.8, -1.2, -34.4, -1.4, 62.3, 140.5]))
    # Left
    P.append(np.array([-46.0, 4.3, -1.4, -92.5, 89.3, 224.1]))
    # Left Top
    P.append(np.array([-41.7, 17.2, 8.0, -90.7, 94.3, 274.1]))
    # Left Bottom
    P.append(np.array([-44.8, 6.8, -11.4, -92.5, 90.3, 204.6]))
    # Left Opposite
    P.append(np.array([-47.0, 4.5, 4.9, -101.4, 58.1, 234.9]))
    # Left Opposite Top
    P.append(np.array([-71.8, -2.4, 11.0, -109.3, 24.4, 235.0]))
    # Left Opposite Bottom
    P.append(np.array([-60.2, 4.9, 7.8, -108.0, 46.1, 233.5]))
    # Right

    rospy.wait_for_service('/abb140/robot_SetJoints')
    try:
        set_joints = rospy.SerivceProxy('/abb140/robot_SetJoints', robot_comm.srv.robot_SetJoints)
        req = robot_comm.srv.robot_SetJointsRequest()
        req.j1 = P[index][0]
        req.j2 = P[index][1]
        req.j3 = P[index][2]
        req.j4 = P[index][3]
        req.j5 = P[index][4]
        req.j6 = P[index][5]
        print req
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__=='__main__':
    main()
