#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


def callback(data):
    br = CvBridge()
    rospy.loginfo('receiving image')
    dx = br.imgmsg_to_cv2(data)
    cv2.imshow("camera", dx)
    cv2.waitKey(1)



def listener():
    rospy.init_node('listenerim', anonymous=True)
    rospy.Subscriber('imager',Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    listener()
	##talker()
