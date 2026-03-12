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

    def add(self, data):
        next = self.first
        while next.next != None:
            next = next.next
        next.next = Node(data=data)

    def __len__(self):
        pass

    def all(self):
        all = list()
        next = self.first
        while next != None:
            all.append(next.data)
            next = next.next
        return all


def main():
    pass

if __name__ == "__main__":
    main()
    
    listn = LinkedList(1)
    
    listn.add(2)
    listn.add(3)
    listn.add("test")
    
    print(listn.first)
    print(listn.all())