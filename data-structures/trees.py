class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Traversals
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

from collections import deque

def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data, end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# Creating a sample tree:
#        1
#      /   \
#     2     3
#    / \   / 
#   4   5 6  

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print("In-order:")
inorder(root)     # 4 2 5 1 6 3

print("\nPre-order:")
preorder(root)    # 1 2 4 5 3 6

print("\nPost-order:")
postorder(root)   # 4 5 2 6 3 1

print("\nLevel-order:")
level_order(root) # 1 2 3 4 5 6
