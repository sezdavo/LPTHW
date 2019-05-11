# print a question folowed by a prompt for the answer
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh", end=' ')
weight = input()
# print a summary of the answers in a string
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
# print a question followed by a prompt for the answer (this time an integer is included)
print("Whats your facourite sport?", end=' ')
sport = input()
print("Whats your dogs name?", end=' ')
dog_name = input()
print("How old is youre dog?", end=' ')
# use int() to convert input into an integer value
dog_age = int(input())
# calculate dogs age from years to dog years
dog_age_dog_years = dog_age * 7
# print a summary of answers in a string
print(f"So you like to play {sport} and your dog, {dog_name}, is {dog_age_dog_years} old in dog years.")
