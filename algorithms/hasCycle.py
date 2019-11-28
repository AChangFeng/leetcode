#! python3
# -*- coding:UTF-8 -*-
"""
# 141. Linked List Cycle
# Created on 2019/11/28 17:11
# hasCycle
# @author: ChangFeng
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def main():
    pass


if __name__ == '__main__':
    main()
