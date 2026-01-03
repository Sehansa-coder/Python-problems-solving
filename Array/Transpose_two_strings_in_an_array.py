# Problem by-------------------------Codewars--------------------
# source: https://www.codewars.com/kata/581f4ac139dc423f04000b99

# explanation:
# You will be given an array that contains two strings. Your job is to create a 
# function that will take those two strings and transpose them, so that the strings go from top 
# to bottom instead of left to right.


def transposeTwoStrings(arr):
    word1=arr[0]
    word2=arr[1]
    # use max() function to find maximum length
    max_length=max(len(word1),len(word2))
    for i in range(max_length):

        if i<len(word1):
            char1=word1[i]
        else:
            char1=" "

        if i<len(word2):
            char2=word2[i]
        else:
            char2=" "
        
        print(char1+" "+char2)

arr=[]
for i in range(2):
    words=str(input(f"Enter word {i+1}:"))
    arr.append(words)

# call function
transposeTwoStrings(arr)

# sample output
#  Enter word 1:hi
#  Enter word 2:Python
#  h P
#  i y
#  t
#  h
#  o
#  n
#-----------------------------
#  Enter word 1:Hello
#  Enter word 2:World
#  H W
#  e o
#  l r
#  l l
#  o d


