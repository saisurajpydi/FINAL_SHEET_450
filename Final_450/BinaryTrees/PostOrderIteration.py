# post order traversal using iteration 

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
    s1 = list() 
    s2 = list() 
    if(root == None):
        return 
    s1.append(root)
    while(len(s1) != 0):
        root = s1.pop()
        s2.append(root)
        if(root.left != None):
            s1.append(root.left)
        if(root.right != None):
            s1.append(root.right)
            
    while(len(s2) != 0):
        root = s2.pop()
        print(root.val,end = " ")


if __name__ == "__main__":
    tree = createNode(5)
    tree.left = createNode(3)
    tree.right = createNode(2)
    tree.left.left = createNode(1)
    tree.left.right = createNode(4)
    tree.right.left = createNode(7)
    tree.right.right = createNode(8)

    postOrder(tree)
