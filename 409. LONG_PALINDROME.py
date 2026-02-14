from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        var = Counter(s)
        l = 0
        od = False
        for i in var.values():
            if i%2==0:
                l += i
            else:
                l += i-1
                od = True
        if od:
            l += 1
        return l
