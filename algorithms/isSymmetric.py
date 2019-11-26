#! python3
# -*- coding:UTF-8 -*-
"""
# 101. Symmetric Tree
# Created on 2019/11/26 16:28
# isSymmetric
# @author: ChangFeng
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def isMirror(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 or not node2:
                return node1 == node2
            if node1.val != node2.val:
                return False

            return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)

        return isMirror(root.left, root.right)


def main():
    h1 = TreeNode(1)
    h1.left = TreeNode(2)
    h1.right = TreeNode(3)
    # h1.left.left = TreeNode(3)
    # h1.left.right = TreeNode(4)
    # h1.right.left = TreeNode(4)
    # h1.right.right = TreeNode(3)
    test_case = [h1]
    max_depth = Solution().isSymmetric(*test_case)
    print(max_depth)


if __name__ == '__main__':
    main()
