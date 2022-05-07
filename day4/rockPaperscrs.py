# rock paper scissors game

# Rock beats scissors, scissors beats paper, and paper beats rock and then draws.

# The program needs to create a random selection between the 3 options vs the input that the player provides.
# The program then needs to compare the selections and print the results.
import random


print("Lets play Rock Paper Scissors!")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# My train of thought... I have a list of choices and the player inputs their selection which comes from the list. However, the choice input that comes as a string needs to trigger the aci art.  In other words I only need the variables to call the image.
# step 1 player input - needs to be a number and the number needs to call the art
# step 2 computer choice
# step 3 compare choices
# step 4 print out results


choices = [rock, paper, scissors]

player_choice = input(
    "What do you choose? Input 0 for rock, 1 for paper, 2 for scissors.\n")

choice = int(player_choice)

if choice >= 3 or choice < 0 :
    print("You typed an invalid number, you lose!")
else:

    computer_choice = random.randint(0, 2)

    player_selection = choices[choice]
    
    computer_selection = choices[computer_choice]
    print(player_selection)
    print("The computer chose:")
    print(computer_selection)

    rock = int(0)
    paper = int(1)
    scissors = int(2)

    rock_win = rock < scissors
    paper_win = paper > rock
    scissors_win = scissors > paper

    if choice == rock and computer_choice == scissors:  # player chose rock vs sc  rock wins
        print("You chose rock, rock beats scissors!")
    elif computer_choice == rock and choice == scissors:  # computer chose rock vs sc rock wins
        print("Rock beats scissors, you loose!")
    elif choice == paper and computer_choice == rock:  # player chose paper vs rock paper wins
        print("Paper beats rock!")
    elif choice == paper and computer_choice == scissors:  # player chose paper vs sc paper loses
        print("Scissors beat paper, you lose.")
    elif choice == scissors and computer_choice == paper:  # player chose sc vs paper
        print("Scissors beat paper, you win")
    elif choice == computer_choice:
        print("Its a draw!")


# course solution

# was almost exactly the same as my code! very few differences. one was the statement to catch invalid choices