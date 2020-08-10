#!/bin/bash
echo "---- master run ----";

cd ~/Workspaces/ros/rc_ws;
source devel/setup.bash;
source master.sh
roslaunch adrv_driver adrv_driver.launch

echo "";
read -p "Please place any key...";