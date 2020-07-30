# adrv

Auto drive robot vehicle packages in ROS

----------------------------------------

## Packages

```bash
adrv/
├ adrv_description/ # robot description urdf file
└ adrv_gazebo/      # gazebo simulator
```

- [adrv_description](httsp://github.com/DaiGuard/adrv/adrv_description)
- [adrv_gazebo](httsp://github.com/DaiGuard/adrv/adrv_gazebo)

## Installation

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

```bash
$ cd catkin_ws
$ catkin build
```

```bash
$ cd catkin_ws
$ source devel/setup.bash
$ roslaunch adrv_gazebo adrv_course.launch
```