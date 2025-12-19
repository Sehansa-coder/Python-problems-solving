# Problem:
# program to requests the user to enter two integers as inputs and the print 
# sum of odd square numbers between the given interval.

num1=int(input("Enter number 1:"))
num2=int(input("Ennter number 2:"))

sum=0
for i in range(num1+1,num2):
    if i%2!=0:
        sum=sum+(i**2)

print(f"Sum of odd square numbers: {sum}")


# Sample output:
# Enter two integer numbers: 2 6 
# Sum of odd square numbers: 34