class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                res.append(i)

        if len(res) == 0:
            return 0

        s = sum(res)
        m = s // len(res)
        return m
