# Problem:
# Write a program to take a number from the user and print the pattern as follows: 

# Sample Output: 
# Enter number: 3 
# 3 2 1 



num=int(input("Enter number:"))

i=1
while i<=num:
    print(num,end=" ")
    num-=1