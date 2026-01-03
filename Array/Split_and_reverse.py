# Problem:
# Task:
# Write a function that takes a sentence and returns an array of words in reverse order.

# Get user input
words=str(input("Enter your sentence:"))
# Use split() function to get the elements as a list 
arr=words.split()
print("Original array :",arr)

# use reverse() function
arr.reverse()
reversed_array=arr
# Print reversed array
print("Reversed array :",arr)

# sample output:

# Enter your sentence:I love python
# Original array : ['I', 'love', 'python']
# Reversed array : ['python', 'love', 'I']