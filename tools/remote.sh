#!/bin/bash
echo -e "\e[34m------------ [remote]: ROS Network Configure -------------\e[m";
echo -e "\e[34m    ____      _____     _   _       __    ______    _____ \e[m";
echo -e "\e[34m    /    )    /    '    /  /|     /    )    /       /    '\e[m";
echo -e "\e[34m---/___ /----/__-------/| /-|----/----/----/-------/__----\e[m";
echo -e "\e[34m  /    |    /         / |/  |   /    /    /       /       \e[m";
echo -e "\e[34m_/_____|___/____ ____/__/___|__(____/____/_______/____ ___\e[m";

HostIP=192.168.50.53
RemoteIP=192.168.50.50

echo "Remote: $RemoteIP"
echo "Host  : $HostIP"

echo "export ROS_IP=$RemoteIP"
echo "export ROS_MASTER_URI=http://$HostIP:11311"
export ROS_IP=$RemoteIP
export ROS_MASTER_URI=http://$HostIP:11311
