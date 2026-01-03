# problem by-------------------------Codewars---------------------------------

# source: https://www.codewars.com/kata/57e76bc428d6fbc2d500036d

# explanation:
# Write a function to split a string and convert it into an array of words.
# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are",  "my", "favorite"]
#------------------------------------------------------------------------------------------------------------


# Get user input
words=str(input("Enter your sentence or words:"))

# the function split() returns a list
# split() function breaks the text wherever there is a space
arr=words.split()

# print array
print(arr)

# sample output:
# Enter your sentence or words:I want to sing
# ['I', 'want', 'to', 'sing']

# Enter your sentence or words:Good
# ['Good']

