class Solution:
    def printGfg(self, n: int) -> None:
        # code here
        if n == 0:
            return
        self.printGfg(n-1)
        print("GFG", end=" ")
