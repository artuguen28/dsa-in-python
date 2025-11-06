import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class BinaryTree:

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

    def insert(self, value: int):
        self.root = self.insertNodeRecursive(self.root, value)



def inorder(node: Node):
    if not node:
        return

    inorder(node.left)
    print(node.data, end=' ') 
    inorder(node.right)

def printBFS(node: Node):
        if not node:
            return

        q = queue.Queue()
        q.put((node, 0))  # Store the node along with its layer

        current_layer = 0
        print(f"Layer {current_layer}:", end=" ")
        while not q.empty():
            n, layer = q.get()

            if layer != current_layer:
                current_layer = layer
                print()
                print(f"Layer {current_layer}:", end=" ")

            print(n.data, end=" ")

            if n.left:
                q.put((n.left, layer + 1))
            if n.right:
                q.put((n.right, layer + 1))

        print()  # Print a newline after the last layer

def printDFS(node: Node):
    if not node:
        return
    
    visited = set()
    stack = [node]
    visited.add(node)

    while stack:
        n = stack.pop()
        print(n.data, end=" ")

        if n.right and n.right not in visited:
            visited.add(n.right)
            stack.append(n.right)
            
        if n.left and n.left not in visited:
            visited.add(n.left)
            stack.append(n.left)


    print()




if __name__ == "__main__":
    tree = BinaryTree()
    values = [7, 3, 9, 1, 5, 8, 10]
    for v in values:
        tree.insert(v)

    # inorder(tree.root)
    printBFS(tree.root)



