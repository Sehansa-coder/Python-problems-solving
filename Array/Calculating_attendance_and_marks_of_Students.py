# problem:
# Student attendance & test marks
# A class has 8 students. For each student, the lecturer record:
#  - attendance percentage
#  - Test marks
# Write a program to decare 2D array to store attendance and test marks of 8 students.
# Input and store the data using the keyboard
# Find and display the 
#  - highest attendance
#  - highest test mark

rows=8
cols=2

arr=[]
for i in range(rows):
    print(f"Enter marks and attendance for student {i+1}:")
    marks=int(input("Enter test marks:"))
    attendance=int(input("Enter your attendance out of 10 days:"))

    arr.append([marks,attendance])

highest_attendance=arr[0][1]
highest_marks=arr[0][0]

for x in range(1,8):
    if arr[x][0]>highest_marks:
        highest_marks=arr[x][0]
    if arr[x][1]>highest_attendance:
        highest_attendance=arr[x][1]

print("Highest attendance=",highest_attendance," days out of 10 days")
print("Highest marks=",highest_marks)

# sample output:

# Enter marks and attendance for student 1:
# Enter test marks:40
# Enter your attendance out of 10 days:5
# Enter marks and attendance for student 2:
# Enter test marks:60
# Enter your attendance out of 10 days:4
# Enter marks and attendance for student 3:
# Enter test marks:98
# Enter your attendance out of 10 days:3
# Enter marks and attendance for student 4:
# Enter test marks:25
# Enter your attendance out of 10 days:10
# Enter marks and attendance for student 5:
# Enter test marks:86
# Enter your attendance out of 10 days:3
# Enter marks and attendance for student 6:
# Enter test marks:94
# Enter your attendance out of 10 days:5
# Enter marks and attendance for student 7:
# Enter test marks:74
# Enter your attendance out of 10 days:2
# Enter marks and attendance for student 8:
# Enter test marks:80
# Enter your attendance out of 10 days:1

# Highest attendance= 10 days out of 10 days
# Highest marks= 98