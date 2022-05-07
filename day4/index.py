# index errors

states_of_america = ["delaware", "pensilvania"]

# an index error happens when we try to call an item thats beyond the qty of items in a list ex the previous list

fruits = ["Strawberries", "Nectarines", "apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# a nested list
dirty_dozen = [fruits, vegetables]

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


horizntal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizntal -1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
