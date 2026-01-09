# problem by-------------------PYnative---------------------
# source : https://pynative.com/python-list-exercise-with-solutions/#h-exercise-17-concatenate-two-lists-index-wise

# explanation:
# Write a program to add two lists index-wise. Create a new list that contains the 0th index 
# item from both the list, then the 1st index item, and so on till the last element. 
# any leftover items will get added at the end of the new list.


def concatenate(list1,list2):

    answer_list=[]
    # find the smaller length of the two lists
    # this ensures we only loop over indexes that exist in both lists
    min_len=min(len(list1),len(list2))
    
    for i in range(min_len):
        # concatenate items
        answer_list.append(list1[i]+list2[i])

    # add leftover items from list1 , if any
    answer_list.extend(list1[min_len:])

    # add leftover items from list2, if any
    answer_list.extend(list2[min_len:])
    
    # return the final concatenated list
    return answer_list

# call the function and display output
print(concatenate(["m","na","i","Ke"],["y","me","s","lly"]))

# lists have different lengths
print(concatenate(["h","b","c"],["y"]))

# sample output:
# ['my', 'name', 'is', 'Kelly']
# ['hy', 'b', 'c']
