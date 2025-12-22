# A program is required to calculate and print the net salary of an employee depending on the 
# basic salary and the commission. The user enters the position and the sales done as user input 
# to calculate the basic salary and commission, respectively. Hint: use the global variables. 
# Consider the following to write the functions: 

# Implement a function called readData() to read the emp no, emp name, executive position and no of sales.  
#  Implement a function called findBasicSalary() to find the basic salary scale of the employee. A company offers the 
# following basic salary scales for two types of marketing executive 
# positions.
# |-----------------------------------|
# | Position      | Basic salary      |
# |  1            |   25000           |
# |  2            |   50000           |
# -------------------------------------

#  If an invalid executive position is entered. display an error message.

# Implement a function called findRate() to find the commission rate based on the sales are done. The commission rates are given below.  

# |--------------------------------------------------|
# | sales                       |commission rate     |
# |6000 or above                |   20%              |
# |4000-5999                    |   15%              |
# |3000-3999                    |   10%              |
# | Below 3000                  |   5%               |
# ----------------------------------------------------

#  Implement a function called calculateCommission() to calculate the commission of the employee.   
#         Commission=basic salary * Commission Rate 

#   Implement a function called calculateNetSalary() to calculate the net salary of the employee.  
#         Net salary = basicsalary+ commission

#  Implement a function called printDetails() to print the employee details. (Details include emp no, emp name, net salary) 

# Implement the main method  to call the respective modules to perform the following tasks.
#--------------------------------------------------------------------------------------------------------------------------------------------

#  We should define the global variables to use them in everywhere of the code
emp_name=""
empno=""
sales=0
position=0
basicSalary=0
commissionRate=0
netSalary=0
commission=0

def readData():
    # define the global variables needed for each function
    global empno,emp_name,position,sales
    empno=str(input("Enter employee no:"))
    emp_name=str(input("Enter employee name:"))
    position=int(input("Enter the position(1/2):"))
    sales=int(input("Enter no. of sales:"))

def findBasicSalary():
    global basicSalary
    if position==1:
        basicSalary=25000
    elif position==2:
        basicSalary=50000
    else:
        print("Invalid position")
        basicSalary=0
        exit()
    
def findRate():
    global commissionRate
    if sales>=6000:
        commissionRate=0.20
    elif sales>=4000 and sales<=5999:
        commissionRate=0.15
    elif sales>=3000 and sales<=3999:
        commissionRate=0.10
    elif sales<3000:
        commissionRate=0.05
    
def calculateCommission():
    global commission
    commission=basicSalary*commissionRate

def calculateNetSalary():
    global netSalary
    netSalary=basicSalary+commission

def printDetails():
    print(f"The Employee No is :{empno}")
    print(f"The Employee name is {emp_name}")
    print(f"The Net salary is {netSalary}")

# call functions
readData()
findBasicSalary()
findRate()
calculateCommission()
calculateNetSalary()
printDetails()



# Sample output
#-----------------------------------------
# Enter Employee No: E_111 
# Enter Employee Name: Jagath Silva 
# Enter Position: 1 
# Enter no of Sales :3500 
# The Employee No is E_111  
# The Employee name is Jagath Silva 
# The Net salary is 27500
