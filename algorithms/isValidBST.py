#! python3
# -*- coding:UTF-8 -*-
"""
# 98. Validate Binary Search Tree
# Created on 2020/4/13 19:45
# isValidBST
# @author: ChangFeng
"""

# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode, min_val=-sys.maxsize, max_val=sys.maxsize) -> bool:
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.isValidBST(root.left, min_val, root.val) \
               and self.isValidBST(root.right, root.val, max_val)

    def isValidBST(self, root: TreeNode, left=sys.maxsize, right=-sys.maxsize) -> bool:
        return not root or left < root.val < right and \
               self.isValidBST(root.left, left, root.val) and \
               self.isValidBST(root.right, root.val, right)


def main():
    pass


if __name__ == '__main__':
    main()
