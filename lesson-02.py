# String review
# my_string = "Hello "
# my_other_string = "World"
# my_final_string = my_string + my_other_string

# Input review
# my_string = "Hello "
# my_other_string = input()
# my_final_string = my_string + my_other_string

# Warm up:

# Input 3 numbers, label them a, b, and c
# print the sum or a and b

# If statement
# if True:
#     print(True)
# else:
#     print(False)


# boolean reivew
# my_bool = (a >= a) # my_bool = a >= a is valid too, but I prefer using parentheticals

# if statements
# if my_bool:
#     print(True)
# a = 1
# b = 2
# if a >= b:
#     print(True)
# else:
#     print(False)

# Questions:
# Take in 2 numbers, print out the greater number
# Numbers will not equal each other

# Take in 2 numbers, print out the smallest number
# If one of the numbers is 0 print bazinga!

# Take in 2 numbers, print "yes" if the difference of the two numbers is 2 and "no" if that is not the case


# Take in two numbers. If a is greater than b print "greater", if equal print "equal" or print print less
# a = 1
# b = 2
# if a > b:
#     print("greater")
# elif a == b:
#     print("equal")
# else:
#     print("lesser")

# find the issue with this code
# number = 101
# if number > 50:
#     print("number is greater than 50 but not greater than 100")
# elif number > 100:
#     print("number is greater than 100")
# else:
#     print("number is not greater than 50 or 100")

# For loops
# for i in range(100):
#     print(i)

# NOTE: i is a VARIABLE, but don't change it inside your loop. That's bad news
# for i in range(100):
#   a = i + 1
#   print(i)

# Example:
# Print a 10, but with x amount of zeros
# i.e. print 10 but with 3 zeroes
output = 1
power = int(input())
for i in range(power):
  output *= 10
print(output)
