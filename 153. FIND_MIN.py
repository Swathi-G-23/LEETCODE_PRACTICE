class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        nums = list(s)
        min = nums[0]
        for i in range(len(nums)):
            if nums[i]<min:
                min = nums[i]
        return min

        