# Traversals
import random
from collections import deque

class TreeNode:

    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def get_left_child(self):
        return self.left

    def set_left_child(self, tnode):
        self.left = tnode
        return

    def get_right_child(self):
        return self.right
    
    def set_right_child(self, tnode):
        self.right = tnode
        return

    def get_value(self):
        return self.value


def create_tree():
    root = TreeNode(None, None, random.randint(1, 20))
    nodes = deque()
    nodes.append(root)
    numNodes = 1
    values_as_array = [root.value]
    while numNodes < 16:
        current = nodes.popleft()
        
        current.left = TreeNode(None, None, random.randint(1, 20))
        nodes.append(current.left)
        values_as_array.append(current.left.value)
        numNodes += 1
        
        current.right = TreeNode(None, None, random.randint(1, 20))
        nodes.append(current.right)
        values_as_array.append(current.right.value)
        numNodes += 1

    print(values_as_array)
    return root


def inorder_traversal(rootNode):
    
    inorder = []
    nodes = deque()

    if rootNode == None:
        return inorder

    while (rootNode is not None or len(nodes) != 0):
        #push left
        while (rootNode is not None):
            nodes.appendleft(rootNode)
            rootNode = rootNode.left


        rootNode = nodes.pop()
        inorder.append(rootNode.value)

        rootNode = rootNode.right

    return inorder

def preorder_traversal(rootNode):

    if rootNode == None:
        return []

    preorder = [rootNode.value]

    preorder.append(preorder_traversal(rootNode.left))
    preorder.append(preorder_traversal(rootNode.right))

    return preorder
    
