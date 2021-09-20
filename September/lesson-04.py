# Functions are code that you can run multiple times

# defining a function
def say_hello():
    print("hello")
# Calling the function:
say_hello()

# The point of functions in big programs is that you don't have to repeat code that appears in multiple places (that can't be done in a loop)
# Just for those interested, DRY is an acronym for a design philosophy where you do NOT repeat yourself as little or not at all

# returning a value
# use the return keyword to give back a value that you can pass to either a variable or another function
def get_three():
    return 3

x = get_three()
print(x)

# taking in a value
# You can define parameters to your functions, these are variables that you can pass to a function
def add_one(x):
    return x + 1

print(add_one(1))

# you can take in multiple paramters
def add_two_numbers(a, b):
    return a + b

# Google CodingBat and set the site to python
# Grind out the problems until you hit a question where you need help