class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        p_d = 1
        s_d = 0
        for i in n:
            p_d *= int(i)
            s_d += int(i)
            res = p_d - s_d
        return res