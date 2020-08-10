#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

import math

# global variables
vel_pub = None
steer_max = 1.0
steer_min =-1.0
drive_max = 1.0
drive_min =-1.0

ave_rate = 0.1

def linear_set(data, lower, upper):

  val = 0.0

  if data > 0.0:    
    val = abs(data * upper)

    if val > upper:
      val = upper

  else:
    val = - abs(data * lower)

    if val < lower:
      val = lower

  return val

def joystickSubscribe(data: Joy):
  global steer_max
  global steer_min
  global drive_max
  global drive_min

  vel = Twist()

  vel.linear.x = linear_set(
                   math.pow(data.axes[1], 3),
                   drive_min, drive_max)
  vel.angular.z = linear_set(
                    math.pow(data.axes[2], 3),
                    steer_min, steer_max)

  if vel_pub is not None:
    vel_pub.publish(vel)

def excecute():

  global vel_pub
  global steer_max
  global steer_min
  global drive_max
  global drive_min

  # ROS initialize
  rospy.init_node('adrv_remote')
  rate = rospy.Rate(30)

  joy_sub = rospy.Subscriber('joy', Joy, joystickSubscribe, queue_size=10)
  vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

  while not rospy.is_shutdown():
    try:
      steer_max = rospy.get_param('~steer_max')
      steer_min = rospy.get_param('~steer_min')
      drive_max = rospy.get_param('~drive_max')
      drive_min = rospy.get_param('~drive_min')
        
    except KeyError as ex:
      rospy.logwarn_once(ex + "not found parameter")

      rate.sleep()


if __name__ == "__main__":
  try:
    excecute()
  except rospy.ROSInterruptException as ex:
    rospy.logerr(ex.msg)
  except Exception as ex:
    rospy.logerr(ex.msg)
