#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
from urllib.request import AbstractBasicAuthHandler


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in  "".join((s[1:],s))
        print(s)
# a bcabcabcab c

# a cbabcacbab c
# @lc code=end

