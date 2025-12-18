# Problem: (W3 School) & self-generated
# Source: W3 school -> https://www.w3schools.com/python/python_if_logical.asp

# Explanation:
# Create a python program that grants access only if the user solves a challenge. The program should:
# ASsk the user a math question -> What is 2**5?
# Ask the user to enter the secret code : "PythonRock"
# Ask the user to confirm verification (yes/no)


q=int(input("What is 2**5:"))
code=str(input("Enter the secret code:"))
verification_status=str(input("Are you vertified(yes/no): "))

verification_status=verification_status.lower().strip()

if q==32 and code=="PythonRock" and verification_status=="yes":
    print("Access granted")
else:
    print("Access denied")


# .lower()  -> to convert the input th lowercase letters to make it easy
# .strip()  -> remove accidental spaces in user input

# output:
# What is 2**5: 32
# Enter the secret code: PythonRock
# Are you verified (yes/no): yes

# Access granted
#----------------------------------
# What is 2**5: 31
# Enter the secret code: PythonRock
# Are you verified (yes/no): yes

# Access denied
#--------------------------------------

# What is 2**5: 32
# Enter the secret code: python
# Are you verified (yes/no): yes

#Access denied 
# (wrong code)

#---------------------------------------
# hat is 2**5: 32
# Enter the secret code: PythonRock
# Are you verified (yes/no): no

#Access denied
# (Not vertified)