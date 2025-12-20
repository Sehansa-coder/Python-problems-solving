# ( BSC In Information and Technology- Higher Diploma Year 1 question)
# Problem:
#  program to read a number from the user and 
# print number of digits, 
# sum of digits and 
# product of digits. 


num=int(input("Enter number:"))

# Validating the number(If less than or equal to zero, it exit from the program)
if num<=0:
    print("Invalid number")
    exit()

product=1
sum=0
count=0
while num>0:
    
    remainder=num%10
    sum=sum+remainder
    product=(remainder*product)
    count+=1
    num=num//10


print(f"The number of digits: {count}")
print(f"The sum of digits is: {sum}")
print(f"The product of digits is: {product}")


# Sample Output: 
#---------------------------------
# Enter number: 1134 
# The number of digits: 4 
# The sum of digits is: 9 
# The product of digits is: 12