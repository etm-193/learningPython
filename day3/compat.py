# People compatability program

# In this leason we explore Logical operators "and" "or" & "not" ture = A AND B need to be true, true = C OR D, only one needs to be true

# the lower function reduces all characters in a string to lower case

# the count function .count("character in here")

# (Instructor explanation count the number of times the words true and then love happen in both of your names)  Count the number of times the letters in a name happen in the words true and then love, flow logic: name1 converted to lower case then compare num of characters between name1 and true and then love. then repeat process for name2, add the results for name1 and name2 true and the same for love, then print each number separately and that is your percentage.
    # step 1 get variables and convert to lower case
    # step 2 count / compare the characters of the word true and then love
    # step 3 add a variable with the math  for each word.
    # step 3.5 use an f"to add the two results as a string!" the point is to concactinate them together.
    # step 4 prep the logic and the print statements

# 🚨 Don't change the code below 👇
from ast import Or


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
lower_case = combined_string.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"your score is {love_score}.")



