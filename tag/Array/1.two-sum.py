#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = {}
        # for i,v in enumerate(nums):
        #     r = target - v
        #     if r in seen:
        #         return [i,seen[r]] 
        #     else:
        #         seen[v] = i
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target - nums[j] == nums[i]:
                    return [i,j]
                else:
                    continue
# @lc code=end

