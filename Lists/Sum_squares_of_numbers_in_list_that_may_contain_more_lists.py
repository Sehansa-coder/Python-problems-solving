# problem by--------------------Codewars---------------------------------
# source : https://www.codewars.com/kata/57882daf90b2f375280000ad

# explanation:
# Write a function that sums squares of numbers in list that may contain more lists


def SumSquares(mylist):
    total=0

    for i in mylist:
        if isinstance(i,list):   # isinstance()- checks whether the i is a list
            total+=SumSquares(i)
        else:
            total+=(i*i)

    return total


# call function and display output
print(SumSquares([1,2,3]))              # (1*1)+(2*2)+(3*3)= 1+4+9 =14
print(SumSquares([[1,2],3])) 
print(SumSquares([[[[[[[[1]]]]]]]]))    # (1*1) = 1
print(SumSquares([10,[[10],10],[10]]))  # (10*10)+(10*10)+(10*10)+(10*10) = 100+100+100+100 = 400

# sample output:
# 14
# 14
# 1
# 400
