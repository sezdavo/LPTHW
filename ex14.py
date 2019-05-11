from sys import argv

script, user_name, code_level = argv
prompt = 'INSERT ANSWER HERE: '

print(f"Hi {user_name}, I'm the {script} script. So youre a {code_level}?")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright {user_name}, so you said {likes} about likeing me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer and are a {code_level} at coding. Nice.
""")
