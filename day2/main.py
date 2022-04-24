# Tip Calculator Project

# My first tip calculator!

print(input("Welcome to the tip calculator."))
bill = (input("What was the total bill? "))
tip = (input("What percentage tip would you like to give? "))
num_people = (input("how many people to split the bil? "))

tip_math = int(tip) / 100

bill_tip = int(bill) * tip_math

bill_total = int(bill) + bill_tip

bill_split = round(bill_total / int(num_people), 2)

print(bill_split)
