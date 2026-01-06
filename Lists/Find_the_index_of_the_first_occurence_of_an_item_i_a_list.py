# problem by--------------Codewars------------------------
# source: https://www.codewars.com/kata/585ba66ce08bae791b00011b
# explanation:
# Write a function index_finder/index-finder that returns the index of the first occurrence of an item (x) in the list (lst), but ignoring the first item in the list. The item will always occur at least once after the first item in the list. For example:

# lst = ['a','b','c'], x = 'b' >>> returns 1 ('b' occurs first at position 1)

# lst = ['b','b','b'], x = 'b' >>> returns 1 ('b' occurs first at position 1 if you ignore index 0)

# lst = ['b','c','b','a'], x = 'b' >>> returns 2 ('b' occurs first at position 2 if you ignore index 0)

# lst = [0,2,'a','5',0,1,0], x = 0 >>> returns 4 (0 occurs first at position 4 if you ignore index 0)




def index_finder(mylist,x):
    for i in range(1,len(mylist)):
        if x==mylist[i]:
            return i

# get user input
input_list=[]
for i in range(5):
    a=input("Enter elements : ")
    input_list.append(a)

item=input("Enter item to see occurence index :")
# call the function and display output
print(index_finder(input_list,item))

# sample output:

# Enter elements : 0
# Enter elements : a
# Enter elements : 5
# Enter elements : 0
# Enter elements : 0
# Enter item to see occurence index :0
# 3
#---------------------------

# Enter elements : b
# Enter elements : c
# Enter elements : b
# Enter elements : a
# Enter elements : x
# Enter item to see occurence index :b
# 2
#---------------------------

# Enter elements : b
# Enter elements : b
# Enter elements : b
# Enter elements : b
# Enter elements : b
# Enter item to see occurence index :b
# 1
#-----------------------------

# Enter elements : a
# Enter elements : b
# Enter elements : c
# Enter elements : d
# Enter elements : e
# Enter item to see occurence index :b
# 1