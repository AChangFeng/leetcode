#! python3
# -*- coding:UTF-8 -*-
"""
# 23. Merge k Sorted Lists
# Created on 2020/5/8 19:20
# mergeKLists
# @author: ChangFeng
"""

# Definition for singly-linked list.
import heapq
import sys
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        堆排序
        """
        l = []
        for head in lists:
            while head:
                heapq.heappush(l, head.val)
                head = head.next
        dummy = ListNode()
        pre = dummy
        while l:
            v = heapq.heappop(l)
            new_node = ListNode(v)
            pre.next = new_node
            pre = pre.next
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        依次比较
        """
        dummy = ListNode()
        pre = dummy
        tmp_list = []
        for node in lists:
            if node:
                tmp_list.append(node)
        lists = tmp_list

        while len(lists) > 0:
            min_val = sys.maxsize
            min_node_index = -1
            for i in range(len(lists)):
                if lists[i].val <= min_val:
                    min_val = lists[i].val
                    min_node_index = i
            min_val_node = lists[min_node_index]
            if min_val_node.next:
                lists[min_node_index] = lists[min_node_index].next
                min_val_node.next = None
            else:
                lists.remove(min_val_node)
            pre.next = min_val_node
            pre = pre.next
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        排序
        """
        vals = []
        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next
        dummy = ListNode()
        pre = dummy
        for val in sorted(vals):
            node = ListNode(val)
            pre.next = node
            pre = pre.next
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        分治
        类似归并排序
        """

        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            """
            合并两个有序链表
            """
            if not l1:
                return l2
            if not l2:
                return l1
            dummy = pre = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    pre.next = l1
                    l1 = l1.next
                else:
                    pre.next = l2
                    l2 = l2.next
                pre = pre.next
            if not l1:
                pre.next = l2
            else:
                pre.next = l1
            return dummy.next

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return mergeTwoLists(l, r)


def main():
    node11 = ListNode(1)
    node14 = ListNode(4)
    node15 = ListNode(5)
    node21 = ListNode(1)
    node23 = ListNode(3)
    node24 = ListNode(4)
    node32 = ListNode(2)
    node36 = ListNode(6)

    node11.next = node14
    node14.next = node15

    node21.next = node23
    node23.next = node24

    node32.next = node36
    node_list = [node11, node21, node32]
    print(Solution().mergeKLists(node_list))


if __name__ == '__main__':
    main()
