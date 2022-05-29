class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = 0
        while n:
            n &= n - 1
            temp += 1
        return temp
