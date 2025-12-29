# problem:
# program to complete following tasks: 
# Declare a one-dimensional array to store 10 integer numbers. 
# Get user input to load the array and print the values stored in an array. 
# The program should replace all even numbers by 0 and odd numbers by 1. 
# Count and print number of odd values and even values in an array. 
# Finally print the array elements after replacing the values with 1 and 0.


num=[]
for i in range(10):
    x=int(input(f"Enter number {i+1} : "))
    num.append(x)

print(num)  # print the array

odd_count=0
even_count=0

for i in range(10):
    if num[i]%2==0:
        num[i]=0
        even_count+=1  # counting even numbers
    else:
        num[i]=1
        odd_count+=1   # counting odd numbers

print("Odd numbers: ",odd_count)
print("Even numbers: ",even_count)

print(num)  # printing new array with 0 and 1

# sample output:
# Enter number 1 : 10
# Enter number 2 : 35
# Enter number 3 : 86
# Enter number 4 : 57
# Enter number 5 : 38
# Enter number 6 : 9
# Enter number 7 : 46
# Enter number 8 : 93
# Enter number 9 : 100
# Enter number 10 : 51
# [10, 35, 86, 57, 38, 9, 46, 93, 100, 51]
# Odd numbers:  5
# Even numbers:  5
# [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]


