# creating a base string to be formatted
formatter = "{} {} {} {}"
# printing base string with different arguments using format function
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Hello",
    "How are you",
    "doing on this",
    "fine evening",
))
