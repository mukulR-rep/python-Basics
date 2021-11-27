#Write a program to read positive numbers continuously until negative number is given by using ‘if’?
a = (1,5,4,9,8,-5,5,4,6 )
i = 0
#To print array numbers
print("Given numbers")
print(a)
for i in a:
    print(i)

    if i<=0:
        break;
