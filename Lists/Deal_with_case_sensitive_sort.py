
# -----------------------sorting lists-----------------

# By default the sort() method is case sensitive, resulting 
# in all capital letters being sorted before lower case letters:

# eg:
thislist=["banana","Orange","Kiwi","cherry"]
thislist.sort()
print(thislist)

# sample output:
# ['Kiwi', 'Orange', 'banana', 'cherry']
#--------------------------------------------------------------------

# To avois the above unexpected results we use str.lower as a key function

thislist.sort(key=str.lower)
print(thislist)

# sample output:
# ['banana', 'cherry', 'Kiwi', 'Orange']

#-------------------------------------------------

# reverse order regardless alphabet order

animals=["lion","cat","tiget","bat"]
animals.reverse()
print(animals)

# Like wise we can turn a list of numbers in ascending into descending
# eg:

numbers=[100,20,40,80,2]
numbers.sort()
print(numbers)
# output: [2, 20, 40, 80, 100]   -> sort function turn into ascending order
numbers.reverse()  # reverse() function can be used then to turn it into descending order
print(numbers)
# output: [100, 80, 40, 20, 2]


# ------------------------copy lists------------------------

# eg:
list_1=["Hinduism","Buddhism","Catholism","Islam"]
list_2=list_1.copy()
print(list_2)
# Assign the items in list_1 to list_2. Therefore list_2 h(as the same elements in list_1
# output: ['Hinduism', 'Buddhism', 'Catholism', 'Islam']

# another method--->

new_list=list(list_1)
print(new_list)
# output: ['Hinduism', 'Buddhism', 'Catholism', 'Islam']




