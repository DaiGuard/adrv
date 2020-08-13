#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

from pwm_com import PWMCom


steer_vel = 0.0
drive_vel = 0.0


def recvTargetVel(data):

  global drive_vel
  global steer_vel

  drive_vel = data.linear.x
  steer_vel = data.angular.z


def linear_set(data, lower, upper, offset, dead):

  val = 0.0
  data = data + offset

  if data > 0.0:    
    val = abs(data / upper)

    if val > 1.0:
      val = 1.0

  else:
    val = - abs(data / lower)

    if val < -1.0:
      val = -1.0

  if abs(val) < dead and abs(val) > 0.0:
    val = val / abs(val) * dead

  return val


def execute():

  # Initialize rospy
  rospy.init_node('adrv_driver', anonymous=True)

  # Frame rate
  loop = rospy.Rate(60)

  # Paramaters
  steer_ch = 0
  drive_ch = 1
  steer_max = math.pi / 2.0
  steer_min = - math.pi / 2.0
  steer_offset = 0.0
  steer_dead = 0.0
  drive_max = 1.0
  drive_min = -1.0
  drive_offset = 0.0
  drive_dead = 0.0

  try:
    steer_ch = rospy.get_param('~steer_ch')
    drive_ch = rospy.get_param('~drive_ch')
  except rospy.ROSException:
    pass

  # Subscribe
  rospy.Subscriber('cmd_vel', Twist, recvTargetVel)

  # PWM Communicator initialize
  com = PWMCom(1, 100.0)
  ret, message = com.InitPWM(steer_ch, 0.0008, 0.0022)
  if not ret:
    raise Exception(message)

  ret, message = com.InitPWM(drive_ch, 0.001, 0.002)
  if not ret:
    raise Exception(message)

  # Loop
  while not rospy.is_shutdown():

    # Runtime parameter update
    try:
      steer_max = rospy.get_param('~steer_max')
      steer_min = rospy.get_param('~steer_min')
      steer_offset = rospy.get_param('~steer_offset')
      steer_dead = rospy.get_param('~steer_dead')
      drive_max = rospy.get_param('~drive_max')
      drive_min = rospy.get_param('~drive_min')
      drive_offset = rospy.get_param('~drive_offset')
      drive_dead = rospy.get_param('~drive_dead')

    except rospy.ROSException:
      pass
    
    ret, message = com.SetPWM(steer_ch, linear_set(steer_vel, steer_min, steer_max, steer_offset, steer_dead))
    if not ret:
      rospy.logwarn(message)

    ret, message = com.SetPWM(drive_ch, linear_set(drive_vel, drive_min, drive_max, drive_offset, drive_dead))
    if not ret:
      rospy.logwarn(message)

    loop.sleep()


if __name__ == '__main__':
  try:
    execute()
  except rospy.ROSInterruptException as ex:
    rospy.logerr(ex)
  except KeyboardInterrupt:
    rospy.logwarn("keyboard interrupt")
  except Exception as ex:
    rospy.logerr(ex)
    