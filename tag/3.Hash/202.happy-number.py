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
            total = 0
            while n:
                total += (n%10)**2
                n //= 10
            return total 
        record = []
        while True:
            n = find(n)
            if n == 1: return True 
            # n!=1, possible dead loop? check it. 
            if n in record: return False 
            # add to hash
            else: record.append(n)
# @lc code=end

