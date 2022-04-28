# conditional statements look as =   if condition: do this else: do this (similar or same as java)

water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster!")

    # Comparison Operators are what we use in these conditional statements greater than >, < Less than, Greater than or equal to >=, less than or equal to <=, == equal to, != not equal to *one = you are assigning the value.

    # 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number!")
else:
    print("This is an odd number!")


# nested if /else

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    elif age >= 45 and  age <= 55:
        print("Have a free ride on us!")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster!")
