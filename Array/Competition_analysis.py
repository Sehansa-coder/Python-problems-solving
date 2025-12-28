# ( BSC In Information and Technology- Higher Diploma Year 1 question)

# Problem:
# In a Cricket tournament, there are 4 teams selected for the semifinals. The Team No and scores 
# are to be recorded in an array to do an analysis about the competition.

#|--------------------------------------|
#| Team No    | 1   | 2   |  3   |  4   |
#| Total score| 100 | 156 | 145  |180   |
#|--------------------------------------|

score=[[1,2,3,4],[100,156,145,180]]
print(score)



maximum_score=score[1][0]  # first team's score
team_no=score[0][0]        # first team's number

for i in range (1,4):      # check the rest of teams by looping
    if score[1][i]>maximum_score:
        maximum_score=score[0][i]
        team_no=score[0][i]

print(f"Team with highest total score is: Team {team_no}")

# sample output:
# [[1, 2, 3, 4], [100, 156, 145, 180]]
# Team with highest total score is: Team 4