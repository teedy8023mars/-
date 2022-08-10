#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
from configparser import MAX_INTERPOLATION_DEPTH


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """solution : 1"""
        # if not nums:return 0
        # l,r = 0,0
        # init = nums[0]
        # ret = 1
        # for i in range(len(nums)):
        #     if nums[i]>init:
        #         r+=1
        #         init = nums[i]
        #         ret = max(ret,r-l+1)
        #     else:
        #         l = r = i
        #         init = nums[i]
        #         ret = max(ret,r-l+1)
        # return ret
        """solution : 2"""
        if not nums: return 0
        cur = max_len = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                cur += 1
            else:
                max_len = max(max_len,cur)
                cur = 1
        return max(max_len,cur)
                
                
# @lc code=end