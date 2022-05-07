# Loop-ty loops and code blocks

# for loops ex: for item in list of -> items do each item

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
#     # PAY ATTENTION TO INDENTATION


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#print(student_heights)
 #sum adds the sum of all the items in the list however the exercise wants us to use a for loop to do this
# print(sum(student_heights))

#print(student_heights[n])

# this is what i was missing:
total_height = 0

for height in student_heights:
# original code:
#     print(int(student_heights[0]) + int(student_heights[n -1]))
#     print(type(student_heights)) # class list
#     print(type(student_heights[n])) #class int
# course solution:
    total_height += height
#print(total_height)

number_of_students = 0
for student in student_heights :
    number_of_students += 1
#print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)
