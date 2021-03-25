# preorder traversal using recursion 

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None

def createNode(val):
    newNode = Node(0)
    newNode.val = val
    newNode.left = None
    newNode.right = None

    return newNode

def preorder(root):
    if(root == None):
        return
    print(root.val,end = " " )
    preorder(root.left)
    preorder(root.right)

if __name__ == "__main__":
    tree = createNode(5)
    tree.left = createNode(3)
    tree.right = createNode(2)
    tree.left.left = createNode(1)
    tree.left.right = createNode(4)
    tree.right.left = createNode(7)
    tree.right.right = createNode(8)

    print(preorder(tree))