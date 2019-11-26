#! python3
# -*- coding:UTF-8 -*-
"""
# 21. Merge Two Sorted Lists
# Created on 2019/11/26 15:21
# mergeTwoLists
# @author: ChangFeng
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        txt = ""
        cur = self
        while cur:
            txt += str(cur.val)
            cur = cur.next
        return txt


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy = ListNode('/')
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                #while l1 and l1.val <= l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                #while l2 and l1.val > l2.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next


def main():
    l11 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(3)
    l14 = ListNode(4)
    l15 = ListNode(5)
    l11.next = l12
    l12.next = l13
    l13.next = l14
    l14.next = l15

    l21 = ListNode(3)
    l22 = ListNode(4)
    l23 = ListNode(5)
    l24 = ListNode(6)
    l25 = ListNode(7)
    l26 = ListNode(8)
    l21.next = l22
    l22.next = l23
    l23.next = l24
    l24.next = l25
    l25.next = l26
    head = Solution().mergeTwoLists(l11, l21)
    print(head)


if __name__ == '__main__':
    main()
