#!/usr/bin/env python3

import rospy
from laser_assembler.srv import *
from sensor_msgs.msg import PointCloud2


def main():
    rospy.init_node("pt2_assembler", anonymous=True)
    rospy.wait_for_service("assemble_scans2")

    r = rospy.Rate(1)
    assemble_scans = rospy.ServiceProxy('assemble_scans2', AssembleScans2)
    pub = rospy.Publisher("/pt2_assembler", PointCloud2, queue_size=1)

    while True:
        try:
            resp = assemble_scans(rospy.Time(0, 0), rospy.get_rostime())
            print("Got cloud with %u points" % len(resp.cloud.data))
            pub.publish(resp.cloud)
        except rospy.ServiceException as e:
            print("Service call failed: %s" % e)
            break
        r.sleep()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        rospy.loginfo('%s stopped' % rospy.get_name())
