# Problem:
# Various software companies charge various prices to implement systems based on their 
# experience and skill. The following figure illustrates the amounts bid by 10 software 
# companies (A-J) to implement a corporate web site. 
# Note: The amounts are in millions.

# |-----------------------------------------------------------------------|
# | Software company | A  | B | C |  D  |  E  | F | G   | H   | I   | J   |
# | Bid              | 10 |8  |15 |14   |12.5 |11 | 9.8 | 9.6 | 11  | 10.5|
# |-----------------------------------------------------------------------|

# Write a program to read and store above figures in one dimensional array. It should 
# calculate the average bid and count how many companies have bid less than the 
# average bid. 


company_bid=[10,8,15,14,12.5,11,9.8,9.6,11,10.5]

total=0

for i in range(10):
    total=total+company_bid[i]

avg_bid=total/10
print("Average bid (millions) : ",round(avg_bid,2))

count=0
for x in range(10):
    if company_bid[x]<avg_bid:
        count+=1

print("Number of companies that has bid less than the average bid : ",count)

# sample output:
# Average bid (millions) :  11.14
# Number of companies that has bid less than the average bid :  7