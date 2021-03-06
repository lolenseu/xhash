<a href="https://github.com/lolenseu/xhash"><img src="https://img.shields.io/badge/license-MIT License-orange"></a> 
<a href="https://github.com/lolenseu/xhash"><img src="https://img.shields.io/badge/OPEN--SOURCE-YES-green"></a>


# XHASH
XHash is a simple Encrypting and Decrypting tool build in Python.
- XHash are using its own xh1 or xhash1 converting process just like ascii or base64 converting process.
- XHash are free to use and opensource tool/software.
- xh1 or xhash1 are the version 1.0 of the tool.


## How to clone and install requirements
```BASHc
sudo apt update && sudo apt upgrade -y
sudo apt install git python3 python3-pip
git clone https://github.com/lolenseu/xhash.git
cd xhash
python3 -m pip install -r requirements.txt
chmod +x bash-scrypts/install.sh
chmod +x bash-scrypts/update.sh
```
or
```BASHc
sudo curl https://raw.githubusercontent.com/lolenseu/xhash/main/bash-scrypts/install.sh > xhash-install.sh && chmod +x xhash-install.sh && bash xhash-install.sh
```


## How to use
 Encrypting
```BASHc
python3 encryptxh1.py
```
 Decrypting
```BASHc
python3 decryptxh1.py
```


## Sample Screenshots and Steps to Use
### "Encrypting" Make a file 
![Screenshot_2022-03-16_03-50-20](https://user-images.githubusercontent.com/98665691/158477378-88c82baf-1930-463f-b94c-08bec186a307.png)
### Add a content to the file
![Screenshot_2022-03-16_03-53-01](https://user-images.githubusercontent.com/98665691/158477879-c8d26ef9-d1d7-4312-9956-89b58ef59ab5.png)
### Run the Encrypting Tool
![Screenshot_2022-03-16_04-04-24](https://user-images.githubusercontent.com/98665691/158478165-beded490-c896-419e-82b7-952ab18323d2.png)
### "Decrypting" Sample file 
![Screenshot_2022-03-16_04-06-45](https://user-images.githubusercontent.com/98665691/158478600-332fbd77-dcb2-4ec6-97c0-c6cc114da3ea.png)
### Run the Decrypting Tool
![Screenshot_2022-03-16_04-08-53](https://user-images.githubusercontent.com/98665691/158478697-c42e0af5-dfbf-49c0-b4bc-7acd51ebedc4.png)
### Decryted file
![Screenshot_2022-03-16_04-12-59](https://user-images.githubusercontent.com/98665691/158479119-242dc80c-348e-418a-86b0-5b7341639407.png)


## Notice
- Before you use the tools, don't forget to edit and disable the encryptxh1.py and decryptxh1.py update checker below each file! (Why this is enabled? - To inform you to each update or release from the github repository)
- Don't update immediately the tool if there is a new update this may cause an error in the encryption process, decrypt fist to the version you used in the encryption process!
- Don't lost your "filename.xh1" file because we don't make any backup to each encrypted file!
- Don't edit the encryted "filename.xh1" file it may couse a error or corrupted error that can't or unable read in encryption process!
- You can rename your file after the encryption process but make sure that have ".xh1" extention.
- You can modify or copy and apply to your code and projects you wish. Its free to use!


## Update and Bug Fixed
Update:
- Update Dictionary
- 3 Characters Encryption
- Decrypted and Encrypted file storage

Fixed:
- Can't read keys


## Future Updates
- xh2 a version 2.0 (Features: new encryption process, adding a small amount of security hashing process, and some changes in cli.)


## Versions

### xh1 (xhash1)
 - v0.3beta Latest

### xh2 (xhash2)
 - vNone Latest
