#writea program to search anumber in the list
a=[]
size=int(input("Enter size of List:"))
for i in range(size):
    val=int(input("Enter number:"))
    a.append(val)
key=int(input("Enter number to search:"))
flag=0
for i in range(size):
    if(a[i]==key):
        flag=1
        pos=i+1
        break
if(flag==1):
    print("Element found at:",pos,"position.")
else:
    print("Element not found")
