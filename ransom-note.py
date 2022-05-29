class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        rans = {}
        
        for i in magazine:
            try:
                mag[i] += 1
            except:
                mag[i] = 1
        for i in ransomNote:
            try:
                rans[i] += 1
            except:
                rans[i] = 1
        
        for n in rans:
            try:
                if mag[n] - rans[n] < 0:
                    return False
            except:
                return False
            
        return True
                
        