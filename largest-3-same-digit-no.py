class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ls = []
        temp = ''
        
        for i in num:
            temp += (i)
            
            if len(temp) == 3:
                if temp[0] == temp[1] and temp[1] == temp[2]:
                    ls.append(temp)
                temp = temp[1:]
                
        if len(ls) == 0:
            return ""
        return str(max(ls))
        