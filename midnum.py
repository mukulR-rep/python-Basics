a = int(input("Enter 1st Number:"));
b = int(input("Enter 2nd Number:"));
c = int(input("Enter 3rd Number:"));
if(a>b)and(a<c) or (a<b)and(a>c):
    print("Mid Number =",a)
elif(b>a)and(b<c) or (b<a)and(b>c):
    print("Mid Number =",b)
else:
    print("Mid Number =",c)
