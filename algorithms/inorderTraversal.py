#! python3
# -*- coding:UTF-8 -*-
"""
# 94. Binary Tree Inorder Traversal
# Created on 2019/12/8 11:16
# inorderTraversal
# @author: ChangFeng
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversalUsingRecursive(self, root: TreeNode) -> List[int]:
        """
        recursive solution
        :param root:
        :return:
        """
        ans = []

        def helper(r: TreeNode):
            if not r:
                return
            helper(r.left)
            ans.append(r.val)
            helper(r.right)

        helper(root)
        return ans

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        iterative solution
        :param root:
        :return:
        """
        ans, stack, curr = [], [], root
        while curr or stack:
            # left
            while curr:
                stack.append(curr)
                curr = curr.left
            # backtrack
            curr = stack.pop()
            ans.append(curr.val)
            # right
            curr = curr.right
        return ans


def main():
    pass


if __name__ == '__main__':
    main()
