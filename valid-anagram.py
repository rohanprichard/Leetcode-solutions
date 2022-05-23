class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if not len(s) == len(t):
            return False
        
        st = set(list(s))

        for i in st:
            if s.count(i) == t.count(i):
                continue
            else: 
                return False

        return True
    
        
