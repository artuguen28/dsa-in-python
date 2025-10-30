class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class BinarySearchTree:

    def __init__(self):
        self.root = None
    
    def insertNodeIterative(self, value: int):
        newNode = Node(value)

        if not self.root:
            self.root = newNode
            return

        current = self.root

        while True:
            if value < current.data:
                if not current.left:
                    current.left = newNode
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = newNode
                    return
                current = current.right

    def insertNodeRecursive(self, current: Node, value: int) -> Node:
        if not current:
            return Node(value)

        if value < current.data:
            current.left = self.insertNodeRecursive(current.left, value)
        else:
            current.right = self.insertNodeRecursive(current.right, value)

        return current

    def insertNode(self, value: int):
        self.root = self.insertNodeRecursive(self.root, value)




