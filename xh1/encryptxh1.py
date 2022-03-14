import os
import time
import json
import urllib.request

version = json.loads(open('../src/version.json', "r").read())
rxh1 = json.loads(open('../src/xh1/rxh1.json', "r").read())
xh1 = json.loads(open('../src/xh1/xh1.json', "r").read())

os.system('clear')
print("Verifying Software Version...")
time.sleep(1)

getversion = False
while not getversion:
    try:
        gitrawversion = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/lolenseu/xhash/main/src/version.json').read())
        gitrawrxh1 = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/lolenseu/xhash/main/src/xh1/rxh1.json').read())
        gitrawxh1 = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/lolenseu/xhash/main/src/xh1/xh1.json').read())
        getversion = True
    except:
        print("Please Connect to Internet!")
        exit()

def main(procces):
    strap = xh1[procces]
    a.write(strap[2:])

def ifversionok():
    os.system('clear')
    print("Checking your Software...")
    time.sleep(2)
    if version == gitrawversion and xh1 == gitrawxh1 and rxh1 == gitrawrxh1:
        os.system('clear')
        pass
    else:
        os.system('clear')
        print("Please Update your Software!")
        exit()

def mainprocces():
    global data
    global a

    counter = 0
    a = open('xhash.xh1', 'w')
    a.write('0x')

    os.system('clear')
    print("Type y to encrypt with file and x to encrypt with text")
    qchoice = input("Enter your choice: ").lower()

    if qchoice == 'y':
        fdata = input("Enter your File: ")
        data = open(fdata, 'r').read()
        for i in range(len(data[:-1])):
            main(data[counter])
            counter += 1
        time.sleep(2)
    elif qchoice == 'x':
        data = input("Enter a Text: ")
        for i in range(len(data)):
            main(data[counter])
            counter += 1
        time.sleep(2)
    else:
        os.system('clear')
        print("Enter a valid choice!")
        time.sleep(3)
        mainprocces()


ifversionok()
mainprocces()
print("Encrypting Done!")
