#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ dict to count"""
        d1, d2 = {},{}
        for i in s:
            d1[i]=1 if i not in d1 else d1[i]+1
        for i in t:
            d2[i]=1 if i not in d2 else d2[i]+1
        return d1 == d2
        # return sorted(s)==sorted(t)
        
            
# @lc code=end


