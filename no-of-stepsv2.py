class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        while num > 0:
            if num & 1:
                c += 1
                num -= 1
            else:
                c += 1
                num = int(num/2)
        return c
            