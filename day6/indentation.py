# Indentation

from shutil import move


def my_function():
    print("hello")
print("world")
# Think of the indentation as the folder structure ex: def my function is the folder, print hello is part of the folder print world is outside the folder therefor if I try to call the function because print world is outside the folder.


# use spaces when in doubt = space 4 times

# The difference between the while loop and the for loop:  
# For item in list_of_each_item:
    # Do something to each item
# for number in range(a, b):
    # print("yda")
# while something_is_true
    # do something repeteadly

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

def jump():
    move()
    turn_left()
    move()
    turn_right
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    jump()

# or

while not at goal():
    jump



# for loops are good when you want to itterate something for multiple items

# first attempt to try and create a program that clears any and all obstacles that they place within reeborgs world challenges.

def find_goal():
    while not at goal():
        if World() == no_highlight():
            turn_left()
        else:
            if not wall_in_front():
                move()
            elif wall_in_front() and wall_on_right():
                turn_left()
                move()
            elif wall_in_front():
                if right_is_clear():
                    turn_right()
                    move()
                else:
                    turn_left()
                    move()
            elif front_is_clear() == True:
                move()

def jump_to_goal():
    while at_goal() != True :
        if wall_on_right() == True :
            move()
        elif wall_in_front() == True and wall_on_right() == True :
                turn_left()
                move()
                if front_is_clear() == True and right_is_clear() == True :
                    turn_right()
                    move()

def around():
    times_around = 0
    if World(1, 1) and times_around == 0:
        move()
        times_around += 1
        if wall_in_front() == True :
            turn_left()
        else:
            turn_right()
    else:
        done()  
# problem with internal javascript in the website trying something different...

# The Problem:  I lack a goal within the world, and I do not know how it is internaly defined.

# How do I define that the possition where Reborg is at is the starting point and then determine that it is the end?

# I could use a for loop with a range to define the number of steps or "move()" Rebo needs. Or I could try and use a variable to define the number of rounds however, this still leaves the matter of the starting point...

position = 1
times_around = 0

while times_around < 1 :
    if wall_in_front() == True :
        turn_left()
    elif front_is_clear() == True :
        move()
        if wall_in_front() == True and right_is_clear() == True :
            done()

                
           

# number = 0

# while number <= 10 :
#     number += 1
#     print(number)

# while True:
#     # main program
#     while True:
#         answer = str(input('Run again? (y/n): '))
#         if answer in ('y', 'n'):
#             break
#         print("invalid input.")
#     if answer == 'y':
#         continue
#     else:
#         print("Goodbye")
#         break

