"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        recol = 0  
        for i in range(row):
            if(matrix[i][0] == target or matrix[i][col-1] == target):
                return True
            elif(matrix[i][0] < target and matrix[i][col-1] > target):
                recol = i
        for j in range(1,col):
            if(matrix[recol][j] == target):
                return True
        return False