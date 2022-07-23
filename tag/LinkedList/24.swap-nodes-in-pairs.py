#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # """ Iterative """
        # if not head or not head.next:
        #     return head
        # first = head
        # second = head.next 
        # # 3->Null, 4->3
        # # 1->4, 2->1
        # first.next = self.swapPairs(second.next)
        # second.next = first 
        # return second
        """ Recursive """
        # 两个两个换，移动指针，不要4个两两换
        temp = ListNode(0)
        temp.next = head
        ans = temp
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return ans.next
        """
        time: O(n),n is the no. of nodes
        space:O(1)
        """

# @lc code=end

