# Problem by----------------------Codewars-----------------------
# Source: https://www.codewars.com/kata/545991b4cbae2a5fda000158

# explanation:
# Create a method that accepts a list and an item, and returns true if the item 
# belongs to the list, otherwise false.


def availability(mylist,item):
    for i in range(len(mylist)):
        if item in mylist:
            return True
        else:
            return False

# get user inputs      
number_list=[]
for x in range(10):
    a=int(input(f"Enter number {x+1}:"))
    number_list.append(a)

item=int(input("Enter your item : "))

# call the function
print(availability(number_list,item))


# sample output:

# Enter number 1 :2
# Enter number 2 :4
# Enter number 3 :8
# Enter number 4 :6
# Enter number 5 :10
# Enter number 6 :12
# Enter number 7 :14
# Enter number 8 :16
# Enter number 9 :18
# Enter number 10 :20
# Enter your item : 11
# False
#------------------------
# Enter number 1 :2
# Enter number 2 :4
# Enter number 3 :6
# Enter number 4 :8
# Enter number 5 :10
# Enter number 6 :12
# Enter number 7 :14
# Enter number 8 :16
# Enter number 9 :18
# Enter number 10 :20
# Enter your item : 8
# True
