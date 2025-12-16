# Problem: by codewars

# Source: https://www.codewars.com/kata/56f3f6a82010832b02000f38

# Explanation:
#  You are given the age (which will always be a positive integer) and does the following:
# 1. If the age is 12 or lower, print "You are a (age) kid"
# 2. If age is between 13 and 17 print "You are a (age) teenager"
# 3. If the age is between 18 and 64 print "You are a (age) adult"
# 4. If the age is above 64 print "You are a (age) elder"

age=int(input("Enter your age:"))
if age>0:
    if age<=12:
        print("You are a ",age," kid")
    elif age>=13 and age<=17:
        print("You are a ",age," teenager")
    elif age>=18 and age<=64:
        print("You are a ",age," adult")
    elif age>=65:
        print("You are a ",age," elder")
    
else:
    # print error messege because the age cannot be a minus value( less than 0)
    print("Invalid input")