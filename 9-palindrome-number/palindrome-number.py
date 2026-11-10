class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x > 1 and x < 9:
            return True
        dup = x
        ans = 0
        while dup > 0:
            ans = (ans*10) + (dup%10)
            dup = dup//10
            print(ans, dup)
        print(ans)
        if ans == x :
            return True
        return False
