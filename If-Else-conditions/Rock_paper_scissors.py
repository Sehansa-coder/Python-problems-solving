# Problem : Playing rock-paper-scissor game using if-else (Codewars)
# Explanation: 
# Rules of the "Rock, Paper, Scissors" game are:
#Rock beats Scissors,
# Scissors beat Paper,
# Paper beats Rock,
# Two identical moves are a draw.
#You will be given moves of rock, paper, scissors players. You have to return which player won. "Player 1 won!" for player 1, and "Player 2 won!" for player 2. In case draw return "Draw!"

player1=str(input("Player 1:"))
player2=str(input("Player 2:"))

if player1=="rock" and player2=="scissors":
    print("Player 1 won!")
elif player1=="scissors" and player2=="rock":
    print("Player 2 won!")
elif player1=="scissors" and player2=="paper":
    print("Player 1 won!")
elif player1=="paper" and player2=="scissor":
    print("Player 2 won!")
elif player1=="paper" and player2=="rock":
    print("Player 1 won!")
elif player1=="rock" and player2=="paper":
    print("Player 2 won!")
else:
    # print "draw!" if both the players put the same sign
    print("Draw!")