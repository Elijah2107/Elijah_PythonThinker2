# Lesson 8 - Input Validation

## Recap 1: List Manipulation
# You have a list of student index numbers who attended the Math Enrichment class. 
# However, some students’ attendance were recorded more than once due to a human error.
# Your task is to clean the list and produce a list of unique Student Indexes

# Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
# Sort the cleaned list in ascending order.
# - Print the final list and also print how many duplicates were removed.
# - Print the count of how many students attended the Math Enrichment Class.

# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]
# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]
# cleaned_list = []
# for index in student_indexes:
#     if index not in cleaned_list:
#         cleaned_list.append(index)


# duplicatesRemoved = len(student_indexes)-len(cleaned_list)
# print(duplicatesRemoved)
# print(len(cleaned_list))
# group all the student indexes such that it is in ascending order 
# if there is more than once, put them together, for example if there is two 1042, they should be in [1042,1042]
# the final result is a nested list where by those with duplicate are in [1042,1042] manner 
# and those unique would be in [1043] manner and the nested list will be [[1042,1042], [1043], ...]
# 1. sort the student_indexes
# 2. put into the nested list

## Task 1: Data Format Check

### Task 1a
# Ask the user to input their first name until it is a valid name. 
# A valid name only contains alphabets.
# Keep asking for a name until a valid name is input.


# first_name = ""
# while not first_name.isalpha():
#     first_name = input("What's your name? ")
    
      
### Task 1b
# Ask the user to input their age until it is a valid number. 
# Keep asking for a name until a valid number is input.

# first_name = ""
# while not first_name.isnumeric():
#     first_name = input("What's your age? ")

### Task 1c
# Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters

# while True:
#     username = input("What is your username? ")
#     if username.isalnum():
#         break
# print(f"Username is {username}")

## Task 2: Length Check (using a while loop)

### Task 2a
# Ask the user to input their phone number until it is valid using a while loop.
# Make sure to check if the input is the correct data type as well!
# phone_number = ""
# username = ""
# while True:
#     phone_number = input("What is your phone number? ")
#     if len(phone_number) == 8 and phone_number.isdigit():
#         break
# while True:
#     username = input("What is your username? ")
#     if len(username) >= 5 and len(username) <= 18 and username.isalnum():
#         break

# print(f"My phone num is {phone_number}")
# print(f"My username is {username}")
### Task 2b
# Ask the user to a username and check if it is between 5 to 18 characters long.

## Task 3: Range Check (using a while loop)

### Task 3a
# Ask the user to input their birth year and check if it is between 1900 and the current year. Keep asking until a correct value is given.

# while True:
#     birth_year = input("What is your birth year? ")
#     if int(birth_year) > 1900 and int(birth_year) < 2027:
#         break
#     else:
#         print("It is invalid")
# while True:
#     volume = input("What is your volume? ")
#     if int(volume) >= 0 and int(volume) <= 100:
#         break
#     else:
#         print("It is invalid")

### Task 3b
# Ask the user to input their volume setting and check if it is between 0 and 100.

## Task 4: Mocking Text Generator
# Create a program that will turn regular sentences into a “SpongeBob Mocking” meme.
# For example, the program will turn “Hello my name is James” into “HeLlO mY nAmE iS jAmEs”

# 1. Using input(), ask the user for a sentence
# 2. Use loops to iterate through each letter in the sentence
# 3. Alternate between .upper() and .lower() for each letter
# 4. Print the result.
# sentence = input("Give me a sentence. ")
# new_sentence = ""
# for i in range(len(sentence)):
#     if i%2 == 0: #you are trying to get the even index number
#         new_sentence += sentence[i].lower()
#     else:
#         new_sentence += sentence[i].upper()
# is_upper = True
# for char in sentence:
#     if char.isalpha():
#         if is_upper:
#             new_sentence += char.upper()
#         else:
#             new_sentence += char.lower()
#         is_upper = not is_upper
#     else:
#         new_sentence += char
# print(new_sentence)
## Task 5: Slice String
# word = “SINGAPORE”

# Slice the string and print these words:
# a. SING
# b. GAP
# c. PORE
# d. SNAOE
# word = "SINGAPORE"
# print(word[:4])
# print(word[3:7])
# print(word[5:])
# print(word[::2])
## Task 6: Palindrome
# Ask the user for an input and check if it is a palindrome, until the input is ‘end’.

# You can try this list of words:
# - civic, kayak, level, madam, radar, refer, rotator, tenet, racecar, deified, stats, wow
# while True:
#     word = input("Give me a word ")

#     if word == "end":
#         break

#     if word == word[::-1]:
#         print("It is palindrome.")
#     else:
#         print("It isn't palindrome")
## Task 7: Presence and Existence Checks
# You are hosting a Birthday Party and have invited your friends.

# Create a list with your friends’ names
# - e.g. c

# Write a program to ask for the visitor’s name and check if:
# - Name is entered (presence check)
# - Name is in your friend list (existence check)
# friend_list = ["Alice", "Bob", "Carl", "Dylan"]
# while True:
#     name = input("What's your name? ").strip()
#     if name == "":
#         print("Please enter something.")
#     else:
#         break

# if name in friend_list:
#     print("Go in")
# else:
#     print("Not on the list OUT!")
# Ask for an input again if a name was not entered.
# Accept the visitor if they are in the list, else deny their entry.

## Task 8: Format Check
# Ask the user to input their NRIC you need to check:
# 1. First and last character are alphabets in upper case
# 2. First letter must be S, T, F, G, or M.
# 3. Have 7 digits between the alphabets
# 4. Be 9 characters long
# first_letter = ["S", "T", "F", "G", "M"]
# has_first_char_upper = False
# has_last_char_lower = False
# is_first_last_upper = False
# has_seven_digit_between_alphabet = False
# is_first_letter_in_list = False
# is_nine_char = False

# while True:
#     nric = input("NRIC?: ")
#     if len(nric) == 9:
#         is_nine_char = True
#     # if nric[0].isalpha() and nric[0].isupper():
#     #     has_first_char_upper = True
#     # if nric[-1].isalpha() and nric[-1].isupper():
#     #     has_last_char_lower = True
#     if nric[-1].isalpha() and nric[-1].isupper() and nric[0].isalpha() and nric[0].isupper():
#         has_last_char_upper = True
#     if nric[1:len(nric)-1].isdigit():
#         has_seven_digit_between_alphabet = True
#     if nric[0] in first_letter:
#         is_first_letter_in_list = True
#     if is_first_last_upper and has_seven_digit_between_alphabet and is_first_letter_in_list and is_nine_char:
#         break
#     else:
#         print("Please enter the correct format")
## Task 9: Password Validation
# A website requires all passwords to
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers.

# Write a program that will ask the user for a password, and check if the password fits all criteria

# You may use some of the following passwords to test your program:
# - PassW0rd
# - H3ll0W0r1d
# - BestF00d
# - pa55Me
# is_eight_character_and_more = False
# contain_upper_case = False
# contain_lower_case = False
# contain_number = False
# no_sus_symbols = False
# while True:
#     password = input("Give me a password ")
#     if len(password) >= 8:
#         is_eight_character_and_more = True
    
#     for char in password:
#         if char.isupper():
#             contain_upper_case = True
#         elif char.islower():
#             contain_lower_case = True
#         elif char.isdigit():
#             contain_number = True

#     if password.isalnum():
#         no_sus_symbols = True
    
#     if is_eight_character_and_more and contain_upper_case and contain_lower_case and contain_number and no_sus_symbols == True:
#         break
#     else:
#         print("Invalid! Try again!")