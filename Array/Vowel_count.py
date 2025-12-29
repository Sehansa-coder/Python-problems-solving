# problem:
# program to do the followings, 
# a) Create a char array with size 7. 
# b) Accept 7 characters and fill the array. 
# c) Count number of vowels in the array. 


letters=[]  # initialize an array

# get user input
for i in range(7):
    x=str(input(f"Enter letter {i+1}: "))
    x=x.lower()
    letters.append(x)

# Print the array of characters
print(letters)

# count vowels
count=0
for a in letters:
    if a in 'aeiou':  # simpler than using or operator
        count+=1

print("The no. of vowels in the array: ",count)

# sample output:

# Enter letter 1: o
# Enter letter 2: c
# Enter letter 3: t
# Enter letter 4: o
# Enter letter 5: p
# Enter letter 6: U
# Enter letter 7: s
# ['o', 'c', 't', 'o', 'p', 'u', 's']
# The no. of vowels in the array:  3
