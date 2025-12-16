# Problem : Check a certain word is included in the given text of the user input

# Explanation:
# Write a Python program that asks the user to enter a sentence.  
#If the sentence contains the word "Python", 
# print:  "This sentence is about Python."  
# Otherwise, 
# print: "This sentence is not about Python."



# convert the letters of the required word "Python" into lowercase letters to make it easy -> "Python".lower()
# convert the letters of the input sentence into lowercase letters -> text.lower

text=str(input("Enter your sentence:"))  # get the user input
if("Python".lower() in text.lower()):
    print("This sentence is about Python.")
else:
    print("This sentence is not about Python.")


# Example run:
# Enter your sentence: I love PYTHON programming
# Output: This sentence is about Python.