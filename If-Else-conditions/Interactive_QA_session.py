# Problem : You have a variable x = 10 and y = 5. What is the value of x + y * 2?  
# Explanation: The user gets a question and has to provide the answer.
# The system ckecks if the answer is correct and output a messege.
# This is an interactive quiz session you can have with the user


x=10
y=5
answer=int(input("What is the value of x + y * 2? : "))

if answer==30:
    print("Correct")
else:
    print("Incorrect")
