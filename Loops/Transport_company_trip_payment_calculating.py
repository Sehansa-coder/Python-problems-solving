# Problem: 
# ( BSC In Information and Technology- Higher Diploma Year 1 question)


# Explanation:
# A program is needed for Black Cabs Transport Company, to calculate the total amount a particular 
# customer should pay for a given trip. The services provided by the cab service company are listed 
# below.

# ---------------------------------------------
# |Package No   |   Package Name              |
# |-------------|-----------------------------|
# | 1           |  Comfort journey            |
# | 2           |  Budget cab journey         |
# | 3           |  Crowded journey-Dual A/C   |
# | 4           |  Crowded journey-Single A/C |

# For comfort Journey package, Rs.150.00 is charged for the first kilometer and for each additional kilometer, Rs.175.00 will be charged. 
# For a Budget cab Journey package each kilometer is charged at Rs. 100.00.
# For a Crowded Journey – Dual A/C package the first kilometer is charged at Rs. 130.00 and each remaining kilometer is charged at Rs.150.00. 
# For a Crowded Journey – Dual A/C package the first kilometer is charged at Rs. 130.00 and each remaining kilometer is charged at Rs.150.00. 

# Write a program to input the package no and total distance of the tour in Kilometers through the keyboard. The program should display corresponding total amount that the customer has to pay. 
# (Hint: use nested selection statements.) 
# Ex: Package No: 2 
# Total Distance: 5 Km 
# Total Amount: Rs. 500 

# Modify your program to display an error message “Invalid Package Number!!!” if the user inputs a wrong package number. 

# Modify the program to handle many customers. After displaying the total amount to pay 
# by the first customer, your program should display the prompt “Do you have more 
# customers?” If the user inputs “y” or “Y”, program should ask for the package no and 
# total distance of the next customer. If the user inputs “n” or “N” program should 
# terminate.

i=1
while i<10:
    packageNo=int(input("Package No:"))
    distance=float(input("Total Distance:"))

    totalAmount=0
    if distance>0:
        if packageNo==1:
                totalAmount=(1*150.0)+(distance-1)*175.0
        elif packageNo==2:
            totalAmount=distance*100.0

        elif packageNo==3:
            totalAmount=(1*130.0)+(distance-1)*150.0
        elif packageNo==4:
            totalAmount=(1*120.0)+(distance-1)*130.0
        else:
            print("Invalid package number")
            continue
    else:
        print("Invalid distance")

    print("Total amount to pay:",totalAmount)

    answer=str(input("Do you have more customers(y/n):"))
    if answer!="y" and answer!="Y":
         break
    

# Sample output:
# ----------------------------------------
# Package No: 2 
# Total Distance: 5 Km 
# Total Amount: Rs. 500
# Do you have more customers(y/n):y
# Package No: 1
# Total Distance: 1 Km 
# Total Amount: Rs. 150
