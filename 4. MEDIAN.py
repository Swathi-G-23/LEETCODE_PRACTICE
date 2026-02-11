class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        res = nums1 + nums2
        res.sort()
        if len(res)%2==1:
            median = res[len(res)//2]
        else:
            m1 = res[len(res)//2-1]
            m2 = res[len(res)//2]
            median = (m1+m2)/2.0
        return median
        