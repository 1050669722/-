# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:32:42 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        ans = []
        ans += self.inorderTraversal(root.left)
        ans.append(root.val)
        ans += self.inorderTraversal(root.right)
        return ans
            