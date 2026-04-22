class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # In-order Traversal: Left -> Root -> Right
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val, end=' ')
        if self.right:
            self.right.inorder()

    # Pre-order Traversal: Root -> Left -> Right
    def preorder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    # Post-order Traversal: Left -> Right -> Root
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val, end=' ')

# Usage Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order traversal: ", end='')
root.inorder()
print("\nPre-order traversal: ", end='')
root.preorder()
print("\nPost-order traversal: ", end='')
root.postorder()   
