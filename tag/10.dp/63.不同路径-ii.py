#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, nums: List[List[int]]) -> int:
        m,n = len(nums),len(nums[0])
        cur = [0]*n
        for j in range(n):
            if nums[0][j] == 1:
                break
            cur[j] = 1
        
        for i in range(1,m):
            for j in range(n):
                if nums[i][j] == 1:
                    cur[j] = 0
                elif j>0:
                    cur[j] = cur[j]+cur[j-1]
        return cur[n-1]
# @lc code=end

