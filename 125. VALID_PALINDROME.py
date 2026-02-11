class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ""
        for i in s:
            if i.isalnum():
                res += i.lower()

        if res == res[::-1]:
            return True
        else:
            return False