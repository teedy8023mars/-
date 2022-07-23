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
    seen = {}
    def dfs(self,root:TreeNode):
        if not root:
            return [0,0]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        # 选root,但left[0],right[0]是相邻的，不能选
        val_steal = root.val + left[1] + right[1]
        # 不选root，左右分别选最大的
        val_no_steal = max(left[0],left[1]) + max(right[0],left[1])
        return [val_steal, val_no_steal]
        
    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.dfs(root)
        return max(res[0], res[1])
# @lc code=end

