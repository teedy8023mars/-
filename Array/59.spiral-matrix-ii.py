#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
from itertools import count


class Solution:
    def generateMatrix(self, n:int) -> List[List[int]]:
        nums = [[0]*n for _ in range(n)]
        x = y = 0
        loop = mid = n//2
        count = 1
        # offset 递增，先填外圈->再填内圈
        for offset in range(1, loop + 1):
            # x 不变，y向右递增至offset
            for i in range(y, n - offset):
                nums[x][i] = count
                count += 1
            # y 不变，x向下递增至offset 
            for i in range(x, n - offset):
                nums[i][n-offset] = count 
                count += 1
            # x 不变，y向左递减 3->2->1
            for i in range(n-offset,y,-1):
                nums[n-offset][i] = count
                count += 1
            # y 不变，x向上递增至
            for i in range(n-offset,x,-1):
                nums[i][y] = count
                count += 1
            x += 1 
            y += 1
        if n%2 != 0: nums[mid][mid] = count
        return nums
# @lc code=end

