#write a program to find reverse of a given number
i=int(input("Enter Number:"));
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
print("Reverse number is=",rev);    
