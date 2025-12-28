# Implement a python program to calculate the sum of the content of array array1 and array2
# and store the values in a new array
array1=[]
array2=[]
sumArray=[]

print("First array")

# get input for first array
for i in range(5):
    x=int(input(f"Enter array1 number {i+1}:"))
    array1.append(x)

print("Second array")

# get inputs for second array 
for a in range(5):
    y=int(input(f"Enter array2 number {a+1}:"))
    array2.append(y)

# Sum array-sum of each two elementgs in two arrays
for n in range(5):
    sumArray.append(array1[n]+array2[n])

#print the array
print("Sum array=",sumArray)


# sample output:
#---------------------------------------
# First array
# Enter array1 number 1:10
# Enter array1 number 2:20
# Enter array1 number 3:30
# Enter array1 number 4:40
# Enter array1 number 5:50
# Second array
# Enter array2 number 1:1
# Enter array2 number 2:2
# Enter array2 number 3:3
# Enter array2 number 4:4
# Enter array2 number 5:5
# Sum array= [11, 22, 33, 44, 55]
