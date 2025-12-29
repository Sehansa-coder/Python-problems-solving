


num=[]
for i in range(10):
    x=int(input(f"Enter number {i+1} : "))
    num.append(x)

print(num)

odd_count=0
even_count=0

for i in range(10):
    if num[i]%2==0:
        num[i]=0
        even_count+=1
    else:
        num[i]=1
        odd_count+=1

print("Odd numbers: ",odd_count)
print("Even numbers: ",even_count)

print(num)


