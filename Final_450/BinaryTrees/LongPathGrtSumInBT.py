"""
Sum of the Longest Bloodline of a Tree (Sum of nodes on the longest path from root to leaf node) 
Easy Accuracy: 49.91% Submissions: 10024 Points: 2
Given a binary tree of size N. Your task is to complete the function sumOfLongRootToLeafPath(), that find the sum of all nodes on the longest path from root to leaf node.
If two or more paths compete for the longest path, then the path having maximum sum of nodes is being considered.

Examples:

Input : Binary tree:
        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3    
      /
     6
Output : 13

        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3 
      /
     6

The highlighted nodes (4, 2, 1, 6) above are 
part of the longest root to leaf path having
sum = (4 + 2 + 1 + 6) = 13
Input:
The function takes a single argument as input the reference pointer to the root of the binary tree.
There will be T, test cases and for each test case the function will be called separately.

Output:
For each test case print the required sum on a new line.

Constraints:
1<=T<=103
1<=N<=103

Example:
Input:
2
2
1 2 L 1 3 R
7
4 2 L 4 5 R 2 7 L 2 1 R 1 6 L 5 2 L 5 3 R
Output:
4
13
"""


def SumOfLongRootToLeafPath(root, Sum, Len, maxLen, maxSum):

    # if true, then we have traversed a
    # root to leaf path
    if (not root):

        # update maximum Length and maximum Sum
        # according to the given conditions
        if (maxLen[0] < Len):
            maxLen[0] = Len
            maxSum[0] = Sum
        elif (maxLen[0] == Len and
              maxSum[0] < Sum):
            maxSum[0] = Sum
        return

    # recur for left subtree
    SumOfLongRootToLeafPath(root.left, Sum + root.data,
                            Len + 1, maxLen, maxSum)

    # recur for right subtree
    SumOfLongRootToLeafPath(root.right, Sum + root.data,
                            Len + 1, maxLen, maxSum)


def sumOfLongRootToLeafPath(root):
    #:param root: root of the given tree.
    #:RETURN: SUM
    # result = list()
    # result = sumval(root)
    # return result[1]
    if (not root):
        return 0

    maxSum = [-999999999999]
    maxLen = [0]

    # finding the maximum Sum 'maxSum' for
    # the maximum Length root to leaf path
    SumOfLongRootToLeafPath(root, 0, 0, maxLen, maxSum)

    # required maximum Sum
    return maxSum[0]
