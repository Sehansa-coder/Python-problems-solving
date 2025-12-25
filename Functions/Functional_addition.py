#----------by Codewars------------------------
# source: https://www.codewars.com/kata/538835ae443aae6e03000547
# problem:

# Create a function add(n)/Add(n) which returns a function that 
# always adds n to any number


def add(n):
    def adder(x):
        return x+n
    return adder

add_one=add(1)
print(add_one(3))

# it output 4