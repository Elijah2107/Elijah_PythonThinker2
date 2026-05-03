# Lesson 10 - Bouncing Ball

# ## Task 1: Even or Odd
# Create a function that takes in a number and returns whether it is even.

# 1. Create a function named ‘is_even()’
# 2. If the number is even, the function should return ‘True’
# 3. If the number is odd, the function should return ‘False’
# 4. Using the ‘is_even()’ function, loop through a list of numbers and print them out in this format:
# “3 is an odd number”
# “9 is an odd number”
# “2 is an even number”
# import random
# def is_even(number):
#     return number % 2 == 0

# print(is_even(21))
# numbers = []
# for i in range(10):
#     number = random.randint(1,1000)
#     numbers.append(number)

# print(numbers)

# for num in numbers:
#     if is_even(num):
#         print(f"{num} is even.")
#     else:
#         print(str(num) + " is odd.")
# ## Task 2: Age Group
# Create a function that will take in someone’s age and return either of the following based on the age provided:
# - ‘Child’ (Below 13)
# - ‘Teen’ (14-20)
# - ‘Adult’ (21-64), or
# - ‘Senior’ (65 and above)

# Define the function ‘age_group()’ with one parameter: ‘age’.
# Use ‘if-elif-else’ statements to return the appropriate age group based on the ‘age’ parameter.
# def age_group(age):
#     if age < 14:
#         print("Child")
#     elif age > 13 and age < 21:
#         print("Teen")
#     elif age > 20 and age < 65:
#         print("Adult")
#     else:
#         print("Senior")

# age_group(100)
# ## Task 3: Quadruple the Number 
# Create a function that takes in a number and quadruples it.

# Create a function named quadruple_number() that takes in 1 parameter
# The function should take in a number, and return the quadrupled value of the number
# Using the quadruple_number() function, print the quadruples of the following numbers:
# - 105 (ans: 420)
# - 24 (ans: 96)
# - 402 (ans: 1608)
# - 594 (ans: 2376)

# def add(num1, num2):
#     sum = num1 + num2
#     return sum

# def quadruple_number(num):
#     quad_number = num * 4
#     return quad_number

# quad_num = quadruple_number(594)
# print(quad_num)
# ## Task 4: Sum of squares - Function within a function

# ### Task 4a
# Create a function ‘square()’ that will take in a number and return the squared value of the number. Squared is when the number is multiplied by itself.

# For example, “5 squared” or 5² = 5x5 = 25

# Example:
# square(5) >>> 25
# Square(7) >>> 49
# square(3) >>> 9
# def square(num):
#     squared_num = num * num
#     return squared_num

# def sum_of_squares(num1,num2):
#     sum_squared =  square(num1) + square(num2)
#     return sum_squared

# print(sum_of_squares(343,643))

# write a function to give me a rectangle area with parameters width and height 
# write another function to give me triangle area with parameter width and height
# both function should return the area respectively.


# create a function using the above two function to find the total area of x num of triangle of same height and base and y num of rectangle of same height and width 

# ### Task 4b
# def rectangle(width,height):
#     rec_area = width * height
#     return rec_area

# def triangle(base,height):
#     tri_area = 1/2 * base * height
#     return tri_area

# def sum_of_tri_and_rec(length_of_tri,base_tri, num_tri,length_of_rec, width_rec,num_rec):
#     return rectangle(width_rec, length_of_rec) * num_rec + triangle(base_tri,length_of_tri) * num_tri
    
# print(sum_of_tri_and_rec(10,10,2,10,10,2))

# f_squares()’ that will take in 2 numbers and return the sum of each of the number squared.

# You must use the  ‘square()’ function within the ‘sum_of_squares()’ function.

# Example:
# sum_of_squares(3, 4) >>> 25
# sum_of_squares(2, 7) >>> 53
# sum_of_squares(9, 5) >>> 106

# ## Task 5: Creating a turtle window
# By creating and using the following function, create a turtle window that is 300(w) x 500(h):
# - setup_screen(screenWidth, screenHeight)

# You will require the following:
# 1. import turtle
# 2. turtle.Screen()
# 3. .setup(width=???, height=???)
# 4. return
# 5. ‘screenWidth’ variable
# 6. ‘screenHeight’ variable
import turtle
def setup_screen(screenWidth,screenHeight):
    screen = turtle.Screen()
    screen.setup(width=screenWidth, height=screenHeight)
    return screen

screenWidth = 600
screenHeight = 600
screen = setup_screen(screenWidth,screenHeight)

# ## Task 6: Creating a turtle object
# By creating and using the following function, create a blue circular turtle object with its pen lifted: 
# - create_blue_ball()

# You will require the following:
# 1. turtle.Turtle()
# 2. .shape()
# 3. .color()
# 4. .penup()
# 5. return
def create_turtle_shape(color,shape,width_stretch,length_stretch,outline):
    ball = turtle.Turtle()
    ball.shape(shape)
    ball.color(color)
    ball.shapesize(width_stretch, length_stretch, outline)
    ball.penup()
    return ball

obj1 = create_turtle_shape("blue","circle",1,1,1)

## Task 7: Moving turtle object
# By creating and using the following function, move the turtle object by ‘dx’ and ‘dy’ in a forever loop: 
# - move_ball(ball, dx, dy)

# You will require the following:
# 1. .setx() #set the x coordinate of the turtle
# 2. .xcor() #return you the current x coordinate of the turtle
# 3. .sety()
# 4. .ycor()
# 5. ‘dx’ variable 
# 6. ‘dy’ variable

def move_ball(ball, dx,dy):
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)


# ## Task 8a: Detecting edge (x-axis)
# By creating and using the following function, reverse the x-direction that the turtle object is moving when it touches the left/right side of the window: 
# - check_x(ball, screenWidth)
# - Returns ‘True’ if ball is beyond window in the x-axis

# You will require the following:
# 1. .xcor()
# 2. screenWidth/2
# 3. or
# 4. -screenWidth/2
# 5. *= -1
def check_x(ball,screenWidth):
    

# ## Task 8b: Detecting edge (y-axis)
# By creating and using the following function, reverse the y-direction that the turtle object is moving when it touches the top/bottom side of the window: 
# - check_y(ball, screenHeight)
# - Returns ‘True’ if ball is beyond window in the y-axis

# You will require the following:
# 1. .ycor()
# 2. screenHeight/2
# 3. or
# 4. -screenHeight/2
# 5. *= -1

# ## Challenge: Features to implement
# 1. Have a line trail that the turtle object leave behind as it bounces around
# 2. Change the following each time the turtle object bounces:
# - Colour of the turtle object
# - Speed of the turtle object (faster/slower)
# - Shape of the turtle object
# 3. Use a variable to count the number of times the ball has bounced
# 4. Exit the loop when the ball bounces 50 times.
# 5. Use the time library to keep the program running for ‘x’ seconds determined by the user
dx = 1
dy = 1

while True:
    move_ball(obj1, dx, dy)  



turtle.done()