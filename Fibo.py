#write a program to print a fibonacci series upto a given  number
n=int(input("Enter Number"));
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
    
    
