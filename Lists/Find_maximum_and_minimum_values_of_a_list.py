# problem by--------------------Codewars-------------------------
# source: https://www.codewars.com/kata/577a98a6ae28071780000989

# explanation:
# Your task is to make two functions ( max and min, or maximum and minimum, etc., 
# depending on the language ) that receive a list of integers as input, and return the largest and 
# lowest number in that list, respectively. Each function returns one number.
# ex:
# [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
#* [42, 54, 65, 87, 0]             -> min = 0, max = 87
#* [5]                             -> min = 5, max = 5


# function to find maximum number
def maximum(mylist):
    max_number=mylist[0]
    for i in range(1,len(mylist)):
        if mylist[i]>max_number:
            max_number=mylist[i]
    
    return max_number

# function to find the minimum number
def minimum(mylist):
    min_number=mylist[0]
    for i in range(1,len(mylist)):
        if mylist[i]<min_number:
            min_number=mylist[i]

    return min_number

# get user input
number_list=[]
for i in range(5):
    x=int(input(f"Enter number {i+1} : "))
    number_list.append(x)

# display outputs
print("max = ",maximum(number_list))
print("min = ",minimum(number_list))

# sample output:

# Enter number 1 : 10
# Enter number 2 : 20
# Enter number 3 : 30
# Enter number 4 : 40
# Enter number 5 : 50
# max =  50
# min =  10