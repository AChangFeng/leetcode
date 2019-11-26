#! python3
# -*- coding:UTF-8 -*-
"""
# 543. Diameter of Binary Tree
# Created on 2019/11/26 15:49
# diameterOfBinaryTree
# @author: ChangFeng
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        一个结点到另一个结点之间的最长路径，可以分解为所有结点的"左子结点最大路径+右子结点最大路径+1"中的最大值，
        也就是：max([left_depth+right_depth+1 for nodes ])
        :param root:
        :return:
        """
        self.ans = 0

        def depth(node: TreeNode):
            if not node:
                return 0
            l, r = depth(node.left), depth(node.right)
            self.ans = max(l + r, self.ans)
            return max(l, r) + 1

        depth(root)
        return self.ans


def main():
    pass


if __name__ == '__main__':
    main()
