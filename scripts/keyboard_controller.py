#!/usr/bin/env python

import pygame
import rospy
from geometry_msgs.msg import Pose
import time



pygame.init()
size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dobot Controller")


def Controller():
    done = False
    x_coord = 200
    y_coord = 0
    z_coord = 0
    r_coord = 0
    dx = 0
    dy = 0
    dz = 0
    dr = 0
    grip = 0

    pub = rospy.Publisher('geometry_pose', Pose, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(0.5) # 10hz


    t1 = time.time()
    while not done:
        t2 = time.time()

        if t2-t1>0.1:
            x_coord += dx
            y_coord += dy
            z_coord += dz
            r_coord += dr
            t1 = t2

            msg = Pose()
            msg.position.x = x_coord
            msg.position.y = y_coord
            msg.position.z = z_coord
            msg.orientation.x = r_coord
            pub.publish(msg)
            



        print("X={} Y={} Z={} R={} G={}".format(x_coord,y_coord,z_coord,r_coord,grip))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dy = 1
                elif event.key == pygame.K_RIGHT:
                    dy = -1
                elif event.key == pygame.K_UP:
                    dx = 1
                elif event.key == pygame.K_DOWN:
                    dx = -1
                elif event.key == pygame.K_a:
                    dr = 1
                elif event.key == pygame.K_d:
                    dr = -1
                elif event.key == pygame.K_w:
                    dz = 1
                elif event.key == pygame.K_s:
                    dz = -1
                elif event.key ==  pygame.K_RETURN:
                    grip = 1
                elif event.key == pygame.K_ESCAPE:
                    done = True
    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dy = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    dx = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    dr = 0
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    dz = 0
                elif event.key == pygame.K_RETURN:
                    grip = 0

    pygame.quit()



if __name__ == '__main__':
    try:
        Controller()
    except rospy.ROSInterruptException:
        pass