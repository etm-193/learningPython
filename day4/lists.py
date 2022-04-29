# List data structure (arrays in java)

import random

# list = [item1, item2]
# can you do the same as in javaScript to use objects variables etc within arrays?
florida = "homestate"

states_of_america = ["Delaware", florida,]

print(states_of_america[1])

# so yes to a degree so far we can use objects

# if we want to add an item to the end of a list we can use commands such as .append or extend

# coding challenge banker roulette

names = ["ernesto", "alex", "joelma", "sara"]

unlucky_soul = names[random.randint(0, 3)]

print(unlucky_soul)

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_pays = names[random_choice]

# i just did this part of the course just to do it... 