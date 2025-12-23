# BSc(Hons) Diploma Year 1 question
# Problem:
#  Write a Python program to calculate and print the area and perimeter (circumference) of a circle.

# The program should:

# Take the radius of the circle as user input.
# The function CalculateArea(radius) should calculate and return the area of the circle.
# The function CalculatePerimeter(radius) should calculate and return the perimeter (circumference) of the circle.

# In the main part of the program:
#    Call both functions
#    Print the area and the perimeter of the circle

def CalculateArea(radius):
    return 3.14*radius**2

def CalculatePerimeter(radius):
   
    return 2*3.14*radius

# Get user input
r=float(input("Enter radius:"))

area=CalculateArea(r)
print("The area of the circle is:",area)

perimeter=CalculatePerimeter(r)
print("The perimeter of the circle is:",perimeter)


# sample output:
#------------------------------
# Enter radius:3
# The area of the circle is: 28.26
# The perimeter of the circle is: 18.84