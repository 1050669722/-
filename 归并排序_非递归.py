# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:18:30 2019

@author: Administrator
"""

'''
Merge Sort, Non-Recursion
'''

class Solution:
    def sortArray(self, nums: list) -> list:
        return self.merge_sort(nums)

    def merge(self, nums, head, mid, tail):
        p = head
        q = mid + 1
        k = head
        temp = nums.copy()
        while p<=mid and q<=tail:
            if temp[p] <= temp[q]:
                nums[k] = temp[p]
                p += 1
                k += 1
            else:
                nums[k] = temp[q]
                q += 1
                k += 1
        if p <= mid:
            nums[k:tail+1] = temp[p:mid+1]
        if q <= tail:
            nums[k:tail+1] = temp[q:tail+1]
           
    def merge_sort(self, nums):
        m = 1
        while m < len(nums):
            head = 0
            while head < len(nums):
                mid = head + m - 1
                tail = min(head + 2*m - 1, len(nums) - 1)
                self.merge(nums, head, mid, tail)
                head += 2*m
            m *= 2
        return nums

solu = Solution()
nums = [5,2,3,1]
print(solu.merge_sort(nums))
