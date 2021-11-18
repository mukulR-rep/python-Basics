#write a program to find sum of elements of the list
a=[]
size=int(input("how many elements you want to enter:"))
for i in range(size):
    val=int(input("Enter Number:"))
    a.append(val)
sum=0
for i in range(size):
    sum=sum+a[i]
print("Sum of List Elements=",sum)    
