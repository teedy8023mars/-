#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):return False
        if len(s) == 0: return True
        ret = 0
        for i in range(0, len(t)):
            if ret <= len(s) - 1 and s[ret]== t[i]:
                    ret += 1
        return ret==len(s)
# @lc code=end