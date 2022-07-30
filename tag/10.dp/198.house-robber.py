#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size==1:return nums[0]
        if size==2:return max(nums[0],nums[1])
        dp = [0 for x in range(size)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        #偷窃第 i 间房屋，那么第 i - 1 间房屋就不能偷窃了，偷窃的最高金额为：前 i - 2 间房屋的最高总金额 + 第 i 间房屋的金额，即 dp[i] = dp[i - 2] + nums[i]；
        #不偷窃第 i 间房屋，那么第 i - 1 间房屋可以偷窃，偷窃的最高金额为：前 i - 1 间房屋的最高总金额，即 dp[i] = dp[i - 1]
        for i in range(2, size):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
# @lc code=end

