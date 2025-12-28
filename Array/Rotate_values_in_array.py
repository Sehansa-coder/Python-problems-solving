# ( BSC In Information and Technology- Higher Diploma Year 1 question)

# problem:
# to create an integer array called Motion of size 5. Ask the user to enter values to the array from the keyboard. Rotate the 
# values of the array by one 
# Ex: number in index 4 should move to index 3, Number in index 3 
# position in the forward direction and display the values in another array called result.
# should move to index2, number index 0 should move to index 4. 
#  ---------------------------------------
#  |  initial values  | 10 6 8 2 9       |
#  |  After rotating  | 6 8 2 9 10       |
#  ---------------------------------------



motion=[]
for i in range(5):
    x=int(input(f"Enter number {i+1} :"))
    motion.append(x)

print(motion)

result=[0]*5

result[4]=motion[0]

for b in range(1,5):
    result[b-1]=motion[b]

print(result)

#-----------------------------------------------
# to fill an array use                         |
# -motion=[]                                   |
# - motion.append(x) method or use             |
#                                              |
# motion=[0]*5 method to get spaces in array   |
#-----------------------------------------------

# sample output
#--------------------
# Enter number 1 :10
# Enter number 2 :6
# Enter number 3 :8
# Enter number 4 :2
# Enter number 5 :9
# [10, 6, 8, 2, 9]
# [6, 8, 2, 9, 10]