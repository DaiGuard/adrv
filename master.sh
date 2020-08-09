#!/bin/bash
echo -e "\e[34m----------- [master]: ROS Network Configure ------------\e[m";
echo -e "\e[34m    _   _     __        __    ______    _____     ____  \e[m";
echo -e "\e[34m    /  /|     / |     /    )    /       /    '    /    )\e[m";
echo -e "\e[34m---/| /-|----/__|-----\--------/-------/__-------/___ /-\e[m";
echo -e "\e[34m  / |/  |   /   |      \      /       /         /    |  \e[m";
echo -e "\e[34m_/__/___|__/____|__(____/____/_______/____ ____/_____|__\e[m";

usage=0

if [ $# != 1 ]; then
  usage=`expr $usage + 1`
else
  if [[ $1 =~ ^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
    echo "[OK]"
  else
    echo -e "\e[31m[ERR]: mismatch host ip \e[m"
    usage=`expr $usage + 1`
  fi
fi

if [ $usage -gt 0 ]; then
  echo ""
  echo "Usage: ROS Network Configure"
  echo ""
  echo "  ./master.sh <host.ip>"
  echo ""
  echo "  ex. ./master.sh 192.168.1"
  echo ""
  exit
fi

echo "Host  : $1"

echo "export ROS_IP=$1"
export ROS_IP=$1
