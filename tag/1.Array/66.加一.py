#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """solution 1:"""
        # a = ''
        # for i in digits:
        #     a += str(i)
        # a = str(int(a) + 1)
        # b = []
        # for i in a:
        #     b.append(int(i))
        # return b

        """solution 2:"""
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            # no carrier, just return
            if digits[i] != 0:
                return digits
        # case when digits[i]==0, means got a carrier
        digits = [0]*(len(digits)+1)
        digits[0] = 1
        return digits
# @lc code=end