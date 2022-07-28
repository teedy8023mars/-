#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # find min, define a max, find max define a min
        res = float('inf')
        sum = 0
        index = 0
        for i in range(len(nums)):
            # keep adding the nums to sum
            sum += nums[i]
            # if sum gets bigger than target
            while sum>=target:
                # calculate current len
                res = min(res, i-index+1)
                # then subtract from left
                sum -= nums[index]
                # update index -> 1
                index += 1
        return 0 if res == float('inf') else res
# @lc code=end

