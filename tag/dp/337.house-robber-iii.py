#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode):
        if not root:
            return [0, 0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        val_steal = root.val + left[1] + right[1]
        val_no_steal = max(left[0], left[1]) + max(right[0], right[1])
        return [val_steal, val_no_steal]
    def rob(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return max(res[0], res[1])
# @lc code=end

