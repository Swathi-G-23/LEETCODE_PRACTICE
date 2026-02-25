class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for i in nums:
            if nums.count(i)==1:
                c += int(i)
        return c