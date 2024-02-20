class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
        self.length +=1

    def __len__(self):
        return self.length
    
    def __getitem__(self, index:int):
        if not isinstance(index,int):
            raise TypeError
        if self.length <= index:
            raise IndexError
        node = self.head
        for _ in range(index):
            node = node.next_node
        return node.data
    
    def __setitem__(self, index:int, value):
        node = self.head
        for _ in range(index):
            node = node.next_node
        node.data = value
        return node.data

    def __delitem__(self, index:int):
        node = self.head
        for _ in range(index):
            node = node.next_node
        
        if node.next_node == None:
            self.tail = node.prev_node
        else:
            node.next_node.prev_node = node.prev_node
        if node.prev_node == None:
            self.head = node.next_node
        else:
            node.prev_node.next_node = node.next_node
        self.length -= 1
    
    def insert(self, value, index:int):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index < self.length:
            node = self.head
            for _ in range(index):
                node = node.next_node
            new_node.next_node = node
            new_node.prev_node = node.prev_node

            for _ in range(index, self.length):
                node.next_node = node.next_node.next_node
                node.prev_node = node
                node = node.next_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
        self.length +=1


linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)