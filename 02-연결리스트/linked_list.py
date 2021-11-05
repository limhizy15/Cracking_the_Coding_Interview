class LinkedListNode:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        current = self.head
        while current:
            # generator를 반환함
            yield current
            current = current.next
    
    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
    
    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)
    
    def append(self, data):
        if self.head is None:
            self.tail = self.head = LinkedListNode(data)
        else:
            self.tail.next = LinkedListNode(data)
            self.tail = self.tail.next
        return self.tail
    
    def appendleft(self, data):
        if self.head is None:
            self.tail = self.head = LinkedListNode(data)
        else:
            self.head = LinkedListNode(data, self.head) # 생성하면서 다음 노드를 기존 헤드로
        return self.head
    
    def pop(self):
        if self.head is None:
            raise IndexError('List is empty')
        item = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return item
    
    def popleft(self):
        if self.head is None:
            raise IndexError('List is empty')
        item = self.head.data
        self.head = self.head.next
        self.head.prev = None
        return item

if __name__ == '__main__':
    DL = LinkedList()
    DL.append(1); DL.append(3); DL.append(5); print(DL)
    DL.appendleft(100); print(DL)
    DL.pop(); print(DL)
    DL.popleft(); print(DL)
    print(len(DL))