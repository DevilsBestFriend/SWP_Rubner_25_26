class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Data: " + str(self.data) + "; "


class LinkedList:

    def __init__(self, data):
        self.first = Node(data=data)

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        
        data = self.current.data
        self.current = self.current.next
        return data

    def apendieren(self, data):
        next = self.first
        while next.next != None:
            next = next.next
        next.next = Node(data=data)
        
    def insertieren():
        pass
    
    def deletieren():
        pass
    
    def pop():
        pass

    def __len__(self):
        count = 0
        while next != None:
            count += 1

    def all(self):
        all = list()
        next = self.first
        while next != None:
            all.append(next.data)
            next = next.next
        return all
    
    def last (self):
        all = list()
        next = self.first
        while next.next != None:
            next = next.next
        return next.data