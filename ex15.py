# receiving a filename from the user upon running the program
##from sys import argv
# unpacking the arguments received
##script, filename = argv
# opening the file inputted at the start and assigning it to a variable
##txt = open(filename)
# printing a sentence followed by the file from the start
##print(f"Here's your file {filename}:")
##print(txt.read())
# printing a sentence followed by prompting the user to input the filename
print("Type the file name again:")
file_again = input("> ")
# assigning the file inputted to a variable
txt_again = open(file_again)
# printing the contents of the file again
print(txt_again.read())
# close file
txt_again.close()
