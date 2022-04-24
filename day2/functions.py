# Understanding Functions

# think a machine that turns potatoes as fries if you put something other than poatoes it will come back as an error... ex len(1234) = type_error

from cmath import log


num_char = len(input("What is your name?"))

# type conversion or casting

print(type(len(input("What is your name?"))))

new_num_char = str(num_char)

print = ("Your name has " + new_num_char + " characters.")

# javaScript has slightly different syntax but the theory and application behind it is the same.


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(type(two_digit_number))

digit_one = two_digit_number[0]

digit_two = two_digit_number[1]


new_digit_1 = int(digit_one)
new_digit_2 = int(digit_two)

output = new_digit_1 + new_digit_2

print(output)


# Took me a while to understand this exercise because i was trying to use the len command along with the int, in other words i was trying to skip a step apparently because i was casting at the same time i was getting the len this resulted in the digit being = 1 always. It was essential to understand that gathering the digit you want as a string using the variable[] first and then casing as a new variable = int(variableOld) to acheive this i should have done as such: digit_one = int(two_digit_number[0])