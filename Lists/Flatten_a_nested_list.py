# problem : Define a function that takes a list which may contain nested lists and returns 
# a flat list containing all elements in the same order.
# Rules:
# Use lists properly
# Order must stay the same
# No shortcuts like itertools

def flatten_list(mylist):
    # create an empty list
    flat_list=[]
    for i in mylist:
        if isinstance(i,list):
            flat_list.extend(flatten_list(i))  # extemd()- merges another list into this list element by element (break apart and merge)
             
        else:
            flat_list.append(i)

    return flat_list

# call the function
# Display the output
print(flatten_list([1,[2,[3,4],5],6]))

# sample output:
# [1, 2, 3, 4, 5, 6]