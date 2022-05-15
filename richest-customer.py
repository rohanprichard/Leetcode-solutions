class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        cusnos = len(accounts)
        banknos = len(accounts[0])
        rich = [0] * cusnos
        
        for i in range(cusnos):
            rich[i] = sum(accounts[i])
            
        return max(rich)