i=int(input("Enter Number:"));
rev=0
a=i
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(a==rev):
    print("Palindrome")
else:
    print("Not Palindrome")    
