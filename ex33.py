numbers = []
numbers2 = []
numbers3 = []

limit1 = int(input("Write 1st desired upper limit here: "))
limit2 = int(input("Write 2nd desired upper limit here: "))
limit3 = int(input("Write 3rd desired upper limit here: "))

def make_list_for(limit, list):

    for val in range(0, limit):
        list.append(val)
        print(f" Val is {val}")

def make_list_while(limit, list):

    val = 0

    while val < limit:
        print(f"At the top val is {val}")
        list.append(val)

        val += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom val is {val}")

def print_list(numbers):
    print ("The numbers: ")

    for num in numbers:
        print(num)

make_list_for(limit1, numbers)
print_list(numbers)

make_list_for(limit2, numbers2)
print_list(numbers2)

make_list_for(limit3, numbers3)
print_list(numbers3)
