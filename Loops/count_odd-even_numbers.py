# Problem:
# Write a C++ program to prompt the user to enter a set of numbers (only positive numbers), 
# one at a time. User enters a zero to indicate that he has completed entering numbers. 
# Then, the program should display 
# • the count of odd numbers entered. 
# • the count of even numbers entered.

even=0
odd=0
num=int(input("Enter positive number(0 to stop):"))
while num!=0:
    if num>0:
        if num%2==0:
            even+=1
        else:
            odd+=1
    else:
        print("Invalid number")
    
    num=int(input("Enter next number:"))

print("Even count:",even)
print("Odd count:",odd)

# sample output:
#-------------------------------------------
# Enter positive number(0 to stop):2
# Enter next number:3
# Enter next number:-2
# Invalid number
# Enter next number:4
# Enter next number:0
# Even count: 2
# Odd count: 1