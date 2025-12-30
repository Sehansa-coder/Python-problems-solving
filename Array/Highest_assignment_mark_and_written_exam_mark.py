# problem:
#  program to complete following tasks: 
# ‘Program Design’ subject is evaluated using one assignment and a written exam. There 
# are 10 students in a batch. The lecturer needs to do the following with the marks of 
# these 10 students: 
# Declare 2D array and enter and store of assignment and written exam marks. 
# Find the highest assignment mark and the highest written exam mark.

rows=10
cols=2

marks=[]
for a in range(rows):
    print(f"Enter marks for student {a+1}:")
    
    # get user input
    assignment=int(input("Enter assignment mark:"))
    written=int(input("Enter marks for written exam:"))

    marks.append([assignment,written])

print(marks)
# assign highest assignment mark
highest_assignment_mark=marks[0][0]
# assign highest written exam mark
highest_written_mark=marks[0][1]

for i in range(1,10):
    if marks[i][0]>highest_assignment_mark:
        highest_assignment_mark=marks[i][0]
    if marks[i][1]>highest_written_mark:
        highest_written_mark=marks[i][1]

print(f"Highest Assignment mark= {highest_assignment_mark}")
print(f"Highest written exam mark= {highest_written_mark}")

# sample output:
# Enter marks for student 1:
# Enter assignment mark:1
# Enter marks for written exam:10
# Enter marks for student 2:
# Enter assignment mark:2
# Enter marks for written exam:20
# Enter marks for student 3:
# Enter assignment mark:3
# Enter marks for written exam:30
# Enter marks for student 4:
# Enter assignment mark:4
# Enter marks for written exam:40
# Enter marks for student 5:
# Enter assignment mark:5
# Enter marks for written exam:50
# Enter marks for student 6:
# Enter assignment mark:6
# Enter marks for written exam:60
# Enter marks for student 7:
# Enter assignment mark:7
# Enter marks for written exam:70
# Enter marks for student 8:
# Enter assignment mark:8
# Enter marks for written exam:80
# Enter marks for student 9:
# Enter assignment mark:9
# Enter marks for written exam:90
# Enter marks for student 10:
# Enter assignment mark:11
# Enter marks for written exam:100
# [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [11, 100]]
# Highest Assignment mark= 11
# Highest written exam mark= 100