# BMI Calculator 2.0
from unittest import result


print("Welcome to the BMI Calculator 2.0")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight_kgs = float(weight)

height_meters = float(height)

bmi = weight_kgs / height_meters ** 2

results = round(float(bmi), 2)

# print(results)

if results < 18.5:
    print(f"Your BMI is {results}, you are underweight.")
elif results <= 25:
    print(f"Your BMI is {results}, you have a normal weight.")
elif results <= 30:
    print(f"Your BMI is {results}, you are slightly overweight.")
elif results <= 35:
    print(f"Your BMI is {results}, you are obese.")
else:
    print(f"Your BMI is {results}, you are clinically obese.")

    # worked like a charm, except that my code repeated the results and the testing app didn't like that :,) thats why there is code commented out. In any case I still could not determine where to use % ...
