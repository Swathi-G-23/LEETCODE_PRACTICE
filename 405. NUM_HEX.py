class Solution(object):
    def toHex(self, num):
        return hex(num & 0xffffffff)[2:]