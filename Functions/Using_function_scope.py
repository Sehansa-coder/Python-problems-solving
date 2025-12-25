#-----------------By codewars--------------
# Problem:
# Write a function that adds from two invocations.
# All inputs will be integers.
# example - add(3)(4)  // 7

def outer_function(a):
    def inner_function(b):
        return a+b
    return inner_function

print(outer_function(3)(4))

# output -> 7