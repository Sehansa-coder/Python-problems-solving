# ( BSC In Information and Technology- Higher Diploma Year 1 question)

# Problem:
# Write a program to check whether a triangle can be formed by the given value for the angles.
# Hint: To form a triangle sum of angles should be 180. 

a=float(input("Enter angle 1:"))
b=float(input("Enter angle 2:"))
c=float(input("Enter angle 3:"))

if a+b+c==180.0:
    print("The triange is valid")
else:
    print("The triangle is not valid")


# Sample Output: 
# Enter angle 1: 40
# Enter angle 2: 55
# Enter angle 3: 65
# The triangle is not valid. 