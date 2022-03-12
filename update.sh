#!/bin/sh
cd
rm -rf xh
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git
git clone https://github.com/lolenseu/xh.git
cd xh
chmod +x update.sh
clear
