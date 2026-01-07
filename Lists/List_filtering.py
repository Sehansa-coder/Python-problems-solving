# problem by-------------------------Codewars------------------------
# source: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

# explanation:
# In this kata you will create a function that takes a list of non-negative 
# integers and strings and returns a new list with the strings filtered out.
# Example
# filter_list([1,2,'a','b']) == [1,2]

def filter_list(my_list):
    new_list=[]
    for item in my_list:
        if type(item)==int:
            new_list.append(item)

    return new_list

# get user input
mylist=[]
for i in range (5):
    x=input("Enter a string or an integer : ")

    if x.isdigit():    # checks if the input is a number
        x=int(x)       # convert to integer
    mylist.append(x)

# call function and display the result
print(filter_list(mylist))


# sample output

# Enter a string or an integer : 1
# Enter a string or an integer : 2
# Enter a string or an integer : a
# Enter a string or an integer : b
# Enter a string or an integer : 3
# [1, 2, 3]
#-----------------------------------

# Enter a string or an integer : 1
# Enter a string or an integer : aasf
# Enter a string or an integer : 123
# Enter a string or an integer : '123'
# Enter a string or an integer : 2
# [1, 123, 2]
#-------------------------------------

# Enter a string or an integer : 1
# Enter a string or an integer : 2
# Enter a string or an integer : acd
# Enter a string or an integer : -2
# Enter a string or an integer : 5
# [1, 2, 5]