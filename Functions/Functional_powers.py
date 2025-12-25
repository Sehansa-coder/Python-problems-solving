# Problem: <self-generated>
# Create a function power(n) that returns another function.
# The returned function should take a number x and return x raised to
# the power n.

def power(n):
    # the function that returns the value
    def base(x):

        # returns the value
        return x**n
    return base

square=power(5)
square(2)
print(square(2))

# The output is 32 [(2**5)=32]
