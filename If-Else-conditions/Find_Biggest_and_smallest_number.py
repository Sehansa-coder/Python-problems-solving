n1=20
n2=100
n3=2

biggest=n1
if n2>biggest:   # check whether n2 is bigger than n1
    biggest=n2
elif n3>biggest:  # check whether n3 is bigger than n1
    biggest=n3

print("Biggest number:",biggest)   # print the biggest number

smallest=n1
if n2<smallest:       #check whether n2 is smaller than n1
    smallest=n2
elif n3<smallest:     # check whether n3 is smaller than n1
    smallest=n3

print("Smallest number: ",smallest)   # print the smallest number