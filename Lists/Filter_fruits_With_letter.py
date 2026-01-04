# problem :---------------------------W3schools-------------------------------
# explanation:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

fruits=["apple","banana","cherry","kiwi"]
fruits_with_letter=[]
for i in fruits:
    if "a" in i:
        fruits_with_letter.append(i)

print(fruits_with_letter)

# sample output:
# ['apple', 'banana']

# The new list only get the fruits that has letter 'a' in it