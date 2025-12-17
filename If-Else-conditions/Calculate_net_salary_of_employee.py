# ( BSC In Information and Technology- Higher Diploma Year 1 question)
# Problem:
# Write a  program to calculate and print the net salary of the employee depending on the 
# basic salary and the allowance. User enters the basic salary and the no of overtime hours to 
# the program as a user input.

# The allowance for the person calculated as follows based on the no of overtime hours: 

# -----------------------------------------------------------
# |No. Overtime hours             |   Allowance             |
# |-------------------------------|-------------------------|
# | No of Overtime Hours>=30      |  20% from basic salary  |
# | 20=<No of Overtime Hours<30   |  10% from basic salary  |
# | 10=<No of Overtime Hours<20   |  5% from basic salary   |
# | No of Overtime Hours<10       |  No allowance           |

# The Net salary of the employee is calculated as follows: 
# Netsalary = basicsalary+ allowance 

basicsalary=float(input("Enter basic salary:"))
ot=int(input("Enter no of overtime hours:"))

allowance=0
if ot>=30:
    allowance=basicsalary*0.20
elif ot>=20 and ot<30:
    allowance=basicsalary*0.10
elif ot>=10 and ot<20:
    allowance=basicsalary*0.05
elif ot<10:
    allowance=0


netsalary=basicsalary+allowance

print("The Net Salary of Employee:",netsalary)

# Sample Output: 
# Enter basic salary: 25000 
# Enter no of overtime hours: 25 
# The Net Salary of Employee: 27500 