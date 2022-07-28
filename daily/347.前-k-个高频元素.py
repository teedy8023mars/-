#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import re


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i,v in enumerate(nums):
            seen[v] = 1 if v not in seen else seen[v]+1
        ret = []
        seen = dict(sorted(seen.items(),key=lambda x:x[1],reverse=True))            
        for i in list(seen.keys()):
            ret.append(i)
        return ret[:k]
            
# @lc code=end

