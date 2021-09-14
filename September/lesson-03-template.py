## TEMPLATE: Has all the text and descriptions you'll need 
## Copy along with my code and this will serve as a pretty decent reference for later

# if statement review
# Take in a name and a boolean (use the bool() function)
# Say if the boolean is true greet the user
# Otherwise do nothing


# Take a number, and print if that number is even or not

# fancy syntax version:


# Make a for loop that will print the numbers 10 to 1 
# Hint: subtraction

# take a number, if it is divisible by 2 and 7, print True, it not divisible by both print false

# OR

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

# For loop ranges
# print numbers from 1 to 20, 

# print numbers from 1 to 100, but every other number

# print numbers from 1 to 10, but increment by .5 

# Challenge: print numbers from 100 to 1

# Lists:
# Lists are our first Data Structure 
# Lists are a changeoble, ordered sequence of items
# These items can be any other data type, including other data structures (i.e. other lists)
# Java kids might know this as ArrayLists

# empty list 

# list with items in it

# Accessing an item in a list uses the index of that position (lists start at 0)
# This will print "fizzbuzz" as fizzbuzz is in position 2 (despite being the third item in the list)

# use len() when getting length of a list
# will print 5 

# write a program that will take a number and print the element at that position in my_list 

# we can use this length to get the last element
# noticing that the last position will be the size of the list - 1 allows us to grab the last position of any list without knowing the size first

# this is how java kids do it, but we're cooler than them we don't need to do all that
# it is important to realize how that works though

# We can actually get a certain position from the end of the list instead of the left, meaning we can go x numbers from the end than the beginning

# if for whatever reason you want to grab the first item from the left in the reverse order you can also do that too!

# use .append() Adding to a list DOES NOT USE += or +
# Those two have other uses which we will NOT cover but feel free to google

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

# Slicing a list

# Challenge:
# Add to your code from before, after printing the list
# But now you will take in two numbers, a and b (assume a < b)
# print the list from position a to b (including elements a but not b)

# You can use the range operator values to get a subarray
# You can use get the reverse of a list by using -1

# Challenge pt 2
# Now assume a MAY BE GREATER THAN b, but doesn't have to
# in that case you will print the list in reverse from a to b (including a but not b)
# assume that a != b


# Strings are just a list of characters and we can index it just like a list
# You can use len() on strings 

# You can get the indexes of a string just like any other list

# You can also get slices of a string like you would with a list
# challenge: print just "br" using my_str

# That's it!