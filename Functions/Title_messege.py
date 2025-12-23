# ( BSC In Information and Technology- Higher Diploma Year 1 question)

# Problem:

# program to print the message which included the title of the person. The 
# user enters the person’s first name, last name, marital status, and gender as user input. 
# Consider the following to write the functions: Hint: use the global variables 
# A. Implement a function called readInputs () to read the person’s first name, last name, 
# marital status, and gender. 
# B. Implement a function called processTitle () Module to find the title of the person 
# based on the marital status, and gender.   
# C. Implement a function called PrintMessage () Module to print the message.   
# D. Implement the main method to call the respective modules to perform the following tasks.  

# Read the inputs from the user. 
# Find the title. 
# Print the message.

# Define global variables
first_name=""
second_name=""
marital_status=""
gender=""
answer=""

def readInputs():
    global first_name,second_name,marital_status,gender

    # get user input
    first_name=str(input("Enter first name:"))
    second_name=str(input("Enter second name:"))
    gender=str(input("Enter gender(male/female):"))
    marital_status=str(input("Enter marital status(single/married): "))
    marital_status=marital_status.lower()
    gender=gender.lower()

def processTitle():
    global answer,first_name,second_name,marital_status,gender

# check validity of inputs to process title messege
    if marital_status=="married" and gender=="female":
        answer="Mrs"
    elif marital_status=="single" and gender=="female":
        answer="Miss"
    elif marital_status=="married" and gender=="male":
        answer="Mr"
    elif marital_status=="single" and gender=="male":
        answer="Mr"
    else:
        print("Invalid marital status or gender")
        exit()

def PrintMessage():
    global answer,first_name,second_name
    print(f"Hi {answer} {first_name} {second_name}")

# call functions
readInputs()
processTitle()
PrintMessage()

# Sample output:
# Enter first name:selena
# Enter second name:gomershy
# Enter gender(male/female):female
# Enter marital status(single/married): single
# Hi Miss selena gomershy
#-----------------------------------------------------
# Enter first name:katerine
# Enter second name:james
# Enter gender(male/female):female
# Enter marital status(single/married): married
# Hi Mrs katerine james
#-----------------------------------------------------

# Enter first name:jonathan
# Enter second name:gates
# Enter gender(male/female):male
# Enter marital status(single/married): single
# Hi Mr jonathan gates

#-----------------------------------------------------
# Enter first name:sehansa
# Enter second name:dewlini
# Enter gender(male/female):FEMALE
# Enter marital status(single/married): SINGLE
# Hi Miss sehansa dewlini
#-----------------------------------------------------

# Enter first name:FATHIMA
# Enter second name:MIRSHA
# Enter gender(male/female):NONE
# Enter marital status(single/married): single
# Invalid marital status or gender

