# problem by------------------------------Codewars----------------------------------
# source: https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef

# explanation:
# Christmas is coming, and Santa has a long list to go through, to find who deserves 
# presents for the big day. Go through a list of children, and return a list containing every 
# child who appeared on Santa's list. Do not add any child more than once. Output should be sorted.

# Comparison should be case sensitive and the returned list should contain only one copy 
# of each name: "Sam" and "sam" are different, but "sAm" and "sAm" are not.


def santaGift(children_list):
    new_list=[]
    for i in children_list:
        if i not in new_list:
            new_list.append(i)

    return sorted(new_list) # since the question ask the output list shouls be sorted

# call function and display output
print(santaGift(["Sam","sam","seha","seha","clEo","clEo"]))

# sample output : 
# ['Sam', 'clEo', 'sam', 'seha']