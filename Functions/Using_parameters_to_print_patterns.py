# ( BSC In Information and Technology- Higher Diploma Year 1 question)


# Problem:
# Write a program to implement a function called drawLinesWithRowCol() to pass the no of rows and columns as parameters. 

# use repetition structures such as for-loop structure to implement the pattern.

def drawLinesWithRowCol(row,col):
    for a in range(row):
        for b in range(col):
            print("*",end="")
        
        print()

drawLinesWithRowCol(3,11)
print()

# Rectangle with 6 rows, 15 columns
drawLinesWithRowCol(6,15)

# Output:
#  ***********
#  ***********
#  ***********

#  ***************
#  ***************
#  ***************
#  ***************
#  ***************
#  ***************
