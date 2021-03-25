# inorder traversal using iterator 

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None
"""

def createNode(val):
    newNode = Node(0)
    newNode.val = val
    newNode.left = None
    newNode.right = None
    return newNode
    
def iterInorder(root):
    stack = list() 
    if(root == None):
        return 
    while(True):
        if(root != None):
            stack.append(root)
            root = root.left
        else:
            if(len(stack) == 0):
                break
            root = stack.pop()
            print(root.val,end = " ")
            root = root.right 

if __name__ == "__main__":
    tree = createNode(5)
    tree.left = createNode(3)
    tree.right = createNode(2)
    tree.left.left = createNode(1)
    tree.left.right = createNode(4)
    tree.right.left = createNode(7)
    tree.right.right = createNode(8)

    iterInorder(tree)    
"""
class Solution:
    
    def createNode(self,val):
        newNode = Node(0)
        newNode.val = val
        newNode.left = None
        newNode.right = None
        return newNode
    
    def iterInorder(self,root):
        stack = list() 
        if(root == None):
            return 
        while(True):
            if(root != None):
                stack.append(root)
                root = root.left
            else:
                if(len(stack) == 0):
                    break
                root = stack.pop()
                print(root.val,end = " ")
                root = root.right 

if __name__ == "__main__":
    so = Solution()
    tree = so.createNode(5)
    tree.left = so.createNode(3)
    tree.right = so.createNode(2)
    tree.left.left = so.createNode(1)
    tree.left.right = so.createNode(4)
    tree.right.left = so.createNode(7)
    tree.right.right = so.createNode(8)

    so.iterInorder(tree)
