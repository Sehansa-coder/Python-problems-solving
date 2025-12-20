# Write a program to requests the user to enter a number and print a pattern as follows: 

# Sample Output: 
# Enter number: 3 
# 3 3 3 
# 2 2 
# 1 


num=int(input("Enter number:"))
if num<=0:
    print("Invalid")
    exit()
# Exit from the program if invalid number<=0 is entered

for i in range(1,num+1):
    for j in range(1,num+1):
        print(num,end=" ")
    num=num-1
    print()