# ----------------By codewars--------------------------

# source: 
# Problem: https://www.codewars.com/kata/53dc54212259ed3d4f00071c
# Write a function that takes an array of numbers and returns the sum of the numbers. 
# The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
# if input contains only one element, it prints that element
# If no element in the array, it returns 0 



def sum_array(numbers):
    total=0
    for i in numbers:
        total=total+i
    
    return total

numbers=[1,5,8.5,-6.9,10]
print(sum_array(numbers))  # output -> 17.6

# if numbers=[]
# output -> 0

#if numbers=[-2.398]
# output -> -2.398