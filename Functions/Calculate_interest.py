# Problem:
# Write a function called CalculateInterest() to calculate the interest in bank savings. It 
# takes 3 parameters, the balance, interest rate and the number of withdrawals. If the 
# numbers of withdrawals are greater than 5, then the function returns the interest as 0.  
# If the number of withdrawals is equal to or less than 5 then the interest would be 
# balance into the interest rate.  

def CalculateInterest(balance,interest_rate,withdrawals):
    if withdrawals>5:
        return 0
    else:
        return interest_rate*balance


# getting user input
balance=float(input("Enter the balance:"))
interest_rate=float(input("Enter the interest rate:"))
withdrawals=int(input("Enter no of withdrawals:"))

interest=CalculateInterest(balance,interest_rate,withdrawals)
print("The interest is :",interest)


# sample output:
# Enter the balance:55000
# Enter the interest rate:0.05
# Enter no of withdrawals:2
# The interest is : 2750.0

#-------------------------------
# Enter the balance:10000
# Enter the interest rate:0.10
# Enter no of withdrawals:10
# The interest is : 0