# take arguments from user uoon starting script
from sys import argv
# unpack arguments provided by user
script, filename = argv
# print some sentences
print(f"We're going to erase {filename}.")
print("If you dont want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# prmopt the user to answer the above questions
input("?")
# open the file in 'write' mode and assign it to variable
print("Opening the file...")
target = open(filename, 'w')
# empty the file (not actaully necessary for 'write' mode )
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
# ask user to input 3 strings to be written onto file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# write the three lines onto the file, starting a new line each time
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
format = "{}\n{}\n{}"
target.write(format.format(line1, line2, line3))
# close file
print("And finally, we close it.")
target.close()
