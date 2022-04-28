# Leap year or not?

# 🚨 Don't change the code below 👇
from operator import truediv


year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print("Leap Year")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not Leap year.")
    
# if year_math1 = True:
#     print(f"{year} is a leap year")
#     elif year_math2



