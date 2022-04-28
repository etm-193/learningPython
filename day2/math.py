# Mathematical operators

from __future__ import division
from doctest import Example
from tokenize import Floatnumber


addition = 3 + 2
subtraction = 5 - 1
multiplication = 9 * 2
division = 4 / 2
exponent = 2 ** 2


# like manual math there are rules as to the order of math : pemdas -   PARENTHESIS, exponent, multiplication and division, addition and subtraction:

Example = 3 * 3 + 3 / 3 - 3

# left to right thats the way to go (program to see code execute step by step is called thony)

# Rounding numbers

print(8 / 3)

# chop off the end ... not rounding

print(int(8 / 3))

# presicion rounding = use a coma to indicate to what decimal digit to round to
print(round(8 / 3, 2))

# floor division // this will result an int
print(type(8 // 3))

# F strings is a way to use multiple datatypes without having to convert  by doing the following
score = 0
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}") 

# and now all the conversions are done in the background!!!!! YAy