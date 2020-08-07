#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu

import board
import busio
import adafruit_lsm9ds1


def execute():

  # ROS initialize
  rospy.init_node('adrv_imu', anonymous=False)
  rate = rospy.Rate(100)
  imu_pub = rospy.Publisher('imu', Imu, queue_size=10)

  # Initial Interface
  i2c = busio.I2C(board.SCL, board.SDA)
  sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)


  data = Imu()

  while not rospy.is_shutdown():
    ax, ay, az = sensor.acceleration
    mx, my, mz = sensor.magnetic
    gx, gy, gz = sensor.gyro
    temp = sensor.temperature

    data.linear_acceleration.x = ax
    data.linear_acceleration.y = ay
    data.linear_acceleration.z = az

    data.angular_velocity.x = gx
    data.angular_velocity.y = gy
    data.angular_velocity.z = gz

    imu_pub.publish(data)

    rate.sleep()



if __name__ == '__main__':
  try:
    execute()
  except rospy.ROSInterruptException as ex:
    rospy.logerr(ex)
  except Exception as ex:
    rospy.logerr(ex)
