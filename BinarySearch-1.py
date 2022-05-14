class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r,pivot
        n = int(floor(len(nums)/2))
        print(n, nums[n], nums)
        
        if nums[n] == target:
            return n
        elif len(nums) == 1 or len(nums) == 0:
            print("active")
            return -1
        
        if nums[n] > target:
            return self.search(nums[:n], target)
        else:
            return self.search(nums[n+1:], target) + n+1