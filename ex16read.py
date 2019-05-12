# ask for arguments upon running script
from sys import argv
# unpack arguments
script, filename = argv
# open inputted file and assign to a variable
file = open(filename)
# print the file
print(file.read())
# close the file
file.close()
