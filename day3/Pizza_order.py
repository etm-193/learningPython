# Python Pizza delivery

# In this exercise I need to build a program with the following requirements. 
# 1- take user input for an order
# 2- calculate the price based on the order

# 🚨 Don't change the code below 👇
from ast import And


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


order = 0

# the logic should work as in the following way:
# if size = small then(which = :) ASSIGN to a VARIABLE (order) pizza size 

if size == "S":
    order += 15
elif size =="M":
    order += 20
else :
    order += 25

if add_pepperoni == "Y":
    if size == "S":
        order += 2
    else :
        order += 3
if extra_cheese == "Y":
    order += 1

print(f"Your final bill is ${order}")
