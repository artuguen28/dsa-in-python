class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = None

    def convertToCircular(self, pos: int):

        if not self.head:
            print("The list in empty")
            return
        
        
        c = 0
        curr = self.head
        cycleNode = self.head

        while curr:
            if c == pos:
                cycleNode = curr

            if not curr.next:
                curr.next = cycleNode
                return

            curr = curr.next
            c += 1

    def detectCycle(self):

        if not self.head:
            print("The list in empty")
            return


        fast = self.head
        slow = self.head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Cycle detected
                print("Cycle found!")
                return True

        print("No cycle found.")
        return False

    def printLinkedList(self):

        if not self.head:
            print("The list is empty")
            return

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
        if not self.head: 
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

    def deleteNodeByPos(self, pos: int):
        if not self.head:  # Handle empty list
            print("The list is empty")
            return

        if pos == 0:  # Handle deletion of the head node
            temp = self.head
            self.head = self.head.next
            del temp
            return

        c = 0
        curr = self.head
        prev = None

        while curr:
            if c == pos:
                prev.next = curr.next
                del curr
                return
            prev = curr
            curr = curr.next
            c += 1

        print("Invalid position")  # Position out of bounds


def mergeTwoSortedLists(lst_1: LinkedList, lst_2: LinkedList) -> LinkedList:
    mergedList = LinkedList()

    curr_1 = lst_1.head
    curr_2 = lst_2.head

    while curr_1 and curr_2:
        if (curr_1.data < curr_2.data):
            mergedList.insertNode(curr_1.data)
            curr_1 = curr_1.next
        else:
            mergedList.insertNode(curr_2.data)
            curr_2 = curr_2.next

    
    while curr_1:
        mergedList.insertNode(curr_1.data)
        curr_1 = curr_1.next
        
    while curr_2:
        mergedList.insertNode(curr_2.data)
        curr_2 = curr_2.next

    return mergedList
                


if __name__ == "__main__":

    lst_1 = LinkedList()
    lst_1.insertNode(1)
    lst_1.insertNode(3)
    lst_1.insertNode(5)

    lst_2 = LinkedList()
    lst_2.insertNode(2)
    lst_2.insertNode(4)
    lst_2.insertNode(6)
    lst_2.insertNode(9)
    lst_2.insertNode(14)

    merged_list = mergeTwoSortedLists(lst_1, lst_2)
    merged_list.printLinkedList()