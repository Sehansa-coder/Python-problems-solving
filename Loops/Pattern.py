# Problem:
#  Print the following pattern using nested loop statements. 
#  Sample Output: 
#Enter number: 3 
#  1 
#  2 2 
#  3 3 3 



num=int(input("Enter number:"))
for i in range(1,num+1):
    for a in range(i):
        print(i,end=" ")  # print on same line with space
    print()  # move to next line after inner loop



