#! python3
# -*- coding:UTF-8 -*-
"""
# 138. Copy List with Random Pointer
# Created on 2020/4/8 18:54
# copyRandomList
# @author: ChangFeng
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.random:
            return str(self.val) + "," + str(self.random.val)
        else:
            return str(self.val)


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        hash table
        """
        dummy = Node(-1, head, None)
        curr = dummy.next
        pre = dummy
        need_random_nodes = []
        origin_copy_node_dict = {}
        while curr:
            copy = Node(curr.val, None, None)
            pre.next = copy
            origin_copy_node_dict[curr] = copy
            if curr.random:
                need_random_nodes.append((copy, curr.random))
            pre = pre.next
            curr = curr.next
        for copy, origin_random in need_random_nodes:
            copy.random = origin_copy_node_dict[origin_random]
        return dummy.next


def main():
    src = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    nodes = [Node(val, None, random) for val, random in src]
    pre = None
    for node in nodes:
        if not pre:
            pre = node
        else:
            pre.next = node
            pre = pre.next
        if node.random is not None:
            node.random = nodes[node.random]
    copy = Solution().copyRandomList(nodes[0])
    print(copy)


if __name__ == '__main__':
    main()
