#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import re


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """solution 1"""
        # seen = {}
        # for i,v in enumerate(nums):
        #     seen[v] = 1 if v not in seen else seen[v]+1
        # ret = []
        # seen = dict(sorted(seen.items(),key=lambda x:x[1],reverse=True))            
        # for i in list(seen.keys()):
        #     ret.append(i)
        # return ret[:k]
        
        """solution 2"""
        # init a counter
        hash = {}
        for num in nums:
            hash[num] = 1 if num not in hash else hash[num]+1 
        keys = list(hash.keys())
        vals = list(hash.values())
        ret = []
        for i in range(k):
            m = max(vals)
            index = vals.index(m)
            vals[index] = 0
            ret.append(keys[index])
        return ret
# @lc code=end

