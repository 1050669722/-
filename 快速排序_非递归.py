# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:47:29 2019

@author: Administrator
"""

'''
Quick Sort | Non-Recursion | In-place
'''

class Solution:
    def sortArray(self, nums: list) -> list:
        self.quick_sort(nums)
        return nums
        
    def quick_sort(self, nums):
        if len(nums) <= 1:
            return
        stack = []
        stack.append(len(nums) - 1)
        stack.append(0)
        while stack:
            left = stack.pop()
            right = stack.pop()
            idx = self.partition(nums, left, right)
            if left < idx - 1:
                stack.append(idx - 1)
                stack.append(left)
            if idx + 1 < right:
                stack.append(right)
                stack.append(idx + 1)
    
    def partition(self, nums, left, right):
        key = nums[left]
        while left < right:
            while left < right and nums[right] >= key:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= key:
                left += 1
            nums[right] = nums[left]
        nums[left] = key
        return left
        
solu = Solution()
nums = [3,7,6,4,1,9]
solu.sortArray(nums)
print(nums)
