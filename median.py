"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

#test comment
index = len(numbers) // 2
isEven = (len(numbers) % 2) == 0
median = 0

if isEven:
    median = (numbers[index - 1] + numbers[index]) / 2
else:
    median = numbers[index]

print(median)
