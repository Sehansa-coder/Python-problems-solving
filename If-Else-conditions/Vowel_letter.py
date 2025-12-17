# Problem: 
#Write a program to check whether a given letter is a vowel or a consonant.
#The program should take a single character as input.
#If the letter is a vowel (a, e, i, o, u), print “Vowel”.
#Otherwise, print “Consonant”.

#Get user input
letter=str(input("Enter a letter:"))

#Convert the input letter to lower case to accept vowel lettern in Capital
letter=letter.lower()
if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
    print("Vowel")
else:
    print("Consonant")


# Output:
#  Enter a letter: A
#  Vowel
# ---------------------
#  Enter a letter: a
#  Vowel
#-----------------------
#  Enter a letter: y
#  Constant
