# ( BSC In Information and Technology- Higher Diploma Year 1 question)

# Problem:
# program to input a number from the user and find the number of 
# occurrences is in the entered number similar to the last digit.


num=int(input("Enter number:"))
if num<=0:
    print("Invalid number")
    exit()


remainder=num%10
occur=remainder
count=1
num=num//10

while num>0:
    remainder=num%10
    if remainder==occur:
        count+=1
    
    num=num//10

print("The last digit:",occur)
print("The number of occurrences of Last digit in given number:",count)


# Sample Output: 
# Enter number: 1323 
# The last digit is: 3 
# The number of occurrences of Last digit in given number: 2
#-----------------------------------------
# Enter number: 0
# Invalid number
#------------------------------