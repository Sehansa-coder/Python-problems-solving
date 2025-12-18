# Problem:
# Write a Python program that:
# Takes an integer units (electricity units consumed)
# Calculates the total bill amount based on the rules below
#Uses ternary operator(s) to perform the calculation
#Prints the final bill

# Getting user input(units)
units=int(input("Enter no of electricity units consumed:"))

# Calculating total bill
bill=(units*5) if units<=100 else (100*5)+(units-100)*8
#Output bill
print("Total bill=",bill)


# Example Outputs
# Input: 80
# Output: Total Bill = 400

# Input: 120
# Output: Total Bill = 660