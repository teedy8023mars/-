#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        while left < right:
            l_max, r_max = max(height[left], l_max), max(height[right], r_max)
            if l_max <= r_max:
                vol += l_max - height[left]
                left += 1
            else:
                vol += r_max - height[right]
                right -= 1
        return vol


# @lc code=end
