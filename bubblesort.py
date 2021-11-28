#write a progam for bubbl sort?
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,4,43,27,7,41,45,21,70]
bubbleSort(nlist)
print(nlist)
