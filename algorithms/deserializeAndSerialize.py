#! python3
# -*- coding:UTF-8 -*-
"""
# 297. Serialize and Deserialize Binary Tree
# Created on 2020/4/15 18:55
# deserializeAndSerialize
# @author: ChangFeng
"""

# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def do_serialize(node):
            if node:
                vals.append(str(node.val))
                do_serialize(node.left)
                do_serialize(node.right)
            else:
                vals.append("#")

        vals = []
        do_serialize(root)
        return " ".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def do_deserialize():
            if not vals:
                return None
            val = vals.pop(0)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = do_deserialize()
            node.right = do_deserialize()
            return node

        vals = data.split()
        return do_deserialize()


class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.
        cheating
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = ""
        queue = deque([])
        queue.append(root)
        while queue:
            curr = queue.popleft()
            ans += (str(curr.val) if curr else "null") + ","
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
        return str(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        data = data[:-1].split(', ')
        if not data:
            return None
        root = TreeNode(data[0])
        queue = deque([])
        queue.append(root)
        for i in range(1, len(data), 2):
            if not queue:
                break
            curr = queue.popleft()
            if data[i]:
                curr.left = TreeNode(data[i])
                queue.append(curr.left)
            if data[i + 1]:
                curr.right = TreeNode(data[i + 1])
                queue.append(curr.right)

        return root


class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.
        cheating
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = ""
        queue = deque([])
        queue.append(root)
        while queue:
            curr = queue.popleft()
            ans += (str(curr.val) if curr else "#") + ","
            if curr:
                queue.append(curr.left)
                queue.append(curr.right)
        return str(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        data = data[:-1].split(',')
        if not data:
            return None
        root = TreeNode(data[0])
        queue = deque([])
        queue.append(root)
        for i in range(1, len(data), 2):
            if not queue:
                break
            curr = queue.popleft()
            if data[i] != '#':
                curr.left = TreeNode(data[i])
                queue.append(curr.left)
            if data[i + 1] != '#':
                curr.right = TreeNode(data[i + 1])
                queue.append(curr.right)

        return root


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    codec = Codec2()
    data = codec.serialize(root)
    print(data)
    root1 = codec.deserialize(data)
    print(root1)


if __name__ == '__main__':
    main()
