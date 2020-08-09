#!/bin/bash
echo -e "\e[34m------------ [remote]: ROS Network Configure -------------\e[m";
echo -e "\e[34m    ____      _____     _   _       __    ______    _____ \e[m";
echo -e "\e[34m    /    )    /    '    /  /|     /    )    /       /    '\e[m";
echo -e "\e[34m---/___ /----/__-------/| /-|----/----/----/-------/__----\e[m";
echo -e "\e[34m  /    |    /         / |/  |   /    /    /       /       \e[m";
echo -e "\e[34m_/_____|___/____ ____/__/___|__(____/____/_______/____ ___\e[m";

usage=0

if [ $# != 2 ]; then
  usage=`expr $usage + 1`
else
  if [[ $1 =~ ^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
    if [[ $2 =~ ^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$ ]]; then
      echo "[OK]"
    else
      echo -e "\e[31m[ERR]: mismatch remote ip \e[m"
      usage=`expr $usage + 1`
    fi
  else
    echo -e "\e[31m[ERR]: mismatch host ip \e[m"
    usage=`expr $usage + 1`
  fi
fi

if [ $usage -gt 0 ]; then
  echo ""
  echo "Usage: ROS Network Configure"
  echo ""
  echo "  ./remote.sh <remote.ip> <host.ip>"
  echo ""
  echo "  ex. ./remote.sh 192.168.0.2 192.168.1"
  echo ""
  exit
fi

echo "Remote: $1"
echo "Host  : $2"

echo "export ROS_IP=$1"
echo "export ROS_MASTER_URI=http://$2:11311"
export ROS_IP=$1
export ROS_MASTER_URI=http://$2:11311
