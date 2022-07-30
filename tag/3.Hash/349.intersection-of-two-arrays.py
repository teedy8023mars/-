#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret=[]
        for i in nums2:
            if i not in ret and i in nums1:
                ret.append(i)
        return ret

# @lc code=end

