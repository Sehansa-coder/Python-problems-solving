# problem by---------------------PYnative-------------------------
# source : https://pynative.com/python-list-exercise-with-solutions/#h-exercise-19-iterate-both-lists-simultaneously

# explanation:
# Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List

# Given:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Expected output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
#---------------------------------------------------------------------------------------------------------

# declare the list
mylist=[10,20,[300,400,[5000,6000],500],30,40]

# mylist[0] = 10
# mylist[1] = 20
# mylist[2] = [300, 400, [5000, 6000, 7000], 500]
# Therefore -----------------------------
# mylist[2][0] = 300
# mylist[2][1] = 400
# mylist[2][2] = [5000,6000]  -> here we append/ add the new item -7000

mylist[2][2].append(7000)
print(mylist)

# sample output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
