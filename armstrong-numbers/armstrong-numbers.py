class Solution:
    def armstrongNumber(self, n: int) -> bool:
        # code here
        sum = 0
        dup = n
        while n > 0:
            sum += (n % 10) ** 3
            n=n//10
        if sum == dup:
            return True
        return False
