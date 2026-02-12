class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        f = l = -1
        for i in range(len(nums)):
            if nums[i]==target:
                f = i
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==target:
                l = j
                break
        return [f,l]