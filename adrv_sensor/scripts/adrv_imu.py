#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu, MagneticField
from std_msgs.msg import Float64

import board
import busio
import adafruit_lsm9ds1
import math

def execute():

  # ROS initialize
  rospy.init_node('adrv_imu', anonymous=False)
  rate = rospy.Rate(100)

  data_pub = rospy.Publisher('imu/data', Imu, queue_size=10)
  mag_pub = rospy.Publisher('imu/mag', MagneticField, queue_size=10)
  temp_pub = rospy.Publisher('imu/temperature', Float64, queue_size=10)

  # Initial Interface
  i2c = busio.I2C(board.SCL, board.SDA)
  sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)


  data = Imu()
  mag = MagneticField()
  temp = Float64()

  while not rospy.is_shutdown():
    ax, ay, az = sensor.acceleration
    mx, my, mz = sensor.magnetic
    gx, gy, gz = sensor.gyro
    t = sensor.temperature

    data.header.frame_id = 'imu_link'
    data.header.stamp = rospy.Time().now()

    data.linear_acceleration.x = ax
    data.linear_acceleration.y = ay
    data.linear_acceleration.z = az

    data.angular_velocity.x = gx / 180 * math.pi
    data.angular_velocity.y = gy / 180 * math.pi
    data.angular_velocity.z = gz / 180 * math.pi

    mag.header.stamp = rospy.Time().now()
    mag.magnetic_field.x = mx
    mag.magnetic_field.y = my
    mag.magnetic_field.z = mz

    temp.data = t

    data_pub.publish(data)
    mag_pub.publish(mag)
    temp_pub.publish(temp)

    rate.sleep()



if __name__ == '__main__':
  try:
    execute()
  except rospy.ROSInterruptException as ex:
    rospy.logerr(ex)
  except Exception as ex:
    rospy.logerr(ex)
