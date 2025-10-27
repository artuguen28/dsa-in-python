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

    def deleteNodeByValue(self, value: int):
        if not self.head:  # Always handle empty lists
            print("The list is empty.")
            return

        if self.head.value == value:  # Handle deletion of head node
            if self.head == self.tail:  # Single node case
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return

        if self.tail.value == value:  # Handle deletion of tail node
            self.tail = self.tail.prev
            self.tail.next = None
            return

        curr = self.head

        while curr:
            if curr.value == value:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                del curr
                return
            curr = curr.next

        print("This value doesn't exist in this list.")

    def reverseList(self):
        if not self.head:  # Handle empty list
            print("The list is empty.")
            return

        curr = self.head
        self.tail = self.head  # Update tail to the current head

        while curr:
            # Swap the next and prev pointers
            curr.prev, curr.next = curr.next, curr.prev
            # Move to the next node (which is the previous node in the original list)
            if not curr.prev:  # If prev is None, this is the new head
                self.head = curr
            curr = curr.prev

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
    dll = DoublyLinkedList()
    dll.insertNodeEnd(8)
    dll.insertNodeEnd(9)
    dll.insertNodeEnd(10)
    dll.insertNodeEnd(11)
    dll.insertNodeBeginning(7)

    dll.reverseTheList()

    print(dll.tail)

    print(dll.getLength())

    dll.print_linked_list()