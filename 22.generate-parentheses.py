#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(n,l,r,s):
            if (l==n and r==n):
                res.append(s)
            else:
                if l<n:
                    dfs(n,l+1,r,s+'(')
                if (r<n and r<l):
                    dfs(n,l,r+1,s+')')
        dfs(n,0,0,'')
        return res
# @lc code=end

