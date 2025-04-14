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
def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right) 

#Insertion
values = [54,78,234,56,34,76,45,98]
root = None
for v in values:
    root = insert(root, v)

#counting nodes
total = count(root)
print("Total nodes in BST:", total)