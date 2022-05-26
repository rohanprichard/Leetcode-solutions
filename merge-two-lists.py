# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        x = ListNode()
        y = x
        
        while list1 and list2:
            if list1.val < list2.val:
                y.next = ListNode(list1.val)
                list1 = list1.next
                y = y.next
            else:
                y.next = ListNode(list2.val)
                list2 = list2.next
                y = y.next
        
        if list1:
            y.next = list1
        elif list2:
            y.next = list2
        
        print(x)
        return x.next
            
