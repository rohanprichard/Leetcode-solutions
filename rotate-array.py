class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = 0
        
        for i in range(k):
            nums.insert(0, nums.pop())
