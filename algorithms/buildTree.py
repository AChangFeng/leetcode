#! python3
# -*- coding:UTF-8 -*-
"""
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Created on 2020/1/9 17:39
# buildTree
# @author: ChangFeng
"""
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        先序遍历中，第一个一定是根节点
        根节点后面是根节点的左子节点
        根节点的右子节点的相对位置为：根节点的左子节点+（根节点在中序数组中的位置-中序数组的起点）
        因为先序遍历遍历完左边的所有子孙节点才会遍历到右节点，所以是左子节点加上左子节点的所有子孙节点
        左子节点的左右子孙节点也就是根节点在中序数组中左边的节点
        """

        def helper(pre_start, in_start, in_end):
            if pre_start > len(preorder) - 1 or in_start > in_end:
                return None
            index = 0
            root = TreeNode(preorder[pre_start])
            for i in range(in_start, in_end + 1):
                if inorder[i] == preorder[pre_start]:
                    index = i
            root.left = helper(pre_start + 1, in_start, index - 1)
            root.right = helper(pre_start + index - in_start + 1, index + 1, in_end)
            return root

        return helper(0, 0, len(preorder) - 1)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        先序遍历的节点一个一个pop出来，顺序就是root,left,right
        """
        if not inorder:
            return None
        d = {v: i for i, v in enumerate(inorder)}

        def helper(pre_order_deque, start, end):
            if start > end:
                return None
            v = pre_order_deque.popleft()
            idx = d[v]
            root = TreeNode(v)
            root.left = helper(pre_order_deque, start, idx - 1)
            root.right = helper(pre_order_deque, idx + 1, end)
            return root

        return helper(deque(preorder), 0, len(preorder) - 1)


def main():
    test_case = [[3, 9, 20, 15, 7],
                 [9, 3, 15, 20, 7]]
    Solution().buildTree(*test_case)


if __name__ == '__main__':
    main()
