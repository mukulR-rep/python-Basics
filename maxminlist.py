#write a programto find max and min number in list
a=[]
size=int(input("Enter size of the List:"))
for i in range(size):
    val=int(input("Enter number:"))
    a.append(val)
maxval=max(a)
minval=min(a)
print("Max Number=",maxval)
print("Min Number=",minval)
