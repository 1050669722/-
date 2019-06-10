# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:01:51 2019

@author: Administrator
"""

'''
Heap Sort | Recursion | In-place
'''

class Solution:
    def sortArray(self, nums: list) -> list:
        self.heap_sort(nums)
        return nums
    
    def adjust_heap(self, nums, size, k):
        lchild = 2*k + 1
        rchild = 2*k + 2
        Max = k
        if k < size//2:
            while lchild < size and nums[lchild] > nums[Max]:
                Max = lchild
            while rchild < size and nums[rchild] > nums[Max]:
                Max = rchild
            if Max != k:
                nums[k], nums[Max] = nums[Max], nums[k]
                self.adjust_heap(nums, size, Max)
    
    def build_heap(self, nums, size):
        for k in range(size//2)[::-1]:
            self.adjust_heap(nums, size, k)
    
    def heap_sort(self, nums):
        size = len(nums)
        self.build_heap(nums, size)
        for k in range(size)[::-1]:
            nums[0], nums[k] = nums[k], nums[0]
            self.adjust_heap(nums, k, 0)

solu = Solution()
nums = [3,7,6,4,1,9]
print(solu.sortArray(nums))
