"""Write a program to find sum of digits of given numbers"""
i=int(input("Enter Number tp find sum of digits:"));
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print("Sum of digits=",sum)

