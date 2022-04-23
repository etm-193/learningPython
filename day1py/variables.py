# Python Variables

name = input("What is your name?")
print(name)

# Like other programming languages and scripting languages going from top to bottom executing code first we create a variable the variable can be a method or an object:

sayTheName = input("What was your name again?")
length = len(name)
# then these two variables come together like so:
print(length)
#sayTheName variable asks for the input method stored inside then length uses the len command/method to examine the sayTheName variable which = input

# EXERCISE, changing variables without typing them out. What really helped me in this one was the visualization the instructor gave me. One variable holds coffee the other milk, we want to switch the contents how do we go about doing it, well we get an extra container or two.

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
d = b
a = d
b = c
# this could have been done with just a b and c where c = a a = b b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


print("Variable Naming conventions")
print("Rule 1 to separate words we use '_' in python\nRule 2 we can use numbers just not at the begining\nRule 3 (bad practice)Don't use functions as variable names")