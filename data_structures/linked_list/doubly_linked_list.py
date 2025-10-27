class Node:
    def __init__(self, value: int, next=None, prev=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeEnd(self, value: int):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def insertNodeBeginning(self, value: int):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def getLength(self) -> int:

        c = 0
        if not self.head:
            return c

        curr = self.head
        while curr:
            c += 1
            curr = curr.next

        return c

    def print_linked_list(self):
        if not self.head:
            print("The list is empty")
            return

        curr = self.head
        while curr:
            print(curr, end="")
            if curr.next:
                print(" <-> ", end="")
            curr = curr.next
        print()


if __name__ == "__main__":
    head = tail = DoublyLinkedList()
    head.insertNodeEnd(8)
    head.insertNodeEnd(9)
    head.insertNodeEnd(10)
    head.insertNodeEnd(11)
    head.insertNodeBeginning(7)

    print(head.getLength())

    head.print_linked_list()