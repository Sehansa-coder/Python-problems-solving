# ( BSC In Information and Technology- Higher Diploma Year 1 question)

# Problem: 

# Write a  program to calculate and print the centripetal force of planet depending on the 
#velocity and radius of circular path. User enters velocity and the radius of circular path to the 
#program as a user input.

# The centripetal force of planet is calculated as follows: 
#  f=(mv^2)/r

# f= centripetal force, 
# M = 250.74 (Constant value) , 
# v = velocity, 
# r = radius of circular path 

v=float(input("Enter velocity:"))
r=float(input("Enter radius of circular path:"))

M=250.74
f=(M*v**2)/r
print("The centripetal force of planet is:",f)

#And, the program is required to find the impact type of planet based on the centripetal force. 
#The impact types are given below. 

# ----------------------------------------
# |Centripetal force   |   Impact        |
# |--------------------|-----------------|
# |0-100               | Low impact      |
# |101-150             | Normal impact   |
# |151-200             | High impact     |
# |Above 200           | Ultra impact    |

if f>=0 and f<=100:
    print("Impact is Low impact")
elif f>=101 and f<=150:
    print("Impact is Normal impact")
elif f>=151 and f<=200:
    print("Impact is High impact")
elif f>200:
    print("Impact is Ultra Impact")
else:
    print("Invalid force")