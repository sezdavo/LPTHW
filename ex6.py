# defining number of people
types_of_people = 10
# assinging a formatted string to a new variable
x = f"There are {types_of_people} types of people"
# creating two new variables
binary = "binary"
do_not = "don't"
# assigning a formatted string to a new variable
y = f"Those who know {binary} and those who {do_not}."
# printing the variables that have formatted strings assigned to them
print(x)
print(y)
# printing new formatted strings with formatted strings embedded into them
print(f"I said: {x}")
print(f"I also said: '{y}'")
# creating variable with boolean value
hilarious = False
# assigning a variable with an EMPTY formatted string
joke_evaluation = "Isn't that joke so funny?! {}"
# printing empty formatted string with a variable inserted into it
print(joke_evaluation.format(hilarious))
# creating two new variables with strings assigned to them
w = "This is the left side of..."
e = "a string with a right side."
# printing those variables next to eachother
print(w + e)
