#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import rosparam
import rospkg
import rosnode
import tf
import math

from std_srvs.srv import Empty, EmptyRequest, EmptyResponse
from geometry_msgs.msg import PoseArray, Pose, PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult
from actionlib_msgs.msg import GoalStatus
import actionlib


# ティーチ用ゴール保存のコールバック
def teach_goal(req):

  # TFデータを購読するクラス
  listener = tf.TransformListener()
  
  try:
    # 現在位置を取得する
    listener.waitForTransform('map', 'base_link', rospy.Time(), rospy.Duration(3.0))    
    (trans, rot) = listener.lookupTransform('map', 'base_link', rospy.Time(0))

    # 現在の登録位置を取得する
    goals = rospy.get_param('~goals')

    # 現在位置を登録位置に追加する    
    goals.append(trans + rot)
    rospy.set_param('~goals', goals)


  except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
    rospy.logerr('[goal_publisher]: not found robot position')
  except KeyError:
    rospy.logerr('[goal_publisher]: not found goals parameter')

  return EmptyResponse()


# # 
# feedback_pose = Pose()
# def feedback_cb(feedback):
#   global feedback_pose

#   feedback_pose = feedback.base_position.pose

# #
# status_id = 0
# def done_cb(state, result):
#   global status_id
#   status_id = state.status


# ノードメイン関数
def goal_publisher():

  # ROS初期化
  rospy.init_node('goal_publisher', anonymous=False)

  # ティーチ用保存コマンド
  rospy.Service('~teach_goal', Empty, teach_goal)

  # 登録位置データを確認用に配信する
  goals_pub= rospy.Publisher('~goals', PoseArray, queue_size=10)

  target_pub = rospy.Publisher('move_base_simple/goal', PoseStamped,queue_size=10)  

  # #   
  # client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
  # client.wait_for_server()  

  # ループ周波数の定義
  loop = rospy.Rate(1.0)

  goals = rospy.get_param('~goals')  

  pose_array = PoseArray()    
  pose_array.header.frame_id = 'map'

  for goal in goals:
    pose = Pose()

    pose.position.x = goal[0]
    pose.position.y = goal[1]
    pose.position.z = goal[2]
    pose.orientation.x = goal[3]
    pose.orientation.y = goal[4]
    pose.orientation.z = goal[5]
    pose.orientation.w = goal[6]

    pose_array.poses.append(pose)

  goals_pub.publish(pose_array)
  
  # global feedback_pose
  # global status_id

  # TFデータを購読するクラス
  listener = tf.TransformListener()

  for goal in goals:
    # act_goal = MoveBaseGoal()
    # act_goal.target_pose.header.frame_id = 'map'
    # # act_goal.target_pose.header.stamp = rospy.Time.now()
    # act_goal.target_pose.pose.position.x = goal[0]
    # act_goal.target_pose.pose.position.y = goal[1]
    # act_goal.target_pose.pose.position.z = goal[2]
    # act_goal.target_pose.pose.orientation.x = goal[3]
    # act_goal.target_pose.pose.orientation.y = goal[4]
    # act_goal.target_pose.pose.orientation.z = goal[5]
    # act_goal.target_pose.pose.orientation.w = goal[6]
        
    # client.send_goal(act_goal, done_cb=done_cb, feedback_cb=feedback_cb)
    
    # while not rospy.is_shutdown():
    #   dx = feedback_pose.position.x - goal[0]
    #   dy = feedback_pose.position.y - goal[1]      

    #   d = math.sqrt(dx * dx + dy * dy)

    #   print(dx, dy, d, status_id)

    #   if(d < 0.4):
    #     print("REACH")
    #     break

    #   loop.sleep()

    simple_goal = PoseStamped()
    simple_goal.header.frame_id = 'map'
    simple_goal.pose.position.x = goal[0]
    simple_goal.pose.position.y = goal[1]
    simple_goal.pose.position.z = goal[2]
    simple_goal.pose.orientation.x = goal[3]
    simple_goal.pose.orientation.y = goal[4]
    simple_goal.pose.orientation.z = goal[5]
    simple_goal.pose.orientation.w = goal[6]    

    target_pub.publish(simple_goal)      

    while not rospy.is_shutdown():

      try:
        (trans, rot) = listener.lookupTransform('map', 'base_link', rospy.Time(0))

        dx = trans[0] - goal[0]
        dy = trans[1] - goal[1]
        d = math.sqrt( dx * dx + dy * dy )

        print(dx, dy, d)

        if d < 0.4:
          break

      except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        pass

      loop.sleep()
    

  # # main loop
  # while not rospy.is_shutdown():
  #   # 現在の套路位置を取得する
  #   goals = rospy.get_param('~goals')

  #   pose_array = PoseArray()    
  #   pose_array.header.frame_id = 'map'

  #   for goal in goals:
  #     pose = Pose()

  #     pose.position.x = goal[0]
  #     pose.position.y = goal[1]
  #     pose.position.z = goal[2]
  #     pose.orientation.x = goal[3]
  #     pose.orientation.y = goal[4]
  #     pose.orientation.z = goal[5]
  #     pose.orientation.w = goal[6]

  #     pose_array.poses.append(pose)

  #   goals_pub.publish(pose_array)

  #   loop.sleep()


if __name__ == '__main__':

  try:
    goal_publisher()

  except rospy.ROSInterruptException:
    pass
  except Exception as ex:
    print ex.message

  # パラメータをバックアップパスを見つける  
  package = rospkg.RosPack()
  path = package.get_path('adrv_navigation')

  goals = rospy.get_param('~goals')
  
  with open(path + '/config/goal_list.yaml', mode='w') as file:    
    text = str(goals).replace('[[', '[\n[')
    text = text.replace('],', '],\n')
    text = text.replace(']]', ']\n]')
    file.write( 'goals: ' +  text)
    # file.write( 'goals: ' + str(goals).replace('[[', '[\n[').replace('],', '],\n').replace(']]', ']\n]') )
    