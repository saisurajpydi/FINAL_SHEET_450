# Create a mirror tree from the given binary tree
"""
Given a binary tree, the task is to create a new binary tree which is a mirror image of the given binary tree.

Examples: 

Input:
        5
       / \
      3   6
     / \
    2   4
Output:
Inorder of original tree: 2 3 4 5 6 
Inorder of mirror tree: 6 5 4 3 2
Mirror tree will be:
  5
 / \
6   3
   / \
  4   2

Input:
        2
       / \
      1   8
     /     \
    12      9
Output:
Inorder of original tree: 12 1 2 8 9 
Inorder of mirror tree: 9 8 2 1 12
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def createNode(val):
    newNode = Node(0)
    newNode.val = val 
    newNode.right = None 
    newNode.left = None 
    return newNode


def inorder(root):
    if(root == None):
        return 
    inorder(root.left)
    print(root.val,end = " ")
    inorder(root.right)

def mirrorify(root,mirror):
    if(root == None):
        mirror = None 
        return mirror

    mirror = createNode(root.val)
    mirror.left = mirrorify(root.right,(mirror).left)
    mirror.right = mirrorify(root.left,(mirror).right)

    return mirror 


if __name__ == "__main__":
    tree = createNode(5)
    tree.left = createNode(3)
    tree.right = createNode(2)
    tree.left.left = createNode(1)
    tree.left.right = createNode(4)
    tree.right.left = createNode(7)
    tree.right.right = createNode(8)
    print("this is original ",end = " ")
    inorder(tree)

    mirror = None 
    mirror = mirrorify(tree,mirror)
    print()
    print("this is mirror image",end = " ")
    inorder(mirror)




    