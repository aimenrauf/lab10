from collections import deque
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def levelorder(root):
    if root is None:
        return  
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        print(current.data, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

values = [15, 10, 20, 8, 12, 17, 25]
root = None
for val in values:
    root = insert(root, val)
print("Level-Order Traversal of BST:")
levelorder(root)