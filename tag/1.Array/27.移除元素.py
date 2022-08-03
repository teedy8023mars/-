#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i to indicate found val
        i = 0
        for x in nums:
            # if x==val, skip, find next non-val to replace nums[i]
            if x != val:
                nums[i] = x
                # update i
                i += 1
        # return index i 
        return i
# @lc code=end

