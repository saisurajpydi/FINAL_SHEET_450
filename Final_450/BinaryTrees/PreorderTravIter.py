# prorder traversal using iteration

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

def iterPreorder(root):
    stack = list()

    if(root == None):
        return 
    stack.append(root)
    while(len(stack) != 0):
        root = stack.pop()
        print(root.val,end = " ")
        if(root.right != None):
            stack.append(root.right)
        if(root.left != None):
            stack.append(root.left)


if __name__ == "__main__":
    tree = createNode(5)
    tree.left = createNode(3)
    tree.right = createNode(2)
    tree.left.left = createNode(1)
    tree.left.right = createNode(4)
    tree.right.left = createNode(7)
    tree.right.right = createNode(8)

    iterPreorder(tree)
