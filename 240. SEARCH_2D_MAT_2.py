class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        r = 0
        c = col-1
        while r<row and c>=0:
            v = matrix[r][c]
            if v==target:
                return True
            elif v>target:
                c -= 1
            else:
                r += 1
        return False