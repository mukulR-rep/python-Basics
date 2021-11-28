def isEmpty(queue):
    if not queue:
        return True
    else:
        return False

def enqeue(queue,n):
    queue.append(n)
    return queue

def dequeue(queue):
    if isEmpty(queue):
        print("queue is enmpty")
        return False
    else:
        queue.dequeue(0)
        return queue   
queue = []

print(queue)
queue.append(2)
queue.append(5)
queue.append(4)
queue.append(8)
queue.append(9)

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue)
