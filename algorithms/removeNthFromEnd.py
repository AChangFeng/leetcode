#! python3
# -*- coding:UTF-8 -*-
"""
# 19. Remove Nth Node From End of List
# Created on 2020/4/2 18:52
# removeNthFromEnd
# @author: ChangFeng
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy
        for i in range(n + 1):
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return dummy.next


def main():
    head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    Solution().removeNthFromEnd(head, 1)
    print(head)


if __name__ == '__main__':
    main()
