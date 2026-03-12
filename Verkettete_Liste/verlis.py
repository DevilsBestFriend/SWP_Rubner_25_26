class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __next__(self):
        return self.next
    
    def __str__(self):
        return "Data: " + str(self.data) + "; "


class LinkedList:

    def __init__(self, data):
        self.first = Node(data=data)

    def __iter__(self):
        self.current = self.first
        return self.first

    def __next__(self):
        self.current = self.current.next
        return self.current

    def apendieren(self, data):
        next = self.first
        while next.next != None:
            next = next.next
        next.next = Node(data=data)
        
    def insertieren():
        pass
    
    def deletieren():
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
    


def main():
    listn = LinkedList(1)
    
    listn.apendieren(2)
    listn.apendieren(3)
    listn.apendieren("test")
    
    x = 0
    for l in listn:
        print(l.data)
        x += 1
        if x >= 10:
            pass
        
    
    print(listn.first)
    print(listn.all())
    print(listn.last())
 
if __name__ == "__main__":
    main()
    
    