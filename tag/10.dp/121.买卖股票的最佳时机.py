#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # """brute force"""
        # ret = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         ret = max(prices[j]-prices[i],ret)
        # return ret

        # """greedy"""
        # if len(prices)>=1 and len(prices)<=10e5:
        #     low = 10e4
        #     result = 0
        #     for i in range(len(prices)):
        #         if prices[i]>=0 and prices[i]<=10e4:
        #             low = min(low,prices[i])
        #             result = max(result,prices[i]-low)
        #     return result

        """dp"""
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][0] = prices[0]
        dp[0][1] = 0
        for i in range(1,len(prices)):
            dp[i][0] = min(dp[i-1][0], prices[i])
            dp[i][1] = max(dp[i-1][1], prices[i] - dp[i-1][0])
        return dp[-1][1]

# @lc code=end

