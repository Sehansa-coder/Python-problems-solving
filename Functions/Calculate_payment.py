
# Problem:
#  Write a function called calPayment() to calculate and return the payment of a customer 
#  based on the item he/she purchased. The item codes and the unit price of the items are 
#  given in following table.

# |-----------------------------------------|
# |  Item code     |    price               |
# |  1             |    50                  |
# |  2             |    100                 |
# -------------------------------------------

# The item code and the quantity are parameters of the function. The main program reads 
# item code and the quantity as user inputs, calls calPayment() function and displays the 
# payment of a customer.

def calPayment(item_code,quantity):
    if item_code==1:
        return quantity*50
    elif item_code==2:
        return quantity*100
    else:
        print("Invalid item")
        return 0
        
    
    
code=int(input("Enter the item code:"))
quantity=int(input("Enter the quantity:"))

payment=calPayment(code,quantity)
print("Payment:",payment)

# sample output:
#--------------------------
# Enter the item code:2
# Enter the quantity:10 
# Payment: 1000

# Enter the item code:1
# Enter the quantity:7
# Payment: 350

# Enter the item code:5
# Enter the quantity:2
# Invalid item
# Payment: 0
