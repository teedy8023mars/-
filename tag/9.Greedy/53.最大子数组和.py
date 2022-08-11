#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = cur = nums[0]
        for i in nums[1:]:
            cur = max(i,cur+i)
            ret = max(ret, cur)
        return ret
# @lc code=end