"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        
        ans = [[1] * i for i in range(1, n+1)]  
        
        for i in range(1, n):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1] 
                
        return ans
    