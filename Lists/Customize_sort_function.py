
# problem: Sort the list based on how close the number is to 50:

def myfunction(n):
    return abs(n-50)

# abs means absolute value(no negative consideration)
# eg: 40-50 = -10   |  but it is considered as 10

mylist=[100,120,40,15,66,55,75,2]

mylist.sort(key=myfunction)
# sort(key=myfunction) means sorting the numbers in any method that myfunction returns
print(mylist)

# sample output:
# [5, -10, 16, 25,-35,-48, 50,70 ]
#          ||
#          \/
# [55, 40, 66, 75, 15, 2, 100, 120]