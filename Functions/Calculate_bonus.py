#  Write a function called calBonus () to calculate the bonus amount of an employee based 
#  on the basic salary. If basic salary is greater than 20000, the bonus amount will be twice 
#  of basic salary or otherwise it will be half of the basic salary. The function takes the basic 
#  salary as a parameter and returns the bonus amount.  
#  The main program reads the basic salary of an employee from the keyboard, calls 
#  calBonus () function and displays the net salary of an employee. 
#  Note: Use the below equation to calculate the netsalary.  
#      NetSalary = Basic Salary + Bonus

def calBonus(basic_salary):
    if basic_salary>20000:
        return basic_salary*2
    else:
        return basic_salary/2
    
salary=float(input("Enter basic salary:"))
bonus=calBonus(salary)
print("Bonus=",bonus)

net_salary=salary+bonus
print("The net salary is: ",net_salary)

# sample output:
# Enter basic salary:30000
# Bonus= 60000.0
# The net salary is:  90000.0

#---------------------------------
# Enter basic salary:12000
# Bonus= 6000.0
# The net salary is:  18000.0