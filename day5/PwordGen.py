# PyPassword Generator

# Details:
    # In this project the user inputs the len of the password, the qty of symbols, the qty of numbers and then the program generates a random combination of characters numbers and symbols.
    # step zero import random
    # step two prep the variables and inputs
    # step three create a list of characters both upper and lower case
    # step four create a list of symbols
    # step five random int logic
    # step six create selection logic
    # Last step concactinate the results

# Imports
import random
# imported from https://replit.com/@appbrewery/password-generator-start#main.py
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassWord Generator!")

# user input:

password_len = input("How many letters would you like in your password?\n")
password_len = int(password_len)

symbol_num = input("How many symbols would you like?\n")
symbol_num = int(symbol_num)
number_num = input("how many numbers would you like?\n")
number_num = int(number_num)

length = password_len
qty_sym = symbol_num
qty_num = number_num


# print(len(letters))= 52 chars
random_letter = letters[random.randint(0, 51)]
random_num = numbers[random.randint(0,8)]
random_symbol = symbols[random.randint(0, 8)]
# print(random_letter)



# program logic:




