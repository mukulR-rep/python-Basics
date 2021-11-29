def quickSort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a.pop()

    greater = []
    lower = []

    for i in a:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)
    return quickSort(lower) + [pivot] + quickSort(greater)

l = [9,8,7,6,5,4,3,2,15]
print(quickSort(l))
