# Problem: Write a Python program that:
# Takes a number n
#Checks whether the number is positive, negative, or zero
#Uses a ternary operator to assign the result to a variable called result
#Prints the result
# Format: 

# value_if_true if condition else value_if_false


n=int(input("Enter number:"))

result="Positive" if n>0 else "Negative" if n<0 else "Zero"
print(result)

# It uses nested ternary operator