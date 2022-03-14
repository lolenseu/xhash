#!/bin/sh
cd
rm -rf xhash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git
git clone https://github.com/lolenseu/xhash.git
cd xhash
chmod +x update.sh
clear
