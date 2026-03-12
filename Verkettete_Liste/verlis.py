class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __next__(self):
        return self.next


class LinkedList:

    def __init__(self, data):
        self.first = Node(data=data)

    def __iter__(self):
        self.current = self.first
        return self.first

    def __next__(self):
        self.current = self.current.next
        return self.current

    def add(self, new):
        while next.next != None:
            next = next.next
        next.next = new

    def __len__(self):
        pass

    def all(self):
        all = [self.first.data]
        next = self.first
        while next.next != None:
            all.append(next.data)


def main():
    pass

if __name__ == "__main__":
    main()
    
    listn = LinkedList(1)
    
    print(listn.all())