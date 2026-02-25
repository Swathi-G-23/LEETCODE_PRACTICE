class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        alpha=num=""
        for i in coordinates:
            if i.isalpha():
                alpha=i
            else:
                num=i
        if ord(alpha)%2==1 :
            if int(num)%2==1:
                return False
            else:
                return True
        else:
            if int(num)%2==1:
                return True
            else:
                return False
        