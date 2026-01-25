# print("Hello from lesson 2")

## Recap 1: For Loop
# **Task: write a separate 'for' loop to print the following
# numbers:**
# 1. from 0 - 20
# 2. from 1 to 30
# 3. from 2 to 24 (in even numbers)
# 4. from 55 to 76 (odd numbers)

# Recap 1.1
# for count in range(21):
#     print(count)

# Recap 1.2
# for count in range(31):
#     print(count)

# Recap 1.3
# for count in range(2,25,2):
#     print(count)

# Recap 1.4
# for count in range(55,76,2):
#     print(count)

# Recap 1.5
# for count in range(72,2,-3):
#     print(count)

## Task 1: Introduction to while loop
# **Task: Using a separate 'while' loop, print each of the
# following:**
# 1. from 0 to 20
# 2. from 1 to 30
# 3. from 2 to 24
# 4. from 55 to 76 (odd numbers)
# 5. from 72 to 3 (in multipers of 3) 
# 6. from 48 to -36 (in multipers of 4) 
# 7. from 48 to -36 (in multipers of 7 or 9) 
# 8. from 48 to -36 (in multipers of 19) 


# Task 1.1
# counter = 0
# while counter <= 20:
#     print(counter)
#     counter += 1
    
# Task 1.2
# counter = 1
# while counter <= 30:
#     print(counter)
#     counter += 1

# Task 1.3
# counter = 2
# while counter <= 24:
#     print(counter)
#     counter += 1

# Task 1.4
# counter = 55
# while counter <= 76:
#     print(counter)
#     counter += 2

# Task 1.5
# counter = 72
# while counter >= 3:
#     print(counter)
#     counter -= -3

# Task 1.6
# counter = 48 
# while counter > -37:
#     print(counter)
#     counter -= 4

# Task 1.7
# counter = 48
# while counter > -37:
#     if counter%7 == 0:
#         print(counter)
    
#     if counter%9 == 0:
#         print(counter)

#     counter -= 1

## Task 2: while... break
# The **break** keyword will **break** out (exit) the loop.
# When a **break** is encountered, the code in the **else** will
# not be run.

# Using a while loop:
# 1. print the numbers from 1 to 10
# 2. if the number is 5, **break** out of the loop

# counter = 1
# while True:
#     print(counter)
#     if counter == 5:
#         break
#     counter += 1

# **Task 3a**: Using a while loop
# 1. print the numbers from 1 to 10
# 2. once count has reached 10, use the else and print "Count
#    has reached 10"

# counter = 1
# while counter < 10:
#     print(counter)
#     counter += 1
# else:
#     print("Count has reached 10")

# **Task 3b**:
# Now, modify your 'while' loop such that:
# 1. If the number is 5, **break** out of the loop
# 2. Ensure your code has an else

# Observe if the code in the **else** runs.

# counter = 1
# while counter < 10:
#     print(counter)
#     if counter == 5:
#         break
#     counter += 1
# else:
#     print("Count has reached 10")

# ## Task 4: Ordering Pizzas with while loop
# **Task: Using what you have learned above, code a program to
# take a customer's order for pizza.
# Declare a variable called _topping_.**

# Using a while loop:
# 1. Ask the user to enter a choice of topping
# 2. For each topping entered, concatenate to the 'topping'
#    variable
# 3. exit the while loop if the user enters "end"
# 4. On program end, print out the toppings that the customer
#    has chosen.
# topping = ""
# while True:
#     topping_response = input("What is your topping? ")
#     if topping_response == "end":
#         break
    
#     topping = topping + topping_response + ", "

# print(topping)

# ## Task 5: General Knowledge Quiz
# **Task: Create a program to quiz users on their general
# knowledge**

# Using the while loop, ask 3 general knowledge questions
# 1. Using input ask the question
# 2. While answer is not correct, repeat the question.
# 3. Move on to the next question when the answer is correct

# Bonus:
# 1. Add a score system
# 2. Add an ability for users to skip by saying “skip”
# 3. Disqualify user when they have tried too many times

# while True:
#     ans1 = input("Why is 67 so viral? ")
#     if ans1 == "67":
#         break
#     print("you lost LOL")
# print("Exactly!")
    
# while True:    
#     ans2 = input("When was YouTube created? ")
#     if ans2 == "2005":
#         break
#     print("you lost LOL")
# print("Exactly!")

# while True:
#     ans3 = input("Who is the most subscribed YouTuber? ")
#     if ans3 == "MrBeast":
#         break
#     print("you lost LOL")
# print("Exactly!")

