# # ( BSC In Information and Technology- Higher Diploma Year 1 question)

# problem:

#  Write a program that reads numbers from an integer array and graph the information 
# in the form of bar chat. Sample output is given below.

# Element   Value   Histogram
# 0         19      *******************
# 1         3       ***
# 2         15      ***************
# 3         7       *******
# 4         11      ***********
# 5         9       *********
# 6         13      *************
# 7         5       *****
# 8         17      *****************
# 9         1       *



num=[]
for x in range(10):
    b=int(input(f"Enter number {x+1}:"))
    num.append(b)

print(f"Element\tValue\tHistogram")  # \t  inserts a horizontal tab space in output

for i in range(10):
    print(f"{i}\t{num[i]}\t",end="")
    # print the pattern
    for c in range(num[i]):
        print("*",end="")  # end=""  stay in the same line
    
    print() # new line
    
        
