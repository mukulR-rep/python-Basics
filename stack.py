def push(num,n):
    num.append(n)
    return num
def pop(num):
    if isEmpty(num):
        return False
    else:
        num.pop()
        return num
    
def isEmpty(num):
    if not num:
        return True
    else:
        return False

num = []
push(num,2)
push(num,3)
push(num,8)
push(num,7)
pop(num)
pop(num)
pop(num)
print(num)
