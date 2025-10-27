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



if __name__ == "__main__":

    sll = LinkedList()

    sll.insertNode(5)
    sll.insertNode(6)
    sll.insertNode(10)
    sll.insertNode(17)
    sll.printLinkedList()
