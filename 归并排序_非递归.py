# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:18:30 2019

@author: Administrator
"""

#用递归的好处就是逻辑简单，符合人的直观思维

#那么应该还有一种不使用递归的实现

#------------非递归-------------------
class Solution:
    def sortArray(self, nums: list) -> list:
        return self.merge_sort(nums)

#    def merge_sort(self, nums):
#        i = 1 #第一次排序的数组规模长度的一半
#        #建立临时数组，防止占用内存过大
#        tmp = [0] * len(nums) #类似于np.zeros()的作用
#        while i < len(nums):#100:# #2个2个排，4个4个排，8个8个排，16个16个排，直到间隔大于等于数组长度
#            low = 0 #初始化
#            while low < len(nums):
#                mid = low+i
#                high = min(low+2*i, len(nums))#low+2*i# #防止索引超出范围
#                if mid < high:
#                    self.merge(nums, low, mid, high, tmp)
#                low += 2*i
#            i *= 2
#        return nums
#     
#    def merge(self, nums, low, mid, high, tmp):
#        i = low
#        j = mid
#        k = low #tmp的索引起始位置
#        while i < mid and j <= high:
#            if nums[i] < nums[j]:
#                tmp[k] = nums[i]
#                k += 1
#                i += 1
#            else:
#                tmp[k] = nums[j]
#                j += 1
#                k += 1
#        # 如果左数组还有剩余
#        if i < mid:
#            tmp[k:high+1] = nums[i:mid]
#        # 如果右数组还有剩余
#        if j <= high:
#            tmp[k:high+1] = nums[j:high+1]
#        # 排好序的部分替换掉原来的乱序
#        print(tmp)
#        nums[low:high+1] = tmp[low:high+1]
        
#------------非递归-------------------
#    def merge_sort(self, nums):
#        i = 1 #第一次排序的数组规模长度的一半
#        #建立临时数组，防止占用内存过大
#        tmp = [0] * len(nums)
#        while i < len(nums):
#            low = 0 #初始化
#            while low < len(nums):
#                mid = low+i
#                high = min(low+2*i, len(nums))
#                if mid < high:
#                    self.merge(nums, low, mid, high, tmp)
#                    print(nums)
#                low += 2*i
#            i *= 2
#        return nums
#     
#    def merge(self, nums, low, mid, high, tmp):
#        i = low
#        j = mid
#        k = low #tmp的索引起始位置
#        while i < mid and j <= high:
#            if nums[i] < nums[j]:
#                tmp[k] = nums[i]
#                k += 1
#                i += 1
#            else:
#                tmp[k] = nums[j]
#                j += 1
#                k += 1
#        # 如果左数组还有剩余
#        if i < mid:
#            tmp[k:high+1] = nums[i:mid]
#        # 如果右数组还有剩余
#        if j <= high:
#            tmp[k:high+1] = nums[j:high+1]
#        # 排好序的部分替换掉原来的乱序
#        nums[low:high+1] = tmp[low:high+1]
        
# =============================================================================
#     def merge(self, nums, low, mid, high):
#         i = low
#         j = mid + 1
#         b = nums.copy() #[0] * len(nums)
#         for k in range(low, high+1):
#             if i>mid:
#                 nums[k] = b[j]
#                 j += 1
#             elif j>high:
#                 nums[k] = b[i]
#                 i += 1
#             elif b[i]<=b[j]:
#                 nums[k] = b[i]
#                 i += 1
#             else:
#                 nums[k] = b[j]
#                 j += 1
#         
#     def merge_sort(self, nums):
#         i = 1
#         while i < len(nums):
#             low = 0
#             while low < len(nums):
#                 self.merge(nums, low, low+i-1, min(low+2*i-1, len(nums)-1))
#                 low += 2*i
#             i *= 2
#         return nums
# =============================================================================
        
#        for(int i=1;i<a.length;i *= 2) {
#    //第二层循环表示每两个自数组之间归并排序，确定起始和终止INDEX
#            for(int low=0;low<a.length;low += 2*i) {
#                    merge(a, low, low + i- 1, Math.min(low + 2*i - 1, a.length - 1));

    
#    def merge(self, nums, head, mid, tail):
#        p = head
#        q = mid + 1
#        k = head
#        temp = nums.copy()
#        while p<=mid and q<=tail:
#            if temp[p] <= temp[q]:
#                nums[k] = temp[p]
#                p += 1
#                k += 1
#            else:
#                nums[k] = temp[q]
#                q += 1
#                k += 1
#        if p <= mid:
#            nums[k:tail+1] = temp[p:mid+1]
#        if q <= tail:
#            nums[k:tail+1] = temp[q:tail+1]
#            
#    def merge_sort(self, nums):
#        m = 1
#        while m < len(nums):
#            head = 0
#            while head < len(nums):
#                mid = head + m - 1
#                tail = min(head + 2*m - 1, len(nums) - 1)
#                self.merge(nums, head, mid, tail)
#                head += 2*m
#            m *= 2
#        return nums
        
    def merge(self, nums, head, mid, tail):
        p = head
        q = mid
        k = head
        temp = nums.copy()
        while p<mid and q<tail:
            if temp[p] <= temp[q]:
                nums[k] = temp[p]
                p += 1
                k += 1
            else:
                nums[k] = temp[q]
                q += 1
                k += 1
        if p < mid:
            nums[k:tail] = temp[p:mid]
        if q < tail:
            nums[k:tail] = temp[q:tail]
            
    def merge_sort(self, nums):
        m = 1
        while m < len(nums):
            head = 0
            while head < len(nums):
                mid = head + m
                tail = min(head + 2*m, len(nums))
                self.merge(nums, head, mid, tail)
                head += 2*m
            m *= 2
        return nums

solu = Solution()
nums = [5,2,3,1]
print(solu.merge_sort(nums))


















#solu = Solution()
#nums = [3,7,6,4,1,9]
#print(solu.sortArray(nums))

#--------------------- 
#作者：冷咖啡离开杯垫 
#来源：CSDN 
#原文：https://blog.csdn.net/c838556614/article/details/88550933 
#版权声明：本文为博主原创文章，转载请附上博文链接！