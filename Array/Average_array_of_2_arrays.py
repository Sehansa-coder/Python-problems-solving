# Problem: By --------------------Codewars-------------------------------
# source: https://www.codewars.com/kata/596f6385e7cd727fff0000d6

# Explanation:
# Create a function that takes a 2D array as an input, and outputs another array that contains the average values for the numbers in the nested arrays at the corresponding indexes.
# Note: the function should also work with negative numbers and floats.


def FindAverageArray(rows,cols):
    num=[]
    for i in range(rows):
        row2=[]
        for j in range(cols):
            x=int(input(f"Enter number [{i}][{j}] : "))
            row2.append(x)
        num.append(row2)
    # display the input array
    print(num)

    # create average array
    avg_array=[]
    for s in range(cols):
        total=0
        for a in range(rows):
            total+=num[a][s]
        avg_array.append(total/rows)
    # display the average array
    print(avg_array)


# get rows and columns by user input
rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))
# call the function
FindAverageArray(rows,cols)

# sample output:
# Enter number of rows:2
# Enter number of columns:4
# Enter number [0][0] : 1
# Enter number [0][1] : 2
# Enter number [0][2] : 3
# Enter number [0][3] : 4
# Enter number [1][0] : 5
# Enter number [1][1] : 6
# Enter number [1][2] : 7
# Enter number [1][3] : 8
# [[1, 2, 3, 4], [5, 6, 7, 8]]
# [3.0, 4.0, 5.0, 6.0]
#---------------------------------

# Enter number of rows:4
# Enter number of columns:5
# Enter number [0][0] : 2
# Enter number [0][1] : 3
# Enter number [0][2] : 9
# Enter number [0][3] : 10
# Enter number [0][4] : 7
# Enter number [1][0] : 12
# Enter number [1][1] : 6
# Enter number [1][2] : 89
# Enter number [1][3] : 45
# Enter number [1][4] : 3
# Enter number [2][0] : 9
# Enter number [2][1] : 12
# Enter number [2][2] : 56
# Enter number [2][3] : 10
# Enter number [2][4] : 34
# Enter number [3][0] : 67
# Enter number [3][1] : 23
# Enter number [3][2] : 1
# Enter number [3][3] : 88
# Enter number [3][4] : 34
# [[2, 3, 9, 10, 7], [12, 6, 89, 45, 3], [9, 12, 56, 10, 34], [67, 23, 1, 88, 34]]
# [22.5, 11.0, 38.75, 38.25, 19.5]