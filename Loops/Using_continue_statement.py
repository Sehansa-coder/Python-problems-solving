# Problem:
# Write a program to print the following number pattern using continue statement.

# Enter number: 6 
# 1 2 4 5 6



num=int(input("Enter number:"))

for i in range(1,num+1):
    if i==3:
        continue

    print(i,end=" ")