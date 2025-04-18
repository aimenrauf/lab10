class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def is_bst_helper(node, min_val, max_val):
    if node is None:
        return True
    if node.data <= min_val or node.data >= max_val:
        return False
    return is_bst_helper(node.left, min_val, node.data) and \
           is_bst_helper(node.right, node.data, max_val)
def is_bst(root):
    return is_bst_helper(root, -999999, 999999)

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(17)
root.right.right = Node(25)

if is_bst(root):
    print("The tree is a valid Binary Search Tree.")
else:
    print("The tree is NOT a valid Binary Search Tree.")
