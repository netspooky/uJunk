# importsort

This is a tool that I use to group imports from Windows binaries. 
Sometimes, you have a gigantic folder full of executables, and you want to figure out what you should look at first. 
importsort will iterate over all of the files in a directory, and create a list containing the DLL name, the function imported, and the file that imported that function. 
You can use it to analyze possible behavior, such as network functionality or registry key manipulation etc. 

It uses radare2's `rabin2` tool, but you can also use rizin's `rz-bin`. 
Make sure you have either tool installed, and the `rToolPath` variable in the script is pointing to the correct binary. 
No special libraries are used, it just calls either tool with the `-j` flag for json output using subprocess, and iterates that way. 

## Usage

Parse a whole directory
```
python3 importsort.py -d someDirectory/
```

Parse a whole directory and output json
```
python3 importsort.py -d someDirectory/ -j
```
