class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        f = strs[0]
        l = strs[-1]
        res =""
        for i in range(len(f)):
            if f[i]==l[i]:
                res += f[i]
            else:
                break
        return res