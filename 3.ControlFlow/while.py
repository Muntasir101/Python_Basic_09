age = int(input("Enter your age: "))
name = input("Enter your name: ")

while age <= 25 or False:
    if name == 'test':
        print(str(age) + " Hello " + str(name))
    else:
        print(str(age) + " None")
    age += 1


# Test case 1: 30, test