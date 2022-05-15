class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        strength = [0] * m
        res = [i for i in range(m)]
        
        for i in range(m):
            strength[i] = sum([x for x in mat[i]])
        
        for i in range(m):
            for j in range(m):
                if strength[i] <= strength[j]:
                    strength[i], strength[j] = strength[j], strength[i]
                    res[i], res[j] = res[j], res[i]
                    
                if strength[i] == strength[j]:
                    if res[i] <= res[j]:
                        res[i], res[j] = res[j], res[i]
        return res[:k]
        