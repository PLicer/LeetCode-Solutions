class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        check = 0
        ans = 0
        num = x
        if ((x > 2**31 - 1) or (x < -2**31 )):
            return 0
        if x < 0:
            check = 1
        x = abs(x)
        while x > 0:
            ans = ans * 10 + x%10
            x = x//10

        if ans > 2**31 - 1 or ans < -2**31:
            return 0
        
        return ans if check == 0 else -(ans)
        

        