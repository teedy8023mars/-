#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n) -> List[str]:
        if n <= 0: return []
        res = []

        def dfs(paths, left, right):
            if left>n or right>left:return 
            if len(paths)==n*2:
                res.append(paths)
                return 
            dfs(paths+'(', left+1, right)
            dfs(paths+')', left, right+1)
        dfs('',0,0)
        return res


# @lc code=end

