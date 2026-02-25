class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = ""
        for i in s:
            if i.isdigit():
                n += i
        l = set(n)
        if len(l)<=1:
            return -1
        else:
            ls = list(l)
            ls.sort()
            return int(ls[-2])