# Problem by:----------------Codewars----------------------------
# Source: https://www.codewars.com/kata/5583090cbe83f4fd8c000051

# explanation:
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example (Input => Output):
# 35231 => [1,3,2,5,3]
# 0   => [0]

# get user input
num=int(input("Enter number:"))
reversed=[]


if num==0:
    reversed.append(num)
else:
    while num>0:
        digit=num%10
        reversed.append(digit)
        num=num//10


print(reversed)

# sample output:
# Enter number:35231
# [1, 3, 2, 5, 3]

# Enter number:0
# [0]

# Enter number:1234
# [4, 3, 2, 1]