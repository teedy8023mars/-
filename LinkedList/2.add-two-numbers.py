#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = r = ListNode(0)
        sum = carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry 
            carry = sum//10
            r.next = ListNode(sum%10)
            r = r.next
            if l2: l2 = l2.next
            if l1: l1 = l1.next
        if carry > 0:
            r.next = ListNode(1)
        return ret.next

# @lc code=end
