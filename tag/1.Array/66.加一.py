#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''
        for i in digits:
            a += str(i)
        a = str(int(a) + 1)
        b = []
        for i in a:
            b.append(int(i))
        return b
        
            
# @lc code=end

