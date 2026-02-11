class Solution(object):
    def isAnagram(self, s, t):
        flag = True
        if sorted(s)==sorted(t):
            return flag
        else:
            return not flag