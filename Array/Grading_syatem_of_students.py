# problem:
#  Table 1 shows the marks scored by students for the subject mathematics. Write a 
# program to complete part a to h.
#-----------------------------------------------------------------------|
# | Array index | 0   | 1   | 2   | 3   | 4   |
# | Student     | A   | B   | C   | D   | E   |
# | Marks       | 10  | 25  |23   |100  |45   |

# Declare a one-dimensional array of size 5. 
# Ask user to enter values to fill the array.  
# Find and print the total value of the marks 
#   Output: Total marks = 203 
# Find the highest mark and print 
#   Output: Highest marks = 100 
# Find the Minimum mark and print 
#   Output: Minimum marks = 10 
# Find and print the array index which has the highest mark  
#   Output: Array index of the highest marks = 3 
# Find and print the name of the student who has got the highest mark  
#   Output: Student D has taken the highest marks for mathematics
# Find and print the Grade of each student using following scale. 

# |--------------------------------|
# |  Marks         |  Grade        |
# | 0-44           |  F            |
# | 45-64          |  C            |
# | 65-84          |  B            |
# | 85-100         |  A            |
#-----------------------------------

marks=[]
# get user input
for a in range(5):
    x=int(input(f"Enter marks of student {a+1}: "))
    if x>=0 and x<=100:
        marks.append(x)
    else:
         x=int(input(f"Invalid mark. Please enter again: "))
         marks.append(x)

# Display total mathematics marks of 5 students
total=0
for b in range(5):
    total+=marks[b]

print("Total marks = ",total)

# display the highest mark
c=0
index=0
highest=marks[c]
for c in range(1,5):
    if marks[c]>highest:
        highest=marks[c]
        index=c
print("Highest marks = ",highest)

# display the lowest mark
d=0
lowest=marks[d]
for d in range(1,5):
    if marks[d]<lowest:
        lowest=marks[d]

print("Minimum marks = ",lowest)

# print the index of the highest mark in the array
print("Array index of the highest marks = ",index)

# display the name of the student who got the highest mark
student_name=['A','B','C','D','E']
print(f"Student {student_name[index]} has taken the highest marks for mathematics")

# grading student

grade=''
for g in range(5):
    if marks[g]>=0 and marks[g]<=44:
        grade='F'
    elif marks[g]>=45 and marks[g]<=64:
        grade='C'
    elif marks[g]>=65 and marks[g]<=84:
        grade='B'
    elif marks[g]>=85 and marks[g]<=100:
        grade='A'
    
    # display grade of the student
    print(f"Student {student_name[g]} grade= {grade}")


# sample output:
# Enter marks of student 1: 10
# Enter marks of student 2: 25
# Enter marks of student 3: 23
# Enter marks of student 4: 100
# Enter marks of student 5: 45
# Total marks =  203
# Highest marks =  100
# Minimum marks =  10
# Array index of the highest marks =  3
# Student D has taken the highest marks for mathematics
# Student A grade = F
# Student B grade = F
# Student C grade = F
# Student D grade = A
# Student E grade = C
#------------------------------------------------------------
# Enter marks of student 1: 10
# Enter marks of student 2: 110
# Invalid mark. Please enter again: 25
# Enter marks of student 3: 23
# Enter marks of student 4: -4
# Invalid mark. Please enter again: 100
# Enter marks of student 5: 45
# Total marks =  203
# Highest marks =  100
# Minimum marks =  10
# Array index of the highest marks =  3
# Student D has taken the highest marks for mathematics
# Student A grade= F
# Student B grade= F
# Student C grade= F
# Student D grade= A
# Student E grade= C








