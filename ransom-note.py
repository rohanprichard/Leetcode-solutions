class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine = magazine[:magazine.index(ransomNote[i])] + magazine[magazine.index(ransomNote[i]) + 1:]
            else:
                return False
        return True
