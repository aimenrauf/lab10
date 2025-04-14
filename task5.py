class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root
def height(root):
    if root is None:
        return -1  # Height in terms of edges
    return 1 + max(height(root.left), height(root.right))

#Insertion
values = [54,78,234,56,34,76,45,98]
root = None
for v in values:
    root = insert(root, v)
h = height(root)
print("Height of the BST is: ",h)