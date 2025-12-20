# Write a program to requests the user to enter a number and print a pattern as follows: 

# Sample Output: 
# Enter number: 3 
# 1 
# 1 2 
# 1 2 3


num=int(input("Enter number:"))
if num<=0:
    print("Invalid")
    exit()

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()