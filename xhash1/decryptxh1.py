import os
import time
import json
import random
import urllib.request

#Files needed to run the program.
version = json.loads(open('../src/xh1/version.json', "r").read())
xh1 = json.loads(open('../src/xh1/xh1.json', "r").read())

#Version verification and other files needed.
def ifversionok():
    os.system('clear')
    print("Verifying Software Version...")
    time.sleep(1)

    getversion = False
    while not getversion:
        try:
            global gitrawversion, gitrawxh1
            gitrawversion = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/lolenseu/xhash/main/src/xh1/version.json').read())
            gitrawxh1 = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/lolenseu/xhash/main/src/xh1/xh1.json').read())
            getversion = True
        except:
            print("Please Connect to Internet!")
            exit()

    #Checking the Software files.
    os.system('clear')
    print("Checking your Software...")
    time.sleep(2)

    if version == gitrawversion and xh1 == gitrawxh1:
        os.system('clear')
        pass
    else:
        os.system('clear')
        print("Please Update your Software!")
        exit()

#Decrypting procces.
def mainprocces():
    global data

    #Input file from the user.
    os.system('clear')
    fdata = input("Enter your File or Directory: ")

    if fdata[-4:] == '.xh1':
        data = open(fdata, 'r').read()
    else:
        os.system('clear')
        print("Enter a valid file!")
        time.sleep(2)
        mainprocces()

    #Checking the file.
    if data[:2] != '0x':
        os.system('clear')
        print("Ops! Your file are invalid or corrupted,\nMake sure it start wtih \"0x\", Example: \"0x00000000\".")
        exit()
    else:
        pass

    #Generating new file to save the decrypted hash.
    time.sleep(3)
    print("Decrypting...")
    genfilename = ''.join((random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(8)))
    filename = genfilename
    a = open(f'decrypted-files/{filename}', 'w')

    #Starting the decrypting procces.
    numsdata = data[2:]
    countdata = data[2:]
    countdata = len(countdata) / 3
    counter1 = 0
    counter2 = 3
    for i in range(int(countdata)):
        procces = '0x' + numsdata[counter1:counter2]
        strap = xh1[procces]
        a.write(strap)
        counter1 += 3
        counter2 += 3

    print("Decrypting Done!")
    print("Your Decrypted file saved to: " + "decrypted-files/" + str(filename))
    exit()


ifversionok() #Put hashtag here to cancel or bypass the version verification!, example: "#ifversionok()".
mainprocces()
