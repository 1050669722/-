# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:02:23 2019

@author: Administrator
"""

class Solution:
    def sortArray(self, nums: list) -> list:
        return self.merge_sort(nums)
    
    def merge(self, left, right):
        p, q = 0, 0
        ans = []
        while p < len(left) and q < len(right):
            if left[p] <= right[q]:
                ans.append(left[p])
                p += 1
            else:
                ans.append(right[q])
                q += 1
        ans += left[p:]
        ans += right[q:]
        return ans
        
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            n = len(nums) // 2
            left = self.merge_sort(nums[:n])
            right = self.merge_sort(nums[n:])
            return self.merge(left, right)
        
solu = Solution()
nums = [3,7,6,4,1,9]
print(solu.merge_sort(nums))