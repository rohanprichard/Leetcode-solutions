# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import floor


class Solution:
    def __init__(self) -> None:
        self.n = 0
        self.total = 0
        self.ans = 0

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.checker(root)
        print(self.ans)
        return self.ans
        
    def checker(self, root):

        self.tf(root)
        if root.val == floor(self.total / self.n):
            self.ans += 1
        self.rs()

        if root.left:
            self.checker(root.left)
        
        if root.right:
            self.checker(root.right)
        
        return

    def tf(self, root):

        self.count()
        self.totalsum(root.val)

        if root.left:
            self.tf(root.left)
        
        if root.right:
            self.tf(root.right)
        
        return
        
    def count(self):
        self.n += 1
    
    def totalsum(self, n):
        self.total += n
    
    def rs(self):
        self.n = 0
        self.total = 0

