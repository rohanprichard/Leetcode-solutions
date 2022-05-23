class Solution:
        
    def romanToInt(self, s: str) -> int:
        vals = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        sum = 0
        prob = self.stringsplit(s)
        for i in prob:
            if len(i) == 1: 
                sum += vals[i]
            else:
                sum =  sum + vals[i[1]] - vals[i[0]]
        return sum
    
    def stringsplit(self, s):
        end = []
        flag = 0
        temp = ""
        for i in range(len(s)):
            if flag == 1:
                flag = 0
                continue
            temp = s[i]
            try:
                if temp  == 'I':
                    if s[i+1] in "VX":
                        temp += s[i+1]
                        flag = 1
                
                if temp  == 'X':
                    if s[i+1] in "LC":
                        temp += s[i+1]
                        flag = 1
                        
                if temp  == 'C':
                    if s[i+1] in "DM":
                        temp += s[i+1]
                        flag = 1  
            except:
                pass
            end.append(temp)

        return end

n = Solution()
print(n.romanToInt("MCMXCIV"))
print(n.romanToInt("LVIII"))
print(n.romanToInt("III"))