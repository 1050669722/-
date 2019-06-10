# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:01:51 2019

@author: Administrator
"""

class Solution:
    def sortArray(self, nums: list) -> list:
#        return self.heap_sort(nums)
        self.heap_sort(nums)
        return nums
        
#    def adjust_heap(self, nums, size, k):
#        lchild = 2*k+1
#        rchild = 2*k+2
#        Max = k
#        if k < size // 2: # while lchild < size:
#            if lchild < size and nums[lchild] > nums[Max]:
#                Max = lchild
#            if rchild < size and nums[rchild] > nums[Max]:
#                Max = rchild
#            if Max != k:
#                nums[Max], nums[k] = nums[k], nums[Max]
#                self.adjust_heap(nums, size, Max)
##            else:
##                break
##            k = Max
##            lchild = 2*k+1
##            rchild = 2*k+2
#        
#    def build_heap(self, nums, size):
#        for k in range(size//2)[::-1]:
#            self.adjust_heap(nums, size, k)  
#        
#    def heap_sort(self, nums):
#        size = len(nums)
#        self.build_heap(nums, size)
#        for k in range(size)[::-1]:
#            nums[0], nums[k] = nums[k], nums[0]
#            self.adjust_heap(nums, k, 0)
#        return nums
    
    
    
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
#        int[] a = new int[]{1,23,234,234,22,1,-1,0,3};
#        for (int i = a.length/2 -1; i >= 0; i--) { // 构建堆，因为a.length/2后面的数据都不会有左右节点了
#            buildHeap(a, i, a.length); 
#        }
#        System.out.println("开始排序前，构建的大根堆：");
#        for (int i : a) {
#            System.out.print(i + " ");
#        }
#        
#        System.out.println();
#        
#        // 开始不断的交换，移除，构建堆
#        for (int i = a.length - 1; i >=0; i--) {
#            swap(a, 0, i);   // 每次都把堆中第一个数和最后一个数交换
#            buildHeap(a, 0, i); // 第二个参数是i，就相当于是把i(最后一个数)移除堆，剩下的重新构建堆
#            System.out.println("第" + (a.length - i) + "次排序后的数组：");
#            for (int j : a) {
#                System.out.print(j + " ");
#            }
#            System.out.println();
#        }    
#        
#
#    public class HeapSort {
#        public static void buildHeap(int[] a, int i, int n) {
#            int leftChild = i * 2 + 1;
#            int rightChild = i * 2 + 2;
#            int largest = i;
#            /**
#             * 循环找出父节点和左右节点中最大的值，
#             * 并将最大值节点交换为父节点
#             */
#            while (leftChild < n) {
#                if (a[leftChild] > a[i]) {
#                    largest = leftChild;
#                }
#                if (rightChild < n && a[rightChild] > a[largest]) {
#                    largest = rightChild;
#                }
#                if (largest != i) {
#                    swap(a, largest, i);
#                } else {
#                    break;
#                }
#                
#                i = largest;
#                leftChild = i * 2 + 1;
#                rightChild = i * 2 + 2;
#            }
#            
#        }
#        
#        public static void swap(int[] a, int i, int j) {
#            int tmp = a[i];
#            a[i] = a[j];
#            a[j] = tmp;
#        }
#        
#        public static void main(String[] args) {
#            int[] a = new int[]{1,23,234,234,22,1,-1,0,3};
#            for (int i = a.length/2 -1; i >= 0; i--) { // 构建堆，因为a.length/2后面的数据都不会有左右节点了
#                buildHeap(a, i, a.length); 
#            }
#            System.out.println("开始排序前，构建的大根堆：");
#            for (int i : a) {
#                System.out.print(i + " ");
#            }
#            
#            System.out.println();
#            
#            // 开始不断的交换，移除，构建堆
#            for (int i = a.length - 1; i >=0; i--) {
#                swap(a, 0, i);   // 每次都把堆中第一个数和最后一个数交换
#                buildHeap(a, 0, i); // 第二个参数是i，就相当于是把i(最后一个数)移除堆，剩下的重新构建堆
#                System.out.println("第" + (a.length - i) + "次排序后的数组：");
#                for (int j : a) {
#                    System.out.print(j + " ");
#                }
#                System.out.println();
#            }
#            
#        }
#    }
            
solu = Solution()
nums = [3,7,6,4,1,9]
print(solu.sortArray(nums))            
            