class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        n=len(matrix[0])
        l,h = 0,m*n-1
        while l<=h:
            m = (l+h)//2
            row = m//n
            col = m%n
            val = matrix[row][col]
            if val==target:
                return True
            elif val<target:
                l = m+1
            else:
                h = m-1
        return False