# ( BSC In Information and Technology- Higher Diploma Year 1 question)

# Write a program to calculate and print the BMI (Body Mass Index) value of the person 
# depending on the height and the weight of the person. The user enters the height and the 
# weight of the person to the program as user input. 

# The BMI of the person is calculated as follows:
# bmi=w/h^2
# w=weight, h=height
# And, the program is required to find the category of a person based on the BMI value. The 
# categories are given below. 

# ----------------------------------------
# |BMI Value           |  Category       |
# |--------------------|-----------------|
# |0-18.5              | under weight    |
# |18.6-25             | healthy weight  |
# |26-30               | over weight     |
# |Above 30            | obese           |

w=float(input("Enter weight:"))
h=float(input("Enter height:"))

bmi=w/h**2        # calculating bmi value
bmi=round(bmi,3)  # Round off to 3 decimal places
print("The BMI value of person is: ",bmi)

if bmi>=0 and bmi<=18.5:
    print("The Category is under weight")
elif bmi>=18.6 and bmi<=25:
    print("The Category is Healthy Weight")
elif bmi>=26 and bmi<=30:
    print("The Category is over weight")
elif bmi>30:
    print("The Category is obese")
else:
    print("Invalid bmi value")
    exit()  


# Sample Output: 
# Enter weight: 65.0 
# Enter Height: 1.76 
# The BMI value of person is: 20.984
# The Category is Healthy Weight 