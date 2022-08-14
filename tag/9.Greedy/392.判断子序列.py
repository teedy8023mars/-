#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0: return True
        if len(s)>len(t):return False 
        index = 0
        for i in range(len(t)):
            if index != len(s) and t[i] == s[index]:
                index += 1
        return index == len(s)
# @lc code=end