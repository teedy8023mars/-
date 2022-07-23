#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        sum=index=0
        for i in range(len(nums)):
            sum += nums[i]
            while sum>=target:
                res = min(res, i-index+1)
                sum -= nums[index]
                index += 1
        return 0 if res == float('inf') else res
# @lc code=end

