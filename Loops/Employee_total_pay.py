# Problem:
# Exercise 05: Create a program using the while structure to read the name of 
# an employee (terminal input). If the name is not equal to ‘END’ then it read the number of hours 
# worked and the rate per hour. Then program calculate the total pay and print the total pay. This 
# process is repeated until the name read is equal to “END”.


name=str(input("Enter employee name(END to stop):"))
while name!="end" and name!="END":
    hours=int(input("Enter no of hours worked:"))
    rate=float(input("Enter rate per hour:"))

    total=hours*rate
    print(f"Total payment: {total:.2f}")   # :.2f makes to 2 decimal places

    name=str(input("Enter next employee name:"))


# Smple output:
# Enter employee name(END to stop):henry
# Enter no of hours worked:10
# Enter rate per hour:500.20
# Total payment: 5002.00
# Enter next employee name:end
# ----------Program ends----------