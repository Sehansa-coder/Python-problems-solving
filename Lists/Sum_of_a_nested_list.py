# problem:--------------Codewars----------------------------------
# source: https://www.codewars.com/kata/5a15a4db06d5b6d33c000018

# explanation:
# Implement a function to calculate the sum of the numerical values in a nested list. 
# For example :
# sum_nested([1, [2, [3, [4]]]]) -> 10

def sum_of_list(mylist):
    total=0
    for item in mylist:
        if isinstance(item,list):
            total+=sum_of_list(item)
        else:
            total+=item

    return total

# Call the function and display output
print(sum_of_list([1,[2,[3,[4]]]]))
print(sum_of_list([10,[20],[30,40],50,60,[70,80,90],100]))

# sample output:
# 10
# 550