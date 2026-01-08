# problem by---------------------Codewars-----------------------
# source : https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118

# explanation:
# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.
# The order of the sequence has to stay the same.

# examples:
# Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]

def remove_duplicate(mylist):
    answer_list=[]
    for i in mylist:
        if i not in answer_list:
            answer_list.append(i)

    return answer_list

# Call functions and display output
print(remove_duplicate([1,1,2]))
print(remove_duplicate([1,2,1,1,3,2]))
print(remove_duplicate([4,4,5,34,34,2,6,77,89,89]))

# sample output:
# [1, 2]
# [1, 2, 3]
# [4, 5, 34, 2, 6, 77, 89]


