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

def LCA(root, n1, n2):
    if root is None:
        return None
    if n1 < root.data and n2 < root.data:
        return LCA(root.left, n1, n2)
    elif n1 > root.data and n2 > root.data:
        return LCA(root.right, n1, n2)
    else:
        return root

values = [20, 10, 30, 5, 15, 25, 35]
root = None
for val in values:
    root = insert(root, val)
n1 = 5
n2 = 15
lca = LCA(root, n1, n2)
if lca:
    print(f"Lowest Common Ancestor of {n1} and {n2}: {lca.data}")
else:
    print("LCA not found.")
