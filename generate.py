import os

os.system('rm -rf src/xh1/xh1.txt && rm -rf src/xh1/xh1var.txt')

alphalo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaup = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
spechar = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/', ' ']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]


x = 0
with open('src/xh1/xh1.txt', 'w') as f:
    for i in alphalo + alphaup + numbers + spechar:
        x += 1
        if x > 9:
            f.write("0x" + str(x) + " = " + i)
            f.write('\n')
        else:
            f.write("0x" + str(0) + str(x) + " = " + i)
            f.write('\n')


x = 0
with open('src/xh1/xh1var.txt', 'w') as f:
    for i in alphalo + alphaup:
        x += 1
        if x > 9:
            f.write("\'" + i + "\'" + " = " + "0x" + str(x))
            f.write('\n')
        else:
            f.write("\'" + i + "\'" + " = " + "0x" + str(0) + str(x))
            f.write('\n')
