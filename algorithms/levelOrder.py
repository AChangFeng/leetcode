#! python3
# -*- coding:UTF-8 -*-
"""
# 102. Binary Tree Level Order Traversal
# Created on 2019/12/26 19:08
# levelOrder
# @author: ChangFeng
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []

        def helper(nodes: List[TreeNode]) -> None:
            if not nodes:
                return
            vals = []
            children = []
            for node in nodes:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
                vals.append(node.val)
            if vals:
                ans.append(vals)
                helper(children)

        helper([root])
        return ans


def main():
    pass


if __name__ == '__main__':
    main()
