def sing_happy_birthday(name):
    print("Happy Birthday To You!")
    print("Happy Birthday To You!")
    print(f"Happy Birthday Dear {name}!")
    print("Happy Birthday To You!")


print(sing_happy_birthday("Ravi"))
print(sing_happy_birthday("Jito"))
print(sing_happy_birthday("Gurnam"))


def make_noise():
    print("THE CROWD GOES WILD")


make_noise()


def square_of_9():
    return 9**2


result = square_of_9()
print(result)


def squared(num):
    return num**2


print(squared(5))
print(squared(25))
print(squared(101))


def add(a, b):
    return a+b


print(add(3, 5))
print(add(13, 15))
print(add(23, 25))

# documenting functions using triple double quotes


def say_hello():
    """ A simple function that returns the string hello"""
    return "Hello!"


say_hello.__doc__  # ' A simple function that returns the string hello'
