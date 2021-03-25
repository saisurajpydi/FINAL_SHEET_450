# Left view of binary tree 
"""
Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /     \    /    \
  4     5   6    7
   \
     8   

Example 1:

Input:
   1
 /  \
3    2
Output: 1 3

Example 2:

Input:

Output: 10 20 40
Your Task:
You just have to complete the function leftView() that prints the left view. The newline is automatically appended by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
0 <= Number of nodes <= 100
1 <= Data of a node <= 1000
"""


def LeftView(root):
    # code here
    result = []
    if (not root):
        return result
 
    q = []
    q.append(root)
 
    while (len(q)):
 
        # number of nodes at current level
        n = len(q)
 
        # Traverse all nodes of current level
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
 
            # Print the left most element
            # at the level
            if (i == 1):
                result.append(temp.data)
 
            # Add left node to queue
            if (temp.left != None):
                q.append(temp.left)
 
            # Add right node to queue
            if (temp.right != None):
                q.append(temp.right)
    return result