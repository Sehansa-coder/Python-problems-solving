# problem by---------------------PYnative----------------------------
# source : https://pynative.com/python-list-exercise-with-solutions/#h-exercise-19-iterate-both-lists-simultaneously

# explanation:
# Extend nested list by adding the sublist
# You have given a nested list. Write a program to extend it by adding the 
# sublist ["h", "i", "j"] in such a way that it will look like the following list.

# declare lists
main_list=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
sub_list=["h","i","j"]

# by using extend() we can add each item of another iterable list/tuple/string to the end of a list
# if we use append(), it becomes ['f', 'g', ['h', 'i', 'j']]

main_list[2][1][2].extend(sub_list)
print(main_list)


# sample output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']