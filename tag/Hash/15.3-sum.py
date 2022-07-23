#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
            # impossible to sum up to zero
                continue
            # 去重：nums[i]要加进去sum，下一次遍历的时候不把相同的计算进去
            if i>=1 and nums[i] == nums[i-1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum>0:
                    right -= 1
                elif sum<0:
                    left += 1
                else:
                    #[-2,-2,0,0,2,2]
                    ans.append([nums[i],nums[left],nums[right]])
                    left += 1
                    # 与i的去重思路相同，下一次遍历相同的left和right不计入sum
                    while left < right and nums[left]==nums[left+1]: 
                        left += 1
        return ans

# @lc code=end

