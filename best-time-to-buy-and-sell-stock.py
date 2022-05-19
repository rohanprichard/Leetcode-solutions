class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)-1
        ans = 0
        curSum = 0
        
        for i in range(n):
            
            curSum += prices[i+1] - prices[i]
            if curSum < 0:
                curSum = 0
            if ans < curSum:
                ans = curSum
            
        return ans