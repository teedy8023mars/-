#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, r: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(r) - 1
        while left < right:
            r[left], r[right] = r[right],r[left]
            left += 1
            right -= 1
        return ''.join(r)    

# @lc code=end

