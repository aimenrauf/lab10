class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def balance(list):
    if not list:
        return None
    mid = len(list) // 2    #this will return the middle element of the list
    root = Node(list[mid])
    root.left = balance(list[:mid])
    root.right = balance(list[mid+1:])
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

list = [2, 4, 6, 8, 10, 12, 14]
root = balance(list)
print("\nIn-order traversal of the constructed BST:")
inorder(root)