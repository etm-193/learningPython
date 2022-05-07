# We need to write a program that calculates the sum of all the even numbers from 1 to 100
# including 1 and 100

# step one determine the range.
# step two define even numbers.
# step three sum all even nums.
# step four print the result.


total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

# Alternative two

total2 = 0
for number in range(2, 101, 2):
    total2 += number
print(total2)
