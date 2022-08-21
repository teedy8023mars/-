#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,v in enumerate(nums):
            remainder = target - v
            if remainder not in seen:
                seen[v] = i 
            else:
                return [seen[remainder],i]
# @lc code=end

