"""Write a program to find whether the given  number is armstrong or not"""

i=int(input("Enter Number:"));
orig=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("Number is armstrong")
else:
    print("Number is Not armstrong")
