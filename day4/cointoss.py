# Learning randomness, through pseudo random number generators... for python it is specifically the Mersenne Twister


import random

a = 1
b = 101

random_int = random.randint(a, b)
# print(random_int)

# modules, each module is responsible for a different functionality of the program. first use import then type the file name then you can use the code used in that document.

# random float number

# random_float = random.random()
# print(random_float)

# Coin toss game
# by using a random numbers create a heads or tails game.

# A possible solution could be if a number ends in a whole number then make that = to heads and if it ends in a float then have it = tails, however if there are more floats than ints... perhaps a better solution would be between even numbers and odd numbers.

# num = int (input (“Enter any number to test whether it is odd or even: “) if (num % 2) == 0: print (“The number is even”) else: print (“The provided number is odd”) Output: Enter any number to test whether it is odd or even: 887 887 is odd.

print("Lets flip a coin...")
print('''-=[ quarter ]=-  4/97

            _.-'~~`~~'-._
         .'`  B   E   R  `'.
        / I               T l
      /`       .-'~"-.       `l
     ; L      / `-    \      Y ;
    ;        />  `.  -.|        ;
    |       /_     '-.__)       |
    |        |-  _.' \ |        |
    ;        `~~;     \\        ;
     ;  INGODWE /      \\)P    ;
      \  TRUST '.___.-'`"     /
       `\                   /`
         '._   1 9 9 7   _.'
     jgs    `'-..,,,..-'`
''')

# error was here the use of the . lower
player_choice = str(input("Heads or tails?"))
player_choice.lower
print("Flips Coin!")

coin_toss = random_int % 2

if coin_toss == 0:
    print(random_int)
    winner = str("heads")
    # print("heads!")
else:
    print(random_int)
    winner = str("tails")
    # print("tails!")

chosen_side = player_choice

if chosen_side == winner:
    print(chosen_side)

    print(f"{winner}! you win!")
elif chosen_side != winner:
    print(player_choice)

    print(f"{winner}! you lose... best 2 out of 3?")

# chosen_side = player_choice
# print(f"you chose {chosen_side}")
# print(winner)
# print(player_choice)

# win = bool(winner == player_choice)
# print(f"{win}")


# if the players choice = true then win = true
# if input of heads or tails ==
