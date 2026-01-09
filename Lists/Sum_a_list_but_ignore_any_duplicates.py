# problem by --------------------Codewars--------------------
# source : https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2

# Explanation : 
# Please write a function that sums a list, but ignores any duplicated items in the list.
# For instance, for the list [3, 4, 3, 6] the function should return 10,

def unique_sum(mylist):
    total=0
    for item in mylist:
        if mylist.count(item)==1:
            total+=item

    return total

# call the function and display output

print(unique_sum([3,4,3,6]))   # unique values = 3  -> remain=[4,6]
print(unique_sum([1,10,3,10,10]))  # unique values = 10   -> remain=[1,3]
print(unique_sum([2,8,8,9,9,1,10,10]))  # unique values = 8,9,10   -> remain=[2,1]

# sample output:
# 10
# 4
# 3
    
