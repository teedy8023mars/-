#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, res: str, k: int) -> str:
        def rev(res):
            left, right = 0, len(res)-1
            while left < right:
                res = list(res)
                res[left], res[right] = res[right],res[left]
                left += 1
                right -= 1
            return res
        
        for i in range(0,len(res),2*k):
            res = list(res)
            res[i:i+k] = rev(res[i:i+k])
        return ''.join(res)
# @lc code=end

