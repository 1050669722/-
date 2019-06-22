# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:58:22 2019

@author: Administrator
"""

'''
Quick Sort | Recursion | In-place
'''

class Solution:
    def sortArray(self, nums: list) -> list:
        self.quick_sort(nums, 0, len(nums)-1)
        return nums
        
    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        head = left
        tail = right
        key = nums[left]
        while left < right:
            while left < right and nums[right] >= key:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= key:
                left += 1
            nums[right] = nums[left]
        nums[left] = key
        self.quick_sort(nums, head, left-1)
        self.quick_sort(nums, left+1, tail)
    
# test
solu = Solution()
nums = [3,7,6,4,1,9]
print(solu.sortArray(nums))
