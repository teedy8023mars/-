#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:return -1
        if not needle:return 0
        return haystack.index(needle)
# @lc code=end

