#! python3
# -*- coding:UTF-8 -*-
"""
114. Flatten Binary Tree to Linked List
# Created on 2020/1/7 18:32
# flatten
# @author: ChangFeng
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pre = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        reversed preorder
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.pre
        root.left = None
        self.pre = root


def main():
    pass


if __name__ == '__main__':
    main()
