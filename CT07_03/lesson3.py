# ## Task 1: Study Timer
# **Task: Write a program that acts as a study timer**
# 1. The user must input how many minutes they plan to study
# 2. Use a while loop to count down the minutes
# 3. Display "Good job!" once the timer is up

# Hint: you will need the time.sleep(). However this function
# only takes in seconds.
# You will need to write a conversion algorithm to change
# minutes to seconds.

# 15 min left
# 14 min left

# timer = int(input("How many minutes do you plan to study? "))
# while timer > 0:
#     print(timer)
#     time.sleep(60)
#     timer -= 1



# ## Task 2: Allowance Savings Tracker
# **Task: Write a program to track how much you save, and
# inform you when your savings is more than $100**
# 1. Create a variable called savings
# 2. Using a while loop, ask how much money you save every
#    day
# 3. While savings is less than 100, you continue to save
# 4. Exit the program when savings is more than 100 and
#    congratulate the user.

# import time
# savings = 0
# dailySavings = int(input("How much money did you save today? "))
# while savings < 100:

#     print(savings)    
#     savings = savings + dailySavings
#     time.sleep(1)
    
# print("Congratulations! You have saved more than $100!")


## Task 3: Multiplication Quiz
# **Task: Ms Tan, your math teacher knows that you are a
# programming whiz,
# she has asked you to help code a multiplication quiz for
# the class to practice.**

# Here are her requirements:
# 1. Students have to answer 15 questions in total
# 2. Students have 3 lives (chances). i.e. they can get the
#    question wrong 3 times.
# 3. The questions will be in this format: "What is 3 x 19? ". 
# 4. The numbers for each question will be randomly generated
#    and between the range of 2 to 20.
# 5. If the student answers correctly, move on to the next
#    question
# 6. If the student answers wrongly, minus 1 life, and ask
#     the question again.
# 7. If the student has no more lives, exit and print
#     "GO AND SEE MS TAN FOR REMEDIAL"

import random 
lives = 3
while True:
    for count in range(15):
        num1 = random.randint(2,20)
        num2 = random.randint(2,20)
        ans = int(input("What is " + str(num1) + " x " + str(num2) + " ? "))
        realAns = int(num1) * int(num2)
        if ans == realAns:
            print("correct")
        else:
            lives -= 1
    
        if lives == 0:
            print("GO AND SEE MS TAN FOR REMEDIAL")
    break   