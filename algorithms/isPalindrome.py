#! python3
# -*- coding:UTF-8 -*-
"""
# 234. Palindrome Linked List
# Created on 2019/11/28 17:35
# isPalindrome
# @author: ChangFeng
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if not head.next:
            return True
        pre = None
        slow = fast = head
        # 移动到中间位置
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        if fast:
            # 奇数个
            slow = slow.next
        # 前半部分翻转
        pre, cur, nxt = None, head, head.next
        while nxt:
            cur.next = pre
            pre, cur, nxt = cur, nxt, nxt.next
        cur.next = pre
        # 对比
        while cur and slow:
            if cur.val != slow.val:
                return False
            cur = cur.next
            slow = slow.next
        if cur or slow:
            return False
        return True


def main():
    head = ListNode('1')
    head.next = ListNode('0')
    head.next.next = ListNode('0')
    test_case = head
    print(Solution().isPalindrome(test_case))
    head = ListNode('1')
    head.next = ListNode('2')
    head.next.next = ListNode('2')
    head.next.next.next = ListNode('1')
    test_case = head
    print(Solution().isPalindrome(test_case))


if __name__ == '__main__':
    main()
