# Just learned that the program wont run from separate files like an html. Apparently everything goes through the main.py sheet.

# This will be the band name generator program! (cheat sheet will be a separate file)

# METHOD 1 (way i came up with)

print("Welcome to the Band Generator")


print(input("What city did you grow up in?\n") + " " +
      input("What is the name of your pet\n?"))

# METHOD 2 (solution)

print("Welcome to the Band Generator")

city = input("What city did you grow up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name could be " + city + " " + pet)

# ---------------------------------------------------------------------------------------------- len function
# understanding input
# input("What is your name?!")

# Practical application

# print("Hello " + input("What is your name?!")) this will print a message saying hello to the input name ex: "Hello tito".

# however in order to make this work the only thing that needs to be printed out is the "len()" of the input:
# input("What is your name?!") <-- turns out that was not needed! only the one bellow was! Thats why the program ran two questions before getting the len.
print(len(input("What is your name?!")))

# ------------------------------------------------------------------------------------- string manimpulaiton

print("Hello World")
# This is the iconic first step, by using the comand print ("") we have just printed a string. Now this syntax looks very similar to java. I guess later my hypothesis confirmed or not.

print("")

print("Learning Concatenation")

print("concatenation is created using the the '+' sign")

# print("e.g. print('Hello' + 'world')"\n"New lines can be created with baslash and n" ) this was my first attempt at using this method and i made the mistake of splitting the statement and inserting the command in between two separate statements (which I'm not sure could have even been called separate as there was no coma or other symbol) the correct way is as follows:

print("e.g. print('Hello' + 'world')\nNew lines can be created with baslash and n")

# ----------------------------------------------------------------------------------------- variables
# Python Variables

name = input("What is your name?")
print(name)

# Like other programming languages and scripting languages going from top to bottom executing code first we create a variable the variable can be a method or an object:

sayTheName = input("What was your name again?")
length = len(name)
# then these two variables come together like so:
print(length)
# sayTheName variable asks for the input method stored inside then length uses the len command/method to examine the sayTheName variable which = input

# EXERCISE, changing variables without typing them out. What really helped me in this one was the visualization the instructor gave me. One variable holds coffee the other milk, we want to switch the contents how do we go about doing it, well we get an extra container or two.

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

c = a
d = b
a = d
b = c
# this could have been done with just a b and c where c = a a = b b = c

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


print("Variable Naming conventions")
print("Rule 1 to separate words we use '_' in python\nRule 2 we can use numbers just not at the begining\nRule 3 (bad practice)Don't use functions as variable names")
