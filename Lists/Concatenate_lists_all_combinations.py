# problem by----------------PYnative--------------------
# source: https://pynative.com/python-list-exercise-with-solutions/#h-exercise-17-concatenate-two-lists-index-wise

# explanation:
# Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']



def concatenate(list1,list2):
    # create a new list to store cncatenated output elements
    new_list=[]
    
    
    for i in list1:
        for j in list2:
            new_list.append(i+j)
    # return the concatenated list       
    return new_list

# call the function and display the output
print(concatenate(["Hello ","take "],["Dear","Sir"]))
print(concatenate(["Good ","Bad "],["Morning","Evening"]))


# sample output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# ['Good Morning', 'Good Evening', 'Bad Morning', 'Bad Evening']

