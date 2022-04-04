sudo apt update && sudo apt upgrade -y
sudo apt install git python3 python3-pip
git clone https://github.com/lolenseu/xhash.git
cd xhash
python3 -m pip install -r requirements.txt
chmod +x bash-scrypts/install.sh
chmod +x bash-scrypts/update.sh
