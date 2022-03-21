import os
import time
import json
import random
import urllib.request

#Files needed to run the program.
version = json.loads(open('../src/version.json', "r").read())
rxh1 = json.loads(open('../src/xh1/rxh1.json', "r").read())
xh1 = json.loads(open('../src/xh1/xh1.json', "r").read())

#Version verification and other files needed.
def ifversionok():
    os.system('clear')
    print("Verifying Software Version...")
    time.sleep(1)

    getversion = False
    while not getversion:
        try:
            global gitrawversion, gitrawrxh1, gitrawxh1
            gitrawversion = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/lolenseu/xhash/main/src/version.json').read())
            gitrawrxh1 = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/lolenseu/xhash/main/src/xh1/rxh1.json').read())
            gitrawxh1 = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/lolenseu/xhash/main/src/xh1/xh1.json').read())
            getversion = True
        except:
            print("Please Connect to Internet!")
            exit()

    #Checking the Software files.
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

#Encrypting procces.
def mainprocces():
    global data

    #Input file or text from the user.
    os.system('clear')
    print("Type y to encrypt with file and x to encrypt with text")
    qchoice = input("Enter your choice: ").lower()

    if qchoice == 'y':
        fdata = input("Enter your File or Directory: ")
        data = open(fdata, 'r').read()
    elif qchoice == 'x':
        tdata = input("Enter a Text: ")
        data = tdata
    else:
        os.system('clear')
        print("Enter a valid choice!")
        time.sleep(2)
        mainprocces()

    #Generating new file to save the hash.
    time.sleep(3)
    print("Encrypting...")
    genfilename = ''.join((random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(8)))
    filename = genfilename + '.xh1'
    a = open(filename, 'w')
    a.write('0x')

    #Starting the ncrypting procces.
    counter = 0
    for i in range(len(data)):
        procces = data[counter]
        strap = xh1[procces]
        a.write(strap[2:])
        counter += 1

    print("Encrypting Done!")
    print("Your Encrypted file saved to: " + str(filename))


ifversionok() #Put hashtag here to cancel or bypass the version verification!, example: "#ifversionok()".
mainprocces()
