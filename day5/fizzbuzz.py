# fizzbuzz

total = 0

for number in range(1, 101):
    if number % 3 != 0 and number % 5 != 0: 
        print(number)
    elif number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0 :
        print("buzz")
    elif  number % 3 == 0 :
        print("fizz")


# took me a while because first i messed up on the syntax structure for modulo and after i forgot that if the if statement = true then it stops there and doesn't check the if the other statements are true. So I moved the order of the statement.

# course solution:

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)