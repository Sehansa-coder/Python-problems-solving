# problem: 

# Task: Calculate the final price of an item after discount.
# Rules:
# Price > $100 → 20% discount.
# Price ≤ $100 → 10% discount.

# Functions:
# readInputs() → Read item name and price.
# calculateDiscount() → Calculate discount amount.
# printBill() → Show item name, discount, and final price.


# Define global variable
item_name=""
price=0
final_price=0
discount=0

def readInputs():
    global item_name,price

# get user input
    item_name=str(input("Enter item name:"))
    price=float(input("Enter price:"))

def calculateDiscount():
    global price,final_price,discount

    if price>100:
        discount=0.20
        final_price=price-(price*discount)
    elif price<=100 and price>0:
        discount=0.10
        final_price=price-(price*discount)
    else:
        print("Invalid price")
        exit()

def printBill():
    global final_price,item_name,discount

# print the outputs
    print("Item name: ",item_name)
    print("Discount=",discount*100,"%")
    print("Final price: ",final_price)


# call the functions
readInputs()
calculateDiscount()
printBill()


# sample output:
# Enter item name:soap
# Enter price:30
# Item name:  soap
# Discount= 0.1
# Final price:  27.0
#---------------------------

# Enter item name:noodles
# Enter price:300
# Item name:  noodles
# Discount= 20.0 %
# Final price:  240.0
#----------------------------

# Enter item name:shampoo
# Enter price:-20
# Invalid price