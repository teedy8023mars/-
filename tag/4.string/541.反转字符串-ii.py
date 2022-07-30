#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for i in range(1,len(s),2*k):
            print(s[i])
            
# @lc code=end

