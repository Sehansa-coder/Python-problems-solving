# Write a program to read a number and print factorial of the given number.



answer=1
num=int(input("Enter number:"))

for i in range(1,num+1):
    answer=answer*i

print(f"Factorial of number {num} is {answer}")


# Sample Output: 
#-----------------------
# Enter number: 4 
# Factorial is: 24