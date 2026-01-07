# problem by-------------------Codewars--------------------
# source: https://www.codewars.com/kata/541da001259d9ca85d000688

# Explanation:
# In this kata, you will write an arithmetic list which is basically a list that 
# contains consecutive terms in the sequence.
# You will be given three parameters :
# first - the first term in the sequence
# c - the constant that you are going to ADD ( since it is an arithmetic sequence...)
# l - the number of terms that should be returned

def arithmetic_pattern(first,c,l):
    result=[]
    for i in range(l):
        result.append(first)
        first=first+c

    return result

# get user input
first=int(input("Enter first number : "))
adder=int(input("Enter the constant that you :"))
terms=int(input("Enter the number of terms should return : "))

# call the function
print(arithmetic_pattern(first,adder,terms))

# sample output:
# Enter first number : 1
# Enter the constant that you :3
# Enter the number of terms should return : 5
# [1, 4, 7, 10, 13]

