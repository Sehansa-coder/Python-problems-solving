# Problem: (HackerRank style )

# Explantion:
# You are given a student’s exam score as an integer score.
# Write a Python program that assigns a grade based on the following rules:

# If score is 90 or above → Grade = "A"
# If score is 75 to 89 → Grade = "B"
# If score is 50 to 74 → Grade = "C"
# If score is below 50 → Grade = "Fail"
#A single integer score
# (0 ≤ score ≤ 100)

# You must use ternary operator(s) to determine the grade.

score=int(input("Enter score:"))
grade=(
    "A" if score>=90 else
    "B" if score>=75 else
    "C" if score>=50 else
    "Fail"
)

print(grade)

# less than 50 means including inputs less than the range
 # of (0 ≤ score ≤ 100). Therefore all are fail


