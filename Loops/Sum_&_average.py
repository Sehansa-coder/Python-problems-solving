# Problem:
# Create a program to input 5 numbers from the keyboard and print 
# the sum and the average to the screen using while-loop structure.

i=1
sum=0
while i<=5:
    num=int(input(f"Enter number {i}:"))
    sum=sum+num
    i+=1

print("Sum is:",sum)
avg=sum/5.0
print("Average is: ",avg)

# Sample output:
# ------------------------------
# Enter number 1:1
# Enter number 2:2
# Enter number 3:3
# Enter number 4:4
# Enter number 5:5
# Sum is: 15
# Average is:  3.0