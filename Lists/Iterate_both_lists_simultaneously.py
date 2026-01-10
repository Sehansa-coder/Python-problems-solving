# problem by-----------------PYnative-------------------------
# source : https://pynative.com/python-list-exercise-with-solutions/#h-exercise-19-iterate-both-lists-simultaneously

# Explanation:
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original 
# order and items from list2 in reverse order.


def iterate(list1,list2):
    for a,b in zip(list1,reversed(list2)):  # zip() - walks both lists together
        print(a,b)
    

listone=[10,20,30,40]
listtwo=[100,200,300,400]

# call the function 
iterate(listone,listtwo)

# sample output:
# 10 400
# 20 300
# 30 200
# 40 100