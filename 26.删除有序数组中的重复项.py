#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                # diff, then self-replace
                nums[x] = nums[i]
                x += 1
            # if equal, x stays, i move forward
        return x
# @lc code=end

