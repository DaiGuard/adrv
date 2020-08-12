#!/bin/bash
echo -e "\e[34m----------- [master]: ROS Network Configure ------------\e[m";
echo -e "\e[34m    _   _     __        __    ______    _____     ____  \e[m";
echo -e "\e[34m    /  /|     / |     /    )    /       /    '    /    )\e[m";
echo -e "\e[34m---/| /-|----/__|-----\--------/-------/__-------/___ /-\e[m";
echo -e "\e[34m  / |/  |   /   |      \      /       /         /    |  \e[m";
echo -e "\e[34m_/__/___|__/____|__(____/____/_______/____ ____/_____|__\e[m";

HostIP="192.168.50.53"

echo "Host  : $HostIP"
echo "export ROS_IP=$HostIP"
# export ROS_IP=$1
export ROS_IP=$HostIP
