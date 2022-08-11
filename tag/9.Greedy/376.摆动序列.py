#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """Greedy algorithm"""
        # ret = 1
        # p = q = 0 # trigger
        # for i in range(1,len(nums)):
        #     q = nums[i] - nums[i - 1]
        #     if p*q<=0 and q!=0:
        #         ret += 1
        #         p = q 
        # return ret

        """dp"""
        # i 0 作为波谷的最大长度
        # i 1 作为波峰的最大长度
        # dp是一个列表，列表中每个元素是长度为 2 的列表
        dp = []
        for i in range(len(nums)):
            dp.append([1,1])
            for j in range(i):
                # low point
                if nums[j] > nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                # high point
                if nums[j] < nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
        return max(dp[-1][0], dp[-1][1])
# @lc code=end