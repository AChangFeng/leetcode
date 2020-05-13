#! python3
# -*- coding:UTF-8 -*-
"""
# 124. Binary Tree Maximum Path Sum
# Created on 2020/5/13 20:20
# maxPathSum
# @author: ChangFeng
"""

# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        @see https://segmentfault.com/a/1190000003554858
        对于指定某个节点为根，最大的路径和有可能是一下几种情况：
        1、left_max+root.val
        2、right_max+root.val
        3、left_max+root.val+right_max（相当于一条横跨当前节点的路径）
        4、root.val
        这四种情况只是用来计算以当前节点根的最大路径，如果当前节点上面还有节点，那它的父节点是不能累加第三种情况的。
        所以要计算两个最大值，一个是当前节点下最大路径和，另一个是如果要连接父节点时最大的路径和。
        用前者更新全局最大量，用后者返回递归值就行了。
        连接父节点的最大路径是一、二、四这三种情况的最大值。
        当前节点的最大路径是一、二、三、四这四种情况的最大值。
        """
        max_val = -sys.maxsize

        def hepler(node):
            nonlocal max_val
            if not node:
                return 0
            left_max = hepler(node.left)
            right_max = hepler(node.right)
            curr_sum = max(left_max + node.val, right_max + node.val, node.val)
            max_val = max(max_val, curr_sum, left_max + node.val + right_max)

            return curr_sum

        hepler(root)
        return max_val


def main():
    pass


if __name__ == '__main__':
    main()
