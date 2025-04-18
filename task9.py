class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def mirror(root):
    if root:
        root.left, root.right = mirror(root.right), mirror(root.left)

    return root

values = [15, 10, 20, 8, 12, 17, 25]
original = None
for val in values:
    original = insert(original, val)
print("Original BST (In-order):")
inorder(original)
m = mirror(original)
print("\n\nMirrored BST (In-order):")
inorder(m)
