class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None 

    def __str__(self): 
        return str(self.value)


class LinkedList: 

    def __init__(self): 
        self._size = 0 
        self._head = None

    def add(self, value): 
        if self._head is None: 
            self._head = Node(value)
        elif value < self._head.value: 
            newHead = Node(value) 
            newHead.next = self._head 
            self._head = newHead
        else: 
            currNode = self._head 
            while currNode.next is not None: 
                if value < currNode.next.value: 
                    newNode = Node(value)
                    newNode.next = currNode.next 
                    currNode.next = newNode 

                    return

                currNode = currNode.next

            if currNode.next is None: 
                currNode.next = Node(value)            

        self._size += 1

    def remove(self, value):
        pass 

    def get(self, index): 
        if index > self._size: 
            IndexError("Index is out of bounds")
        
        i = 0 
        node = self.head
        while i < index: 
            i += 1
            node = node.next 

        return node.value
            
         
    def length(self): 
        return self._size 

    def __str__(self): 
        node = self._head 
        ret = ""
        while node: 
            ret += str(node) + " "
            node = node.next 
        
        return ret
    
    def __len__(self): 
        return self._size

l = LinkedList()
from numpy.random import randint
for i in range(1, 10):
    l.add(randint(0, 1000))

for i in range(len(l)): 
    try: 
        assert(l())
    except IndexError: 
        print("end of list")
