#!/bin/bash
echo "---- remote control ----";

cd ~/Workspaces/ros/rc_ws;
source devel/setup.bash;
source remote.sh
roslaunch adrv_remote adrv_remote.launch

echo "";
read -p "Please place any key...";