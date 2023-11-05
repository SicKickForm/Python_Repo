import os

# File handling
if os.path.exists("Control/Notes.txt"):
    file = open("Control/Notes.txt", "wt")
else:
    file = open("Control/Notes.txt","xt") 
file.write("x mode: Create the file / Return an error if the file exists\n")
file.write("w mode: Overwrite the file context / Create the file if it does not exist\n")
file.write("a mode: Append the file context / Create the file if it does not exist\n")
file.write("r mode: Read the file context (default)\n")
file.write("Use t extension for text mode (default) and b extension for binary mode\n")
file.write("Use .read(Num) to read certain amount of characters and .readline() to read one line\n")
file = open("Control/Notes.txt")
print(file.read())
file.close()