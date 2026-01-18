## Recap 1: Pseudocode (Recycling logic)
# Task: Write down the steps on how to solve the problem below

# Design pseudocode for a recycling robot that sorts items
# into bins for glass, plastic, and paper. The robot should
# check each item's material and place it in the correct bin.

# glass_bin = 0
# paper_bin = 0
# plastic_bin = 0 
# recyclable = when asked "what are you recycling?"
# if recyclable = glass 
#     glass_bin + 1
# elif recyclable = paper
#     paper_bin + 1
# else
#     plastic_bin + 1   1

## Recap 2: Variables & Mind map

redPlate = 1
bluePlate = 2
greenPlate = 3
total = 0
# redPlate = redPlate * 3
# bluePlate = bluePlate * 5
# greenPlate = greenPlate * 4
# total = redPlate + bluePlate + greenPlate
# print("$" + str(total))

# ask the user for the number of plate for red, blue and green
# numOfRedPlates = int(input("How many red plates do you have? "))
# numOfBluePlates = int(input("How many blue plates do you have? "))
# numOfGreenPlates = int(input("How many green plates do you there? "))
# redPlate = redPlate * numOfRedPlates
# bluePlate = bluePlate * numOfBluePlates
# greenPlate = greenPlate * numOfBluePlates
# total = redPlate + bluePlate + greenPlate
# print("$" + str(total))

## Recap 3: Debugging Average Score Program
# There is a total of 3 bugs in the following program.
# Identify and fix the bugs:

# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))

## Recap 4: If..elif..else & Flowchart
# Write a program that asks the user to input a score
# (as an integer) and then assigns a grade based on that score.
# Use the following grading scheme:

# If the score is 75 or higher, the grade is 'A'.
# If the score is between 60 and 74 (inclusive), the grade is 'B'.
# If the score is between 50 and 59 (inclusive), the grade is 'C'.
# Any score below 50 will be graded as 'Fail'.

# Use flowchart to draw out all decisions that are to be made
# before starting on your code.

score = int(input("What is your score? "))
if score >= 75:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
else:
    print("Fail")