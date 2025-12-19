# Problem:
# A program is required to read a number from the user and check whether that number is palindrome or not. 
# Any number is said to be a palindrome if the original number and the reverse of the 
# original number are the same



num=int(input("Enter number:"))
original=num
answer=0

while num>0:
    remainder=num%10
    answer=answer*10+remainder
    num=num//10
    # we use // which is the integer division (7//2 ->3).
    # If we use 7/2, it will give 3.5
    # Or if 4/2, it gives 2.0 in float format

print("The reverse of the number is ",answer)
if answer==original:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")


# Sample Output:
#-------------------------------------- 
# Enter a number: 121 
# The reverse of the number is: 121 
# The number is a palindrome.