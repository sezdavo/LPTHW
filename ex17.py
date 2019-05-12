# getting arguments from user
from sys import argv
# importing exists function for later use
from os.path import exists
# unpacking arguments
script, from_file, to_file = argv
# printing what file is being copied to what
##print(f"Copying from {from_file} to {to_file}")

# opening file being copied and assigning it to a variable
# in_file = open(from_file)
# creating variable that reads the file
indata = open(from_file).read()
# printing length of file
##print(f"The input file is {len(indata)} bytes long")
# Saying whether the file exists
##print(f"Does the output file exist? {exists(to_file)}")
##print("Ready, hit RETURN to continue, CTRL-C to abort.")
# asking for input from user to go ahead with copy
##input()
# opening new file in 'write' mode
out_file = open(to_file, 'w')
# writing the contents of the initial file to the new file
out_file.write(indata)

##print("Alright, all done.")
# closing both files
out_file.close()
# in_file.close()
