class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return "Data= " + self.data + " Next= " + self.next


class LinkedList:

    def __init__(self, data):
        self._first_node = Node(data=data)

    def __iter__(self):
        self.current = self._first_node
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        
        data = self.current.data
        self.current = self.current.next
        return data

    def __add__(self, data):
        next = self._first_node
        while next.next != None:
            next = next.next
        next.next = Node(data=data)
        
    def insertieren(self, i, data): #fügt nach dem index i ein
        if self.__len__() < i:
            raise IndexError
        node_i = self._first_node
        for _ in range(0, i):
            node_i = node_i.next
            
        node_next = node_i.next
        node_i.next = Node(data=data, next=node_next)
    
    def deletieren(self, i): #löscht den index
        if self.__len__() < i:
            raise IndexError
        node_i = self._first_node
        for _ in range(0, i-1):
            node_i = node_i.next
            
        node_next = node_i.next.next
        node_i.next = node_next
    
    def pop(self):
        current = self._first_node
        while current.next.next != None:
            current = current.next
        
        data = current.next
        current.next = None
        return data

    def __len__(self):
        count = 0
        current = self._first_node
        while current.next != None:
            current = current.next
            count += 1
        return count

    def all(self):
        all = list()
        next = self._first_node
        while next != None:
            all.append(next.data)
            next = next.next
        return all
    
    def last(self):
        all = list()
        next = self._first_node
        while next.next != None:
            next = next.next
        return next.data
    
    def first(self):
        return self._first_node.data
    