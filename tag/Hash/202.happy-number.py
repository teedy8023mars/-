#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
from numpy import record


class Solution:
    def isHappy(self, n: int) -> bool:
        def find(n):
            sum = 0
            while n:
                sum += (n%10)**2
                n = n//10
            return sum 
        # A set is unordered, unchangeable*, and unindexed
        seen = set()
        while 1:
            n = find(n)
            if n==1: return True
            if n in seen: return False
            else: seen.add(n) 
# @lc code=end

