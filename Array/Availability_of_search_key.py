# ( BSC In Information and Technology- Higher Diploma Year 1 question)

# problem:
# Create a single-subscripted array of size 10. 
# Initialize the array with 25, 32, 45, 2, 13, 9, 6, 10, 17, 4. 
# Input a search key (number) from the keyboard and display the location within the array, 
# if the search key is found.

arr=[25,32,45,2,13,9,6,10,17,4]

search_key=int(input("Enter a number:"))
for i in range(len(arr)):
    if search_key==arr[i]:
        print(f"Location of the search key number:{i}")
        break
else:        
    print("Number not found")



# sample output:
# Enter a number:10
# Location of the search key number:7

#---------------------------------------
# Enter a number:-4
# Number not found

    

