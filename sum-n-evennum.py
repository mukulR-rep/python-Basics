max = int(input("Please enter the maximum value: "))
total = 0

for num in range(1, max+1):
    if(num % 2 == 0):
        print("{0}".format(num))
        total = total + num

print("The Sum of Even Numbers from 1 to {0} = {1}".format(num, total))
