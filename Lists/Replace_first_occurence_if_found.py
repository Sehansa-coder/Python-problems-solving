# problem by-----------------PYnative-------------------
# source: https://pynative.com/python-list-exercise-with-solutions/#h-exercise-19-iterate-both-lists-simultaneously

# explanation:
# Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and 
# if it is present, replace it with 200. Only update the first occurrence of an item.


# declare list
mylist=[5,10,15,20,25,50,20]

if 20 in mylist:  # checks availability
    index=mylist.index(20)   # mylist.index(20) = returns only the first index
    mylist[index]=200   # replace

# display output
print(mylist)

# sample output:
# [5, 10, 15, 200, 25, 50, 20]
        
    