# ------------------ By Codewars-------------
# source: https://www.codewars.com/kata/563a631f7cbbc236cf0000c2

# Problem:
# In this game, the hero moves from left to right. The player rolls the die and moves the number of spaces indicated by the die two times.

# Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.
# Example: move(3, 6) should equal 15

# It means correny position+ roll +roll


def move_hero(current_position,roll):
    return current_position+(roll+roll)

current_position=int(input("Enter current position: "))
roll=int(input("Enter rolled value:"))
print(move_hero(current_position,roll))

# sample output:
# Enter current position: 3
# Enter rolled value:6
# 15
