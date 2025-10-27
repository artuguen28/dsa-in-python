class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    

def addNode(head: Node, value: int) -> Node:

    if not(head):
        return Node(value)
    
    current = head
    while current.next:
        current = current.next
    current.next = Node(value)

    return head



def print_linked_list(head: Node) -> None:
    if not(head):
        print("The list is empty")
        return

    current = head

    while current:
        print(current, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print()


if __name__ == "__main__":
    head = Node(1)
    addNode(head, 5)
    addNode(head, 7)
    addNode(head, 8)

    print_linked_list(head)
