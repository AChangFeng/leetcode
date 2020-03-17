#! python3
# -*- coding:UTF-8 -*-
"""
# 236. Lowest Common Ancestor of a Binary Tree
# Created on 2020/3/17 19:05
# lowestCommonAncestor
# @author: ChangFeng
"""


# Definition
# for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        if both p and q exist in Tree rooted at root, then return their LCA
        if neither p and q exist in Tree rooted at root, then return null
        if only one of p or q (NOT both of them), exists in Tree rooted at root, return it
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root


def main():
    pass


if __name__ == '__main__':
    main()
