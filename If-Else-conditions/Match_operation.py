# Problem: (W3 school)
# Source: W3 school -> https://www.w3schools.com/python/python_if_logical.asp

# Using match operator as a alternative for if-else statement

day=int(input("Enter a number 1-7:"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input day")

# Another format to use match operator
match day:
    case 1|2|3|4|5:
        print("I love weekdays")
    case 6|7:
        print("I love weekends")
    case _:
        print("No match")

# Adding extra conditions
month=5
match day:
    case 1|2|3|4|5 if month==5:
        print("A weekday in May")
    case 6|7 if month==5:
        print("A weekend day in May")
    case _:
        print("No match")

# Output :
# Enter a number 1-7:6
# Saturday
# I love weekends
# A weekend day in May