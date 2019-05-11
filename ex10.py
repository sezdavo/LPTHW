# create string that uses \t to tab in the strings
tabby_cat = "\tI'm tabbed in."
# create a string that uses \n to start a new lines
persian_cat = "I'm split\non a line."
# create a string that uses \\ to write a false \
backslash_cat = "I'm \\ a \\ cat."
# create a string that uses ''' to write unlimited lines
# and also uses a combination of \n and \t to make a list structure
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# print results
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
# create a formatter with \n and \t to change structure
formatter = "{} \n\t{} \n\t\t {} {}"
# use format function to insert variables into formatter
print(formatter.format(fat_cat, persian_cat, backslash_cat, tabby_cat))
