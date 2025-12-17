# ( BSC In Information and Technology- Higher Diploma Year 1 question)
# Problem:
# Write a program to calculate and print the annual interest amount of the credit card 
# depending on the credit limit and the annual interest rate. User enters the credit card type 
# and credit limit to the program as a user input. 
# The interest rate for each card type can be determined as follows:

# --------------------------------------------
# |Card Type           | Annual interest rate|   
# |--------------------|---------------------|
# | Platinum (P)       | 20 %                |
# |Gold (G)            | 10 %                |
# | Silver (S)         | 5 %                 |

# The annual interest amount for each card type can be determined as follows 
# Annual Interest Amount= Credit Limit * Annual interest rate

card=str(input("Enter card type (P/G/S):"))
card=card.upper()
creditLimit=float(input("Enter credit limit:"))

annualInterestRate=0
if card=='P':
    annualInterestRate=0.20
elif card=='G':
    annualInterestRate=0.10
elif card=='S':
    annualInterestRate=0.05
else:
    print("Invalid card type")
    exit()

annual_interest_amount=creditLimit*annualInterestRate

print("The Annual Interest Amount:",annual_interest_amount)

# Sample Output: 
# Enter Card Type: P 
# Enter Credit Limit:50000 
# The Annual Interest Amount: 10000 


