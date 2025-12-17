# Problem: Write a C++ program to calculate the average mark of 3 subjects entered by user. 
# Then program should check whether the status of the student (Pass/Fail) based on the following criteria. 
# Averangemark >=50 - Pass
# Averangemark <50 - Fail


mark1=float(input("Enter makr 1:"))
mark2=float(input("Enter makr 2:"))
mark3=float(input("Enter makr 3:"))

sum=0
avg=0
sum=mark1+mark2+mark3
avg=sum/3

print("The average mark is:",avg)

if avg>=50:
    print("Pass")
else:
    print("Fail")


# Output:
# Enter mark 1:70
# Enter mark 1:60
# Enter mark 1:65
# Average mark: 65.0 
# Status: Pass 

