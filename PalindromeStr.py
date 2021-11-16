#write a program to check a sting is palindrome or not
a=input("Enter String:");
b=a[-1::-1]
if(a==b):
    print("Palindrome String")
else:
    print("Not Palindrome String")
