#!/bin/python

import os
import time
import json


#results, runtime, and logs

#results
class results():
    rlo = '[ load! ]' #loading result
    rok = '[  ok!  ]' #ok result
    rer = '[  er!  ]' #error result
    rgo = '[ good! ]' #googd result
    rba = '[ bad!  ]' #bad result

r = results()

#runtime
def runtime():
    time.sleep(.5)

#making .logs
def makelogs():
    os.system('mkdir ./.logs')

#remove .logs
def removelogs():
    os.system('rm -rf ./.logs')


#all starting run fuctions here!

#runfuc
def runfuc():
    print(f"{r.rlo} Generating logs...")
    runtime()
    try:
        print(f"{r.rgo} makelogs.")
        makelogs()
    except:
        print(f"{r.rba} makelogs.")
        pass

    print(f"{r.rlo} Reading srclist...")
    runtime()
    try:
        print(f"{r.rgo} srclist.")
        readsrc()
    except:
        print(f"{r.rba} srclist.")
        pass
    
    print(f"{r.rlo} Generating list...")
    runtime()
    try:
        print(f"{r.rgo} genlist.")
        genptlist()
    except:
        print(f"{r.rba} genlist.")
        pass

    print(f"{r.rlo} Generating Numbers...")
    runtime()
    try:
        print(f"{r.rgo} numbers.")
        gennum1()
        gennum2()
    except:
        print(f"{r.rba} numbers..")
        pass
    
    print(f"{r.rlo} Generating Dictionary...")
    runtime()
    try:
        print(f"{r.rgo} Dictionary.")
        gendict()
    except:
        print(f"{r.rba} Dictionary.")
        pass

    print(f"{r.rlo} Removing logs...")
    runtime()
    try:
        print(f"{r.rok} logsremoved.")
        removelogs()
    except:
        print(f"{r.rer} logsremvoed.")
        pass


#all src fuctions run here!

#read the text
def readsrc():
    runtime()
    try:
        global text, keys
        text = open('./gendictsrc/printed/text', 'r').read().rstrip('\n')
        keys = open('./gendictsrc/printed/keys', 'r').read().rstrip('\n')
        print(f"{r.rok} readsrc.")
    except:
        print(f"{r.rer} readsrc.")
        pass

#gen ptable list/tuples
def genptlist():
    runtime()
    try:
        count1 = 0
        genptllog = open('./.logs/.genptllog', 'w')
        genptllog.write('(')
        for i in range(len(text)):
            if text[count1] == '\"':
                genptllog.write('\"\\' + str(text[count1]) + '\", ')
            else:
                genptllog.write('\"' + str(text[count1]) + '\", ')

            count1 += 1

        genptllog.write('\"genptllogok\")')
        print(f"{r.rok} genptlist.")
    except:
        print(f"{r.rer} genptlist.")
        pass

#use letter as a numbering
def gennum1():
    runtime()
    try:
        count1, count2 = 0, 0
        gennum1log = open('./.logs/.gennum1log', 'w')
        gennum1log.write('{\n')
        for i in range(len(keys)):
            gennum1log.write('\t\"' + str(count2) + '\":\"' + str(keys[count1]) + '\",\n')

            count1 += 1
            count2 += 1

        gennum1log.write('\t\"gennum1\":\"ok!\"\n}')
        print(f"{r.rok} gennum1.")
    except:
        print(f"{r.rer} gennum1.")
        pass

def gennum2():
    runtime()
    try:
        count1, count2, count3 = 1, 0, 1
        countlimit = 10
        gennum2log = open('./.logs/.gennum2log', 'w')
        gennum2log.write('{\n\t\"0\":\"00",\n')
        for i in range(len(text)):
            if count1 >= countlimit:
                count3 = 0
                count2 += 1
                gennum2log.write('\t\"' + str(count1) + '\":\"' + str(keys[count2]) +  str(keys[count3]) + '\",\n')
                countlimit += 10
            else:
                gennum2log.write('\t\"' + str(count1) + '\":\"' + str(keys[count2]) +  str(keys[count3]) + '\",\n')

            count1 += 1
            count3 += 1

        gennum2log.write('\t\"gennum2\":\"ok!\"\n}')
        print(f"{r.rok} gennum2.")   
    except:
        print(f"{r.rer} gennum2.")
        pass


#making a dictionay form text and keys
def gendict():
    runtime()
    try:
        gennum = json.loads(open('./.logs/.gennum2log', 'r').read())
        count1, count2, = 0, 1
        gendictlog = open('./dictionary/xh1/xh1.json', 'w')
        gendictlog.write('{\n')
        for i in range(len(text)):
            if text[count1] == '\"':
                gendictlog.write('\t\"\\' + str(text[count1]) + '\":\"' + str(gennum[str(count2)]) + '\",\n')
            elif text[count1] == '\\':
                gendictlog.write('\t\"\\' + str(text[count1]) + '\":\"' + str(gennum[str(count2)]) + '\",\n')
            else:
                gendictlog.write('\t\"' + str(text[count1]) + '\":\"' + str(gennum[str(count2)]) + '\",\n')

            count1 += 1
            count2 += 1
        
        gendictlog.write('\t\"xh1\":\"ok\"\n}')
        print(f"{r.rok} gendict.")
    except:
        print(f"{r.rer} gendict.")
        pass


runfuc()
