class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__ (self):
        self.head = Node()

    def accept_data(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node    

    def display(self):
        disp = []
        cur = self.head
        disp.append(cur.data)
        while cur.next != None :
            cur = cur.next
            disp.append(cur.data)
        print(disp)    


l = Linkedlist()
l.head = Node(1)
element2 = Node(2)
element3 = Node(3)

l.head.next = element2;
element2.next = element3;

l.display()
