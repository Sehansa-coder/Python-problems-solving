# problem:

# Write a program with functions to classify a person into an age group:
# readInputs() -> reads the name ans age from the user
# processGroup() -> determines the age group
# 0-12 -> "child"
# 13-19 -> "teenager"
# 20-59 -> "Adult"
# 60+ -> "Senior"
# printMessage() -> prints "Hi [name], you are an [age group]."

# define global variables
name=""
age=0
age_group=""

def readInputs():
    global name,age

# get user input
    name=str(input("Enter name: "))
    age=int(input("Enter age:"))

def processGroup():
    global age,age_group

    if age>0 and age<=12:
        age_group="Child"
    elif age>=13 and age<=19:
        age_group="Teenager"
    elif age>=20 and age<=59:
        age_group="Adult"
    elif age>=60:
        age_group="Senior"
    else:
        print("Invalid age")
        exit()  # end the program

# print the messege
def printMessage():
    global name,age_group

    print(f"Hi {name}, you are a {age_group}.")

readInputs()
processGroup()
printMessage()

# Sample output:
# Enter name: sehansa
# Enter age:18
# Hi sehansa, you are a Teenager.
#-------------------------------------
# Enter name: don
# Enter age:89
# Hi don, you are a Senior.
#-------------------------------------
# Enter name: rafayel
# Enter age:-2
# Invalid age
# <program ends>