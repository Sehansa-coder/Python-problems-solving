# problem by: --------------Codewars---------------
# source: https://www.codewars.com/kata/59a9919107157a45220000e1
# explanation:
# Given an array (a list in Python) of integers and an integer n, find all occurrences of n in the given array and return another array containing all the index positions of n in the given array.
# If n is not in the given array, return an empty array [].
# Assume that n and all values in the given array will always be integers.

# Example:
# [6, 9, 3, 4, 3, 82, 11]
# input number is 3
#  [2, 4]

arr=[6,9,3,4,3,82,11,3,9]

# get user input
num=int(input("Enter number:"))
index_array=[]
index=0

for i in range(len(arr)):
    if arr[i]==num:
        index=i
        index_array.append(index)

print(index_array)

# sample output:

# Enter number:3
# [2, 4, 7]

# Enter number:9
# [1, 8]

# Enter number:100
# []