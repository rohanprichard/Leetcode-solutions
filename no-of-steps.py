class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.rec(num, 0)
        
    def rec(self, n, c):
        if n == 0:
            return c
        elif n & 1:
            return self.rec(int(n-1), c+1)
        else:
            return self.rec(int(n/2), c+1)
            