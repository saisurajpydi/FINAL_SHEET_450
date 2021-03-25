# Reverse Level Order Traversal
"""
Given a binary tree of size N, find its reverse level order traversal. ie- the traversal must begin from the last level.

Example 1:

Input :
        1
      /   \
     3     2

Output: 3 2 1
Explanation:
Traversing level 1 : 3 2
Traversing level 0 : 1
Example 2:

Input :
       10
      /  \
     20   30
    / \ 
   40  60

Output: 40 60 20 30 10
Explanation:
Traversing level 2 : 40 60
Traversing level 1 : 20 30
Traversing level 0 : 10

Your Task: 
You dont need to read input or print anything. Complete the function reverseLevelOrder() which takes the root of the tree as input parameter and returns a list containing the reverse level order traversal of the given tree.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 10^4



"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None


def reverseLevelOrder(root):
    # code here
    queue = []
    stack = []
    queue.append(root)
    
    while(len(queue) > 0):
        stack.append(queue[0].data)
        node = queue.pop(0)
        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)
            
    stack.reverse()
    return stack


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print(reverseLevelOrder(root))