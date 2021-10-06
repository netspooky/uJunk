import fnmatch
import os
import subprocess
import json
import argparse
import sys

rToolPath = "/usr/bin/rabin2" # Change if this is different. Can use both rabin2 and rz-bin
importDict = {} # The import dict, 
outLines   = [] # for the final sort

parser = argparse.ArgumentParser(description='importsort - Sort imports from a directory of executable files')
parser.add_argument('-d', dest='directory', help='Directory to parse', required=True)
parser.add_argument('-j', dest='jsonOut', help='Output all data as JSON', action='store_true')
parser.set_defaults(jsonOut=False)
args = parser.parse_args()

def rGlob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        goodfiles = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in goodfiles)
    return results

def getImports(filename):
    process = subprocess.run(['{} -j -i "{}"'.format(rToolPath,filename)], 
                           shell=True, check=True, stdout=subprocess.PIPE, 
                           universal_newlines=True)
    output = json.loads(process.stdout)
    return output

def processImports(filej):
    for i in range(0,len(filej["imports"])):
        libName = filej["imports"][i]["libname"]
        fncName = filej["imports"][i]["name"]
        if libName not in importDict:
            importDict[libName] = []
        importDict[libName].append((fncName,infile))

if __name__ == '__main__':
    directory = args.directory
    dirlist = rGlob(directory,"*")
    sys.stderr.write("Parsing files in directory...\n")
    for infile in dirlist:
        outj = getImports(infile)
        if ( len(outj["imports"]) > 0 ) and ( "libname" in outj["imports"][0] ):
            sys.stderr.write("[+] {}\n".format(infile))
            processImports(outj)
        else:
            sys.stderr.write("[-] {}\n".format(infile))
            continue
    if args.jsonOut:
        print(json.dumps(importDict))
    else:
        for k in sorted(importDict.keys(), key=lambda x:x.lower()):
            for x in range(0,len(importDict[k])):
                outLines.append("{}\t{}\t{}".format(k,importDict[k][x][0],importDict[k][x][1]))
        print("\nDLL Name\tExported Function\tExecutable")
        print("--------------------------------------------------")
        for l in sorted(outLines):
            print(l)
