#Using if-else
def linearSearch(num,key):
    for i in range(len(num)):
        if key == num[i]:
            return True
    return False


num = [2,3,4,5,6,11,2,9,0,44,3,23,78,90]
key = 23

if linearSearch(num,key):
    print(key,"is found in the list")
else:
    print(key,"is not found in the list")


    
#Without if-else          
def linearSearch(num,key):
    for i in range(len(num)):
        if key == num[i]:
            return "found at", i
    return "not found"




num = [2,3,4,5,6,11,2,9,0,44,3,23,78,90]
key = 23

print(linearSearch(num,key))
