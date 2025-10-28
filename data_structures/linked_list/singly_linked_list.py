class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):

        if not self.head:
            print("The list is empty")

        curr = self.head
        while curr:
            print(curr, end="")
            if curr.next:
                print(" -> ", end="")
            curr = curr.next
        print()
        

    def insertNode(self, value: int):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = newNode

    def reverseList(self):
        if not self.head:
            print("The list is empty")
            return
        
        prev = None
        curr = self.head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def deleteNodeByValue(self, value: int):
        if not self.head:  # Handle empty list
            print("The list is empty")
            return

        # Handle deletion of the head node
        if self.head.data == value:
            temp = self.head
            self.head = self.head.next
            del temp
            return

        curr = self.head
        prev = None

        # Traverse the list to find the node to delete
        while curr:
            if curr.data == value:
                prev.next = curr.next
                del curr
                return
            prev = curr
            curr = curr.next

        print("Value not found in the list")


if __name__ == "__main__":

    sll = LinkedList()

    sll.insertNode(5)
    sll.insertNode(6)
    sll.insertNode(10)
    sll.insertNode(17)

    sll.printLinkedList()

    sll.reverseList()

    sll.printLinkedList()
