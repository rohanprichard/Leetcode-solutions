class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxv = cur = temp = 0
        n = set()
        
        for i in range(1,len(s)):
            temp = len(n)
            n.add(s[i])
            if temp == len(n):
                cur = 0
                
            else:
                cur += 1
                
                if cur > maxv:
                    maxv = cur
                    
        return maxv
            
