class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            if i==0:
                res.append(nums[i])
            else:
                res.append(sum(nums[:i+1]))
        return res
        