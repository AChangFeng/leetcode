#! python3
# -*- coding:UTF-8 -*-
"""
# 437. Path Sum III
# Created on 2019/11/26 16:47
# pathSum
# @author: ChangFeng
"""

# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def helper(self, node, target):
        if not node:
            return 0
        ans = 0
        if node.val == target:
            ans += 1
        return ans + self.helper(node.left, target - node.val) + self.helper(node.right, target - node.val)

    def pathSum(self, root, sum):
        self.ans = 0

        def test(node, target):
            if not node:
                return
            if node.val == target:
                self.ans += 1
            test(node.left, target - node.val)
            test(node.right, target - node.val)

        def dfs(node):
            if not node:
                return
            test(node, sum)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans

    def pathSum(self, root, sum):
        self.cache = {0: 1}
        self.ans = 0

        def dfs(node, currSum):
            if not node:
                return
            currSum += node.val
            oldSum = currSum - sum
            self.ans += self.cache.get(oldSum, 0)
            self.cache[currSum] = self.cache.get(currSum, 0) + 1
            dfs(node.left, currSum)
            dfs(node.right, currSum)
            self.cache[currSum] -= 1

        dfs(root, 0)
        return self.ans


def main():
    # h1 = TreeNode(10)
    # h1.left = TreeNode(5)
    # h1.right = TreeNode(-3)
    # h1.left.left = TreeNode(3)
    # h1.left.right = TreeNode(2)
    # h1.right.right = TreeNode(11)
    # h1.left.left.left = TreeNode(3)
    # h1.left.left.right = TreeNode(-2)
    # h1.left.right.right = TreeNode(1)
    # test_case = [h1, 8]
    # max_depth = Solution().pathSum(*test_case)
    # print(max_depth)

    h1 = TreeNode(1)
    h1.right = TreeNode(2)
    h1.right.right = TreeNode(3)
    h1.right.right.right = TreeNode(4)
    h1.right.right.right.right = TreeNode(5)
    test_case = [h1, 3]
    max_depth = Solution().pathSum(*test_case)
    print(max_depth)


if __name__ == '__main__':
    main()
