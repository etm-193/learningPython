import random
a = 1
b = 101

random_int = random.randint(a, b)

print("lets flip a coin...")

player_choice = str(input("Heads or tails?"))
player_choice.lower
print("Flips Coin!")

coin_toss = random_int % 2

if coin_toss == 0 :
  print(random_int)
  winner = str("heads")
  # print("heads!")
else :
  print(random_int)
  winner = str("tails")
  # print("tails!")

chosen_side = player_choice

if chosen_side == winner :
  print(chosen_side)
  
  print(f"{winner}! you win!")
elif chosen_side == winner :
  print(player_choice)
  
  print(f"{winner}! you lose... best 2 out of 3?")

