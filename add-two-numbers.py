"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        tot = 0
        a = l1
        b = l2
        head = ListNode(0)
        c = head
        while a or b:
            
            if a is None:
                a = ListNode(0,None)
                
            if b is None:
                b = ListNode(0,None)
            
            tot = a.val + b.val + carry
            
            carry = tot//10
            
            if carry == 1:
                tot-= 10
                
            head.next = ListNode(tot, None) 
            
            a = a.next
            b = b.next
            head = head.next
                
        if carry == 1:
            head.next = ListNode(1)
            
            
        return c.next
                
            
            
            
            