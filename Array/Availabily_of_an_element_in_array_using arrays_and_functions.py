# problem:
# Provided is a function which accepts two parameters in the following order: array, element and returns the index of 
# the element if found and "Not found" otherwise. Your task is to shorten the code as much as possible in order to meet the character count 
# requirements of the Kata.



def availability(arr,element):
    if element in arr:
        return "Index=",arr.index(element)
            
    else:
        return "Not found"
   
    
        
array=[]
for i in range(5):
    x=int(input(f"Enter number {i+1}:"))
    array.append(x)

element=int(input("Enter your element:"))

answer=availability(array,element)
print(answer)

# sample output:

# Enter number 1:15
# Enter number 2:30
# Enter number 3:45
# Enter number 4:100
# Enter number 5:70
# Enter your element:100
# ('Index=', 3)
#----------------
# Enter number 1:1
# Enter number 2:3
# Enter number 3:5
# Enter number 4:7
# Enter number 5:9
# Enter your element:10
# Not found