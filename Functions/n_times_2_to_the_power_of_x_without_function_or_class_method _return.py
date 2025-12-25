#------------By Codewars---------------------------
# source: https://www.codewars.com/kata/57b971f68f58135e840001cc

# Problem:
# Your goal is to create something called puzzle which is equivalent 
# to function n_time2_power_x(n, x) (see below) where n and x are positive integers.

# IMPORTANT: puzzle must not be a function or method and your solution mustn't contain return keyword.

n=2
x=5
def n_time2_power_x(n,x):
    return n*2**x

puzzle=n<<x
print(puzzle)

# How this works?
# << means left shift
# Each left shift:
# - Multiply the number by 2
# so, 
# 2<<1 ->4
# 2<<2 ->8
# 2<<5 ->64
# same result as n*2**x
# But function is not used here. Just for clarification


# Output:
# 64