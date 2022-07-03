#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ recursion 1 """
        # if not l1 or not l2:
        #     # if l1 False, return l2, else l1
        #     return l1 or l2
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2
        """iteratively"""
        t1 = t2 = ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                t2.next = l1
                l1 = l1.next
            else:
                t2.next = l2
                l2 = l2.next
            t2 = t2.next
        # append the rest nodes of l1 or l2
        t2.next = l1 or l2 
        return t1.next

        
# @lc code=end

