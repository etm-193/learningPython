# Highes scores

# the max function print(max(student_scores)) = max value within a list, min function print(max(student_score)) = min value within a list


# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# the course is asking for me to replicate the max function for the scores that are input as a list using a for loop.
# In other words they want us to check each value and compare to see which one is higher.

# highest_score = 0

# for score in student_scores:
#     if score > highest_score:
#         highest_score = score

# print(f" the highest score in the class is: {highest_score}")

# truns out you can use if statements within for loops

#for loops with range operators

#  for number in range(a, b):
#       print(number)
total = 0
for number in range (1, 101):
    total += number
print(total)