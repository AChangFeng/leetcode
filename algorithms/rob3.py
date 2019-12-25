#! python3
# -*- coding:UTF-8 -*-
"""
# 337. House Robber III
# Created on 2019/12/25 18:35
# rob3
# @author: ChangFeng
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node: TreeNode):
            """
            返回长度为2的元组，其中第一个数字表示抢当前节点能获取到的最大收益
            第二个数字表示抢当前节点能获取到的最大收益
            """
            if not node:
                return (0, 0)
            # 处理子节点
            left, right = helper(node.left), helper(node.right)

            # 计算出当前节点应该返回的元组
            # 抢当前节点，则不能抢子节点。所以当前节点的第一个数字等于node.val+子节点返回元组的第二个数字
            now = node.val + left[1] + right[1]
            # 不抢当前节点，可以抢子节点。所以当前节点的第二个数字等于子节点返回所有元组中数字的最大值
            later = max(left) + max(right)
            return (now, later)

        return max(helper(root))

    def rob(self, root: TreeNode) -> int:
        """
        TLE
        """
        if not root:
            return 0

        def rob_include(node: TreeNode):
            """
            抢当前节点
            """
            if not node:
                return 0
            return node.val + rob_exclude(node.left) + rob_exclude(node.right)

        def rob_exclude(node: TreeNode):
            """
            不抢当前节点
            """
            if not node:
                return 0
            return self.rob(node.left) + self.rob(node.right)

        # 返回抢或不抢根节点的最大值
        return max(rob_include(root), rob_exclude(root))


def main():
    pass


if __name__ == '__main__':
    main()
