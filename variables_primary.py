# author: <Lyric Marner>
# date: <July 2, 2021>
#
# description: <fill in>

# --------------- Section 1 --------------- #

# 1.1 | Variable Creation | Strings
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Create a variable that holds your name.
#   2) Create a variable that holds your birthday.
#   3) Create a variable that holds the name of an animal you like.
#
# Print
#   4) Print each variable, describing it when you print it.
#
# Example Code
example_name = 'elia'
#print('EXAMPLE: my name is', example_name)

# WRITE CODE BELOW
my_name = 'Lyric'
my_birthday = 'September 12, 2006'
animal = 'panda'

print('My name is', my_name)
print('My birthday is', my_birthday)
print('A', animal, 'is cute animal that I like')
print()
# 1.2 | Variable Creation | Integers / Floats
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# All variables created in this section should hold either an integer or float.
#
# Variables
#   1) Create a variable that holds your favorite number.
#   2) Create a variable that holds the day of the month of your birthday.
#   3) Create a variable that holds a negative number.
#   4) Create a variable that holds a floating (decimal) point number.
#
# Print
#   5) Print each variable, describing the value you print.

# WRITE CODE BELOW
fav_num = '1'
birth_day = '12'
neg_num = '-6'
dec_num = '18.3'

print('My favorite number is', fav_num)
print('The day of the month of my birthday is cool, it\'s', birth_day)
print('A negative number is a number below zero, like', neg_num)
print('A float is a decimal point number, an example of one would be', dec_num)
print()
# 1.3 | Overwriting Variables
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Overwrite the variable holding your name, and save a different name to it.
#   2) Overwrite the variable holding birthday with the day you think would be best to have a birthday on.
#   3) Overwrite the variable holding your favorite number and set it to a number you think is unlucky.
#
# Print
#   4) Print the variables you've overwritten, describing the values you print.
#
# Example Code
#example_name = 'lucia'
#print('EXAMPLE: my new name is', example_name)

# WRITE CODE BELOW
my_name = 'Imani'
my_birthday = 'December 24th, 2006'
fav_num = '8' 

print('My new name is', my_name)
print('I think the best birthday would be', my_birthday)
print('An unlucky number might possibly be', fav_num)
print()
# 1.4 | Operations
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Create a variable that is the sum of two numbers.
#   2) Create a variable that is the product of three numbers.
#   3) Create a variable by dividing the previously created sum, with the previously created product.
#
#   4) Create a variable that is the concatenation of your name and an animal you like (use the variables!)
#   5) Create a variable that is an acronym (like 'lol') multiplied by your birth day.
#
#   6) Create a variable that is difference of itself minus the number you think is unlucky.
#   7) Overwrite the lucky variable with the itself squared.
#
# Print
#   7) Print all the new variables you've created along with what the represent
#
# Example Code
example_sum = 11 + 21
#print('EXAMPLE: the sum of 11 and 21 is', example_sum)

# WRITE CODE BELOW
num1 = 10+10
num2 = 3 * 3 * 2
num3 = 20/18
num4 = 'lyric' + 'panda'
num5 = 'ttyl' * 12
num6 =  7 - 7 - 8
num7 = 1**2
print('The sum of 10 and 10 is', num1)
print('The product of 3 times 3 times 2 is', num2)
print('20 divided by 18 is', num3)
print('My name combined with an animal I like, in this case a panda, looks like', num4)
print('If you duplicate ttyl 12 times it looks like', num5)
print('7 minus 7 minus 8 is', num6)
print('1 squared is', num7)