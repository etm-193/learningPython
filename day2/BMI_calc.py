# BMI calculator

# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight. The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Meters to feet : for an approximate result, multiply the length value by 3.281  so... to get the inverse divide?

print("Welcome to the BMI Calculator")

height = input("Enter your height in Feet: ")

height_feet = float(height)

height_meters = height_feet / 3.281

print(height_meters) 

weight = input("Enter your weight in Lbs: ")

# for an approximate result, divide the mass value by 2.205

weight_kgs = int(weight) / 2.205

print(weight_kgs)

bmi = weight_kgs / height_meters ** 2

results = str(bmi)

print("Your Body mass indicator is: " + results)

