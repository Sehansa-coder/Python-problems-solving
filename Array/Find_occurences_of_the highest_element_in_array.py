# Problem:
# Given an array (list in Python) of integers, find all index positions of the largest number in the array and return them as a list.
# If the array is empty, return [].


def find_max_indexes(arr):
    if not arr:
        return []
    
    # find highest element
    i=0
    highest=arr[i]
    for i in range(1,len(arr)):
        if arr[i]>highest:
            highest=arr[i]
    print("Highest elemet:",highest)
        

    index_array=[]
    index=0
    for i in range(len(arr)):
        if arr[i]==highest:
            index=i
            index_array.append(index)
    
    return index_array

# get user input
arr=[]
for x in range(5):
    num=int(input(f"Enter element [{x}]:"))
    arr.append(num)

print(arr)

print(find_max_indexes(arr))

# sample output:

# Enter element [0]:1
# Enter element [1]:3
# Enter element [2]:7
# Enter element [3]:7
# Enter element [4]:2
# [1, 3, 7, 7, 2]
# Highest elemet: 7
# [2, 3]