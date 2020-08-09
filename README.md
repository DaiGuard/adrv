# adrv

Auto drive robot vehicle packages in ROS

----------------------------------------

## Packages

ADRV all packages

----------------------------------------

```bash
adrv/
├ adrv_description/ # robot description urdf file
├ adrv_driver/      # robot motor driver
├ adrv_gazebo/      # gazebo simulator
├ adrv_remote/      # robot remote controller
└ adrv_sensor/      # robot sensor packages

```

- [adrv_description](https://github.com/DaiGuard/adrv/adrv_description)
- [adrv_driver](https://github.com/DaiGuard/adrv/adrv_driver)
- [adrv_gazebo](https://github.com/DaiGuard/adrv/adrv_gazebo)
- [adrv_remote](https://github.com/DaiGuard/adrv/adrv_remote)
- [adrv_sensor](https://github.com/DaiGuard/adrv/adrv_sensor)

## Installation

ADRV packages installation

----------------------------------------

* clone repository

```bash
$ mkdir -p catkin_ws/src
$ cd catkin_ws/src
$ git clone https://github.com/DaiGuard/adrv
```

* install depend repository

```bash
$ cd catkin_ws
$ wstool init src
$ wstool merge -t src src/adrv/adrv.rosinstall
$ wstool update -t src
```

```bash
$ cd catkin_ws
$ sudo rosdep init
$ rosdep update
$ rosdep install --from-paths src --ignore-src -y
```

## Build & Run

ADRV build and way of running

* Runnting mode

  - Remote control mode

----------------------------------------

```bash
$ cd catkin_ws
$ catkin build
```

```bash
$ cd catkin_ws
$ source devel/setup.bash
$ roslaunch adrv_gazebo adrv_course.launch
```

* ### Remote Control Mode

----------------------------------------


## Memo

* ### ROS on Python3

  Reference: [Jetbot+ROS+Python3環境構築](https://masato-ka.hatenablog.com/entry/2019/07/17/065000)

  ```bash
  $ sudo pip3 install rospkg catkin_pkg
  ```