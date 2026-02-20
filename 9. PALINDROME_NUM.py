class Solution(object):
    def isPalindrome(self, x):
        i = str(x)
        if i == i[::-1]:
            return True
        else:
            return False