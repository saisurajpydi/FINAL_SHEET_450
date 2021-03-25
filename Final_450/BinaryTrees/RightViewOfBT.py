# Right view of binary tree
"""
Given a Binary Tree, find Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

Right view of following tree is 1 3 7 8.

          1
       /     \
     2        3
   /   \      /    \
  4     5   6    7
    \
     8

Example 1:

Input:
       1
    /    \
   3      2
Output: 1 2
Example 2:

Input:
     10
    /   \
  20     30
 /   \
40  60 
Output: 10 30 60
Your Task:
Just complete the function rightView() that takes node as parameter and returns the right view as a list. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105.
"""

class Solution:
    def rightView(self,root):
        '''
        :param root: root of given tree.
        :return: the right view of tree,
        '''
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
                      
                # Print the right most element 
                # at the level 
                if (i == n) :
                    result.append(temp.data)
                  
                # Add left node to queue 
                if (temp.left != None) :
                    q.append(temp.left) 
      
                # Add right node to queue 
                if (temp.right != None) :
                    q.append(temp.right)         
                
        return result