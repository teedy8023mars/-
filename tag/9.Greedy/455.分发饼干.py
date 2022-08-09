#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        # max_no_kids is len(g), only has len(s)_no_of cookies
        ret = index = 0
        for i in s:
            # reached max_no_kids,break
            if ret == len(g):break
            # can fulfil the kid
            if i>=g[index]:
                ret += 1 
                index += 1
        return ret
# @lc code=end