#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash = dict()
        for n1 in nums1:
            for n2 in nums2:
                hash[n1+n2] = 1 if n1 + n2  not in hash else hash[n1+n2] + 1
        # if the -(a+b) exists in nums3 and nums4, we shall add the count
        count = 0
        for n4 in nums4:
            for n3 in nums3:
                key = - n4 - n3
                if key in hash:
                    count += hash[key]
        return count
# @lc code=end

