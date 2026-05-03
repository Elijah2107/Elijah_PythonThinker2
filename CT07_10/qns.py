# Qns: Student Score Analyzer

# You are given a list of student marks:

marks = [85, 42, 73, 91, 58, 67, 81, 95]

# =========================
# Task 1: Create a Function
# =========================

# Function Name: get_total
# Parameter: marks (list of integers)
# Return Type: integer

# Description:
# This function should return the total of all marks.
def get_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total

# =========================
# Task 2: Create Another Function
# =========================

# Function Name: get_average
# Parameter: marks (list of integers)
# Return Type: float

# Description:
# This function should return the average mark.

# IMPORTANT:
# You MUST use get_total() inside this function.
def get_average(marks):
    return get_total(marks)/len(marks)
# =========================
# Task 3: Create a Function with Condition
# =========================

# Function Name: count_pass
# Parameter: marks (list of integers)
# Return Type: integer

# Description:
# This function should return the number of students who scored 50 and above.
def count_pass(marks,passing_mark):
    count = 0
    for mark in marks:
        if mark >= passing_mark:
            count += 1
    return count     


# =========================
# Task 4: Combine Functions
# =========================

# Function Name: analyze_marks
# Parameter: marks (list of integers)
# Return Type: None

# Description:
# This function should:
# - call get_total()
# - call get_average()
# - call count_pass()
# - print the results neatly
def analyze_marks(marks):
    total_marks = get_total(marks)
    average = get_average(marks)
    passers = count_pass(marks,50)
    print(total_marks + average + passers)

analyze_marks(marks)
# =========================
# Task 5: Call the Function
# =========================

# Call analyze_marks(marks)

# Task 6:
# Modify count_pass() so that it takes an extra parameter:
# passing_mark (integer)

# Example:
# count_pass(marks, 60)