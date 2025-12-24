#----------By Codewars-------------
# source: https://www.codewars.com/kata/57cded7cf5f4ef768800003c
# The question is modified

# Problem:

# Takes a number(like 10,255)-base 10
# Takes a base(either 'bin' for binary or 'hex' for hexadecimal)
# converts number from decimal tselected base
# returns the result as a string
# Also if something goes wrong, return
#  - "Invalid number input"
#  - "Invalid base input"

def base_conversion(number,base):
    try:
        number=int(number)
    except ValueError:
        return "Invalid number input"
    
    
    if base=="hex":
        return hex(number)[2:]  # [2:]-> remove the front two elements in "0xff"= "ff"
    elif base=="bin":
        return bin(number)[2:]
    else:
        return "Invalid base input"
    

print(base_conversion("abc","oct"))

# sample output:
# number was given as 10 and base was given as "bin" ->output= 1010
# number was given as 255 and base was given as "hex" -> output = ff
# number was given as 10 and base was given as "oct" ->output= "Invalid base input"
# number was given as "abc" and base was given as "bin" ->output= "Invalid number input"


