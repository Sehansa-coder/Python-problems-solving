# Problem:
# Task: Calculate total salary including overtime.
# Rules:
# Normal hourly rate = $15/hour.
# Overtime rate = 1.5 × hourly rate for hours > 40/week.

# Functions:
#readInputs() → Read employee name and hours worked.
# calculateSalary() → Compute total pay based on hours.
# printSalary() → Display employee name and total salary.

# Define global variables
name=""
hours=0
pay=0

def readInputs():
    global name,hours

# get user input
    name=str(input("Enter employee name: "))
    hours=int(input("Enter no. of hours worked: "))

def calculateSalary():
    global hours,pay
    if hours<=40:
        pay=hours*15
    elif hours>40:
        pay=((hours-40)*1.5*(15))+(40*15)
    else:
        print("Invalid hours")
        exit()

def printSalary():
    global pay,name

# print 
    print("Name:",name)
    print("Total pay=",pay)

# calling functions
readInputs()
calculateSalary()
printSalary()



