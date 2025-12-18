# ( BSC In Information and Technology- Higher Diploma Year 1 question)
# Problem:
# Create a program called Ex04.cpp to input a list of positive numbers from the 
# keyboard and find the average. The list is terminated with the value -99 (Sentinel input value).


num=int(input("Enter a positive number(-99 to stop):"))

sum=0
count=0
while num!=-99:
    if num>0:
        sum=sum+num
        count+=1
    else:
        print("Negative number. Enter again")
    num=int(input("Enter next value:"))


# If the count is 0, dividing by zero will result in an error
if count>0:
    avg=sum/count
    print("Average is:",avg)
else:
    print("No positive numbers entered")


# Sample output:
# ----------------------------------------------
# Enter a positive number(-99 to stop):10
# Enter next value:2
# Enter next value:-3
# Negative number. Enter again
# Enter next value:-99
# Average is: 6.0