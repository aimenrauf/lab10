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

#Insertion
values = [54,78,234,56,34,76,45,98]
root = None
for v in values:
    root = insert(root, v)
#In-order traversal
print("\n\nIn-Order Traversal:")
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
inorder(root)
#Pre-Order Traversal
print("\n\nPre-Order Traversal")
def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)       
        preorder(root.right)
preorder(root)
#Post_order traversal
print("\n\nPost Order traversal")
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')
postorder(root)