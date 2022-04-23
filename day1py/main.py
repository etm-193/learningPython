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
