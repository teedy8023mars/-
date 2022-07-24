#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, res: str, k: int) -> str:
        def rev(str):
            left, right = 0, len(str)-1
            while left < right:
                str[left], str[right] = str[right], str[left]
                left += 1
                right -=1
            return str

        for i in range(0, len(res), 2 * k):
            res = list(res)
            res[i:i + k] = rev(res[i: i + k])
        
        return ''.join(res)
# @lc code=end

