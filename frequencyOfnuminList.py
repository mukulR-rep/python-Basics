#write a program to count frequency of a given number from a list
a=[]
size=int(input("Enter size of List:"))
for i in range(size):
    val=int(input("Enter nuimber:"))
    a.append(val)
key=int(input("Enter number to find frequency:"))
count=0
for i in range(size):
    if(a[i]==key):
        count=count+1
print("Frequency=",count)        
