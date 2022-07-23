#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import defaultdict


class Solution:
    def canConstruct(self, s1: str, s2: str) -> bool:
        """ s1 : intuitive """
        d2 = {}
        for i in s2:
            d2[i] = 1 if i not in d2 else d2[i]+1
        
        for k in s1:
            if k in list(d2.keys()) and d2[k]>0:
                d2[k] -= 1
            else: 
                return False 
        return True

        # """ s2: defaultdict """
        # hashmap = defaultdict(int)
        # for i in s1:
        #     hashmap[i] += 1

        # for j in s2:
        #     value = hashmap.get(j)
        #     if value == None or value == 0:
        #         return False 
        #     else: 
        #         hashmap[j] -= 1
        # return True
# @lc code=end

