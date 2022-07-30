#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:return nums[0]
        ans1 = self.find(nums[1:n])
        ans2 = self.find(nums[0:n-1])
        return max(ans1,ans2)
        
        
    def find(self, nums):
        if len(nums)==1:return nums[0]
        if len(nums)==2:return max(nums[1],nums[0])
        dp = [0 for x in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
        
# @lc code=end

