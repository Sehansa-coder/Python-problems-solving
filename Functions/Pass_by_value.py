# A company wants to give a salary raise to an employee temporarily to see the effect, without changing the original salary stored in the system.
# Create a function tempRaise(salary, bonus) that adds bonus to the salary and prints the new value inside the function.
# Outside the function, print the original salary to show it has not changed.


bonus=500
# original salary
salary=5000

def tempRaise(salary,bonus):
    salary=salary+bonus  # this change only the local copy of salary
    print("Inside function:",salary)


tempRaise(salary,bonus) 
print("Outside function:",salary)

# sample output
#----------------------------
# Inside function: 5500
# Outside function: 5000


