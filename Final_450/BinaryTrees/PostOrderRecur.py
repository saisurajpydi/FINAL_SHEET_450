# post order taversal using recursion 

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

def postOrder(root):
    if(root == None):
        return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.val , end = " ")

if __name__ == "__main__":
    tree = createNode(5)
    tree.left = createNode(3)
    tree.right = createNode(2)
    tree.left.left = createNode(1)
    tree.left.right = createNode(4)
    tree.right.left = createNode(7)
    tree.right.right = createNode(8)

    postOrder(tree)


