#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from bigO import BigO
from bigO import algorithm
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ret = []
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:continue
            for k in range(i+1,n):
                if k>i+1 and nums[k]==nums[k-1]: continue
                left = k+1
                right = n-1
                while left < right:
                    s = nums[i]+nums[k]+nums[left]+nums[right]
                    if s>target: right-=1
                    elif s<target: left+=1
                    else:
                        ret.append([nums[i],nums[k],nums[left],nums[right]])
                        while left < right and nums[left]==nums[left+1]:
                            left += 1
                        left += 1
        print(self.fourSum().test)
        return ret
                
# @lc code=end

