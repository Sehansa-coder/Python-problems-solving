# Problem: By HackerRank

# source: https://www.hackerrank.com/challenges/py-if-else/problem?utm_source=chatgpt.com

# Explanation:
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# n>=1 and n<=100

n=int(input("Enter a number:"))

if n>=1 and n<=100:
    if n%2!=0:
        print("Weird")
    elif n%2==0:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")
else:
    print("Invalid number")





