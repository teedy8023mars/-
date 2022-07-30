#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        """solution 1: two pointers"""
        # left, right = 0, len(n)-1
        # while left < right:
        #     if n[left] + n[right] == target:
        #         return [left+1, right+1]
        #     if n[left] + n[right] > target:
        #         right -= 1
        #     if n[left] + n[right] < target:
        #         left += 1

        """solution 2: hashmap"""
        hash = {}
        for i,v in enumerate(n):
            if target - v in hash:
                return [hash[target-v]+1, i + 1]
            else:
                hash[v] = i
# @lc code=end

