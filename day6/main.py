# Defining and calling python functions

# 

# print("hello")
# len("hello")

# # if we want to make our own function we use the def keyword def my_function():  example:
# def my_function():
#     print("hello")
#     print("bye")

# # to execute or to call the function:

# my_function()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def race():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()

race()

def race1():
    turn_left()
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    

race = int(0)
while race <= int(25):
    race += int(1)
    race1()
    if race == int(25):
    done()    