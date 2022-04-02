# cook your dish here
for i in range(int(input())):
    a,f,k=map(int,input().split())
    n=a-f
    if f*3-n*1>=k:
        print("PASS")
    else:
        print("FAIL")