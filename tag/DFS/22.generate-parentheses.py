#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n) -> List[str]:
        res = [] 
        def dfs(n, lc, rc, s): 
            if(lc == n) and (rc == n):
                res.append(s) 
            else:
                if (rc < n) and (rc < lc):
                    dfs(n, lc, rc+1, s+')')
                if lc < n:
                    dfs(n, lc+1, rc, s+'(')
        # n=3
        dfs (n,0,0,"")
        return res
# @lc code=end