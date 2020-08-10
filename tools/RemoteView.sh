#!/bin/bash
echo "---- remote view ----";

cd ~/Workspaces/ros/rc_ws;
source devel/setup.bash;
source remote.sh
roslaunch adrv_rviz adrv_rviz.launch

echo "";
read -p "Please place any key...";