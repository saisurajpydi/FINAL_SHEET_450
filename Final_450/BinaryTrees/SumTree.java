/*
Given a Binary Tree. Check whether it is a Sum Tree or not.

A Binary Tree is a Sum Tree in which value of each node x is equal to sum of nodes present in its left subtree and right subtree . An empty tree is also a Sum Tree as sum of an empty tree can be considered to be 0. A leaf node is also considered as a Sum Tree.

Example 1:

Input:
    3
  /   \    
 1     2

Output: 1
Explanation: The given tree is a sum 
tree so return a boolean true.

Example 2:

Input:

          10
        /    \
      20      30
    /   \ 
   10    10

Output: 0
Explanation: The given tree is not a sum
tree. For the root node, sum of elements
in left subtree is 40 and sum of elements
in right subtree is 30. Root element = 10
which is not equal to 30+40.

Your Task: 
You dont need to read input or print anything. Complete the function isSumTree() which takes root node as input parameter and returns true if the tree is a SumTree else it returns false.
 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(Height of the Tree)
*/
public class SumTree {
    static int height(Node root) {
        int lh = 0;
        int rh = 0;
        if (root == null) {
            return 0;
        }
        return (height(root.left) + root.data + height(root.right));
    }

    boolean isSumTree(Node root) {
        int ls, rs;
        // Your code here
        if (root == null) {
            return true;
        }
        int rootval = root.data;
        ls = height(root.left);
        rs = height(root.right);

        if (rootval == ls + rs) {
            return true;
        }
        return false;
    }
}
