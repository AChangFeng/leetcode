#! python3
# -*- coding:UTF-8 -*-
"""
# 142. Linked List Cycle II
# Created on 2020/3/31 19:13
# detectCycle
# @author: ChangFeng
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        When fast and slow meet at point p, the length they have run are 'a+2b+c' and 'a+b'.
        Since the fast is 2 times faster than the slow. So a+2b+c == 2(a+b), then we get 'a==c'.
        So when another slow2 pointer run from head to 'q', at the same time,
        previous slow pointer will run from 'p' to 'q', so they meet at the pointer 'q' together.
        """
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow2 = head
                while slow2 != slow:
                    slow2 = slow2.next
                    slow = slow.next
                return slow
        return None


def main():
    pass


if __name__ == '__main__':
    main()
