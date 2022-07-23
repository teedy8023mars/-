#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 暴力解法
        # a = list(map(lambda x:x**2,nums))
        # a.sort()
        # return a

        # 双指针
        result = [0 for x in range(len(nums))]
        left, right, i = 0, len(nums)-1, len(nums)-1
        while left<=right:
            r = nums[right]**2
            l = nums[left]**2
            if r>=l:
                result[i]=r
                right -= 1
            else:
                result[i]=l
                left += 1
            i-=1
        return result
        
# @lc code=end

