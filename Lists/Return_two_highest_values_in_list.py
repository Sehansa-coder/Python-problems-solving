# problem by-------------Codewars---------------------
# source: https://www.codewars.com/kata/57ab3c09bb994429df000a4a

# explanation:
# In this kata, your job is to return the two distinct highest values in a list. 
# If there're less than 2 unique values, return as many of them, as possible.
# The result should also be ordered from highest to lowest.

# Examples:

# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []



def highest_two(mylist):
    new_list=list(set(mylist))  # set()-> removes duplicates  # list()->copies the same list 
    new_list.sort()   # turn into ascending order
    new_list.reverse()   # turn into descending order

    return new_list[:2]   # return the elements of the index 0 and 1  [:2]

mylist=[]
# get user inputs
for i in range(5):
    x=int(input(f"Enter number {i+1}:"))
    mylist.append(x)

# call function
print(highest_two(mylist))


# sample output:

# Enter number 1:3
# Enter number 2:3
# Enter number 3:3
# Enter number 4:4
# Enter number 5:1
# [4, 3]
#--------------------
# Enter number 1:2
# Enter number 2:2
# Enter number 3:2
# Enter number 4:2
# Enter number 5:2
# [2]
#--------------------
# Enter number 1:4
# Enter number 2:10
# Enter number 3:10
# Enter number 4:9
# Enter number 5:1
# [10, 9]