class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m+1]
        print(temp, nums2)
        for i in range(m+n):
            nums1[i] = min(min(temp), min(nums2))

        print(nums1)
