# Problem: Calculating the sum of three input numbers if all the numbers are equal.
# Then printing the thrice of their sum.
# Print error messege if the inputs are not equal

num1=int(input("enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

# Check whether the numbers are equal to each other
if num1==num2==num3:
    # calculating the sum
    sum=num1+num2+num3
    print("Sum is:",sum)
    print("Thrice of sum: ",3*sum)   # 3*sum is multiplying the sum by 3 to get the thrice of it
else:
    print("The input numbers are not equal")   # error messege
