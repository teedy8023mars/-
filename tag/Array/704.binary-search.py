#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums: return -1
        left, right = 0, len(nums)
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target: 
                return mid 
            if nums[mid] >= target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
# @lc code=end

