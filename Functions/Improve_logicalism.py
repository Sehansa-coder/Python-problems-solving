#----------------------By Codewars-------------------------
# source: https://www.codewars.com/kata/54147087d5c2ebe4f1000805

# problem:
#  Create a function that takes three arguments:
#    a value to be evaluated for truthiness.
#    a function to execute if the first argument is truthy.
#    a function to execute if the first argument is falsy.
# If the first argument evaluates to truthy, call the second argument (a function). 
# If it evaluates to falsy, call the third argument instead (also a function).

# In statically-typed languages, the first argument will be a boolean. In dynamically-typed languages that 
# attribute a truth value to all expressions, it may be of any type.


def check_one():
    return "correct"

def check_two():
    return "Incorrect"

def check_both(value,one,two):
    if value:
        return check_one()
    else:
        return check_two()

    

value=False
print(check_both(value,check_one,check_two))

# sample output:
# Incorrect
#--------------------
# If we give value=True,  it prints "correct"