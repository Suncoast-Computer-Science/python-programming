# if statement review
# Take in a name and a boolean (use the bool() function)
# Say if the boolean is true greet the user
# Otherwise do nothing
# name = input()
# greet_user = bool(input())
# if greet_user:
#   print("Hello " + name)

# Take a number, and print if that number is even or not
# number = int(input())
# if number % 2 == 0:
#   print("even")
# else:
#   print("odd")
# fancy syntax version:
# print("even" if int(input()) % 2 == 0 else "odd")

# Make a for loop that will print the numbers 10 to 1 
# Hint: subtraction
# for i in range(10):
    # print(10-i)

# take a number, if it is divisible by 2 and 7, print True, it not divisible by both print false
# number = input()
# print(number % 2 == 0 and number % 7 == 0)
# OR
# number = input()
# if number % 2 == 0 and number % 7 == 0:
#   print(True)
# else:
#   print(False)

# FIZZBUZZ:
# Print number 0 to 100
# if the number is divisible by 3 print fizz
# if the number is divisible by 5 print buzz
# if the number is divisible by 3 and 5 print fizzbuzz
# if the number is NOT divisible by 3 or 5, print the number
# Sample Output 
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz

# The way I expect you to do it
# for i in range(101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print('fizz')
#     elif i % 5 == 0:
#         print('buzz')
#     else:
#         print(i)

# For loop ranges
# print numbers from 1 to 20, 
# for i in range(1, 20):
#     print(i)
# print numbers from 1 to 100, but every other number
# for i in range(1, 100, 2):
#     print(i)
# print numbers from 1 to 10, but increment by .5 
# for i in range(1, 10, .5):
#     print(i)
# Challenge: print numbers from 100 to 1
# for i in range(100, 1, -1):
#     print(i)

# Lists:
# Lists are our first Data Structure 
# Lists are a changeoble, ordered sequence of items
# These items can be any other data type, including other data structures (i.e. other lists)
# Java kids might know this as ArrayLists

# empty list 
# my_list = []

# list with items in it
# my_list = [1, 2, "fizzbuzz", True, 3.4]

# Accessing an item in a list uses the index of that position (lists start at 0)
# print(my_list[2])
# This will print "fizzbuzz" as fizzbuzz is in position 2 (despite being the third item in the list)

# use len() when getting length of a list
# len(my_list)
# will print 5 

# write a program that will take a number and print the element at that position in my_list 
# print(my_list[int(input())])

# we can use this length to get the last element
# noticing that the last position will be the size of the list - 1 allows us to grab the last position of any list without knowing the size first
# print(my_list[len(my_list) - 1])
# this is how java kids do it, but we're cooler than them we don't need to do all that
# it is important to realize how that works though

# We can actually get a certain position from the end of the list instead of the left, meaning we can go x numbers from the end than the beginning
# print(my_list[-1]) # gives us the last item
# print(my_list[-2]) # gives us the second last item
# if for whatever reason you want to grab the first item from the left in the reverse order you can also do that too!
# print(my_list[-len(my_list)])

# use .append() Adding to a list DOES NOT USE += or +
# Those two have other uses which we will NOT cover but feel free to google
# my_list.append(5)
# we will talk about deleting items later, but tldr you just don't do it lmao

# Challenge:
# Take a number. Use a for loop to run that number of times, taking input each time and adding that input to the list
# And then print the list
# Input:
# 3
# bruh
# bruhbruh
# br
# Output:
# ["bruh", "bruhbruh", "br"]

# my_list = []
# for i in range(int(input())):
#     my_list.append(input())
# print(my_list)
# Slicing a list
# my_sublist = my_list[1:3]
# print(my_sublist, my_list)

# Challenge:
# Add to your code from before, after printing the list
# But now you will take in two numbers, a and b (assume a < b)
# print the list from position a to b (including elements a but not b)
# a = int(input())
# b = int(input())
# print(my_list[a:b])

# You can use the range operator values to get a subarray
# You can use get the reverse of a list by using -1
# my_sublist = my_list[3:1:-1]
# print(my_sublist)

# Challenge pt 2
# Now assume a MAY BE GREATER THAN b, but doesn't have to
# in that case you will print the list in reverse from a to b (including a but not b)
# assume that a != b

# if a < b:
    # print(my_list[a:b])
# else:
    # print(my_list[a:b:-1])

# Strings are just a list of characters and we can index it just like a list
# You can use len() on strings 
# len("bruh") # gives four

# You can get the indexes of a string just like any other list
# my_str = "bruh"
# my_list = ["b", "r", "u", "h"]
# print(my_str[2])
# print(my_str[2])

# You can also get slices of a string like you would with a list
# challenge: print just "br" using my_str
# print(my_str[0:2])

# That's it!
