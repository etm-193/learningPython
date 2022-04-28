# Coin Toss Program v1.2

# First version had all the concepts and notes used to build the program. This version cleans up the code for better readability.

import random

a = 1
b = 101

random_int = random.randint(a, b)

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

player_choice = str(input("Heads or tails?"))
player_choice.lower
print("Flips Coin!")

coin_toss = random_int % 2

if coin_toss == 0:
    
    winner = str("heads")
    
else:
    
    winner = str("tails")
    

chosen_side = player_choice

if chosen_side == winner:
    

    print(f"{winner}! you win!")

elif chosen_side != winner:

    print(f"{winner}! you lose... best 2 out of 3?")

