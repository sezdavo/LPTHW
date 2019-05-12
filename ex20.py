# get args from user
from sys import argv
# unpack args
script, input_file = argv
# define function that prints an entire text file
def print_all(f):
    print(f.read())
# define a function that resets the state of a file back to 0
def rewind(f):
    f.seek(0)
# define a function that reads a single line and then prints it
def print_a_line(line_count, f):
    print(line_count, f.readline())
# open file inputted at start of program
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) # current_line = 1

current_line += 1
print_a_line(current_line, current_file) # current_line = 2

current_line += 1
print_a_line(current_line, current_file) # current_line = 3
