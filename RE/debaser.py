import sys, base64, hexdump, textwrap
from itertools import permutations
# 2019-02-16
# pip3 install textwrap hexdump
# Create file full of base64 fragments, each one on a new line
# Usage:
# python3 debaser.py <file>

def getLines():
    with open(sys.argv[1],"r") as f:
        pieces = []
        lines = f.readlines()
        for line in lines:
            #print(line.strip("\n"))
            pieces.append(line.strip("\n"))
    return pieces

linez = getLines()
print("Finding Permutations in {}".format(sys.argv[1]))
print("\033[0;33;40m"+"-"*80+"\033[0m")

perm = permutations(linez, len(linez)) 

for i in list(perm): 
    try:
        ii = ''.join(list(i))
        data = base64.b64decode(ii)
        print("\033[0;32;40m")
        print(" \033[0m\n\033[0;32;40m".join(textwrap.wrap(ii,80)))
        print("\033[0m")
        hexdump.hexdump(data)
        print("\n\033[0;33;40m"+"-"*80+"\033[0m")
    except:
        pass
