# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:47:29 2019

@author: Administrator
"""

class Solution:
    def sortArray(self, nums: list) -> list:
#        return self.quick_sort(nums)
        self.quick_sort(nums)
        return nums
    
#    def quick_sort(self, nums):
#        if len(nums) < 2:
#            return nums
#        stack = []
#        stack.append(len(nums)-1)
#        stack.append(0)
#        while stack:
#            l = stack.pop()
#            r = stack.pop()
#            idx = self.partition(nums, l, r)
#            if l < idx-1:
#                stack.append(idx-1)
#                stack.append(l)
#            if idx+1 < r:
#                stack.append(r)
#                stack.append(idx+1)
#        return nums
#        
#    def partition(self, nums, left, right):
#        key = nums[left]
#        while left < right:
#            while left < right and nums[right] >= key:
#                right -= 1
#            nums[left] = nums[right]
#            while left < right and nums[left] <= key:
#                left += 1
#            nums[right] = nums[left]
#        nums[left] = key
#        return left
        
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
#print(solu.quick_sort(nums))
solu.sortArray(nums)
print(nums)