a=[]
for i in range(5):
    x=input("Enter Value:")
    a.append(x)
print("originl list of:",a)
index=int(input("Enter Index:"))
value=input("zenter value:")
a.insert(index,value)
print("List after insertion:",a)
