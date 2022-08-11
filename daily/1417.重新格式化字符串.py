#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        l = [c for c in s if c.isalpha()]
        d = [d for d in s if d.isdigit()]
        if abs(len(l) - len(d)) > 1:
            return ""
        ret = []
        flag = len(l) > len(d)
        while l or d:
            ret.append(l.pop() if flag else d.pop())
            flag = not flag
        return "".join(ret)
# @lc code=end
