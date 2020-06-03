#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2020/6/3 13:54
# getKthFromEnd
# @author: ChangFeng
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        i = 1
        slow = fast = head
        while fast:
            if i == k:
                break
            fast = fast.next
            i += 1
        if not fast:
            return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        return slow


def main():
    n1 = ListNode(1)
    # n2 = ListNode(2)
    # n1.next = n2
    # n3 = ListNode(3)
    # n2.next = n3
    # n4 = ListNode(4)
    # n3.next = n4
    # n5 = ListNode(5)
    # n4.next = n5
    print(Solution().getKthFromEnd(n1, 1).val)


if __name__ == '__main__':
    main()
