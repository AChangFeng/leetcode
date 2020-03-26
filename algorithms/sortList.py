#! python3
# -*- coding:UTF-8 -*-
"""
# 148. Sort List
# Created on 2020/3/25 18:48
# sortList
# @author: ChangFeng
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        核心思想就是归并排序，从前往后，每次分成1*n大小的两个链表，然后合并，
        直到2n大于数据长度为止
        """
        dummy = ListNode(0)
        dummy.next = head
        l = [0, 0]
        done = True if not head else False
        step = 1
        while not done:
            done = True
            pre = dummy
            remaining = pre.next
            while remaining:
                # split
                for i in range(2):
                    l[i] = remaining
                    tail = None
                    for j in range(step):
                        if not remaining:
                            break
                        tail = remaining
                        remaining = remaining.next
                    if tail:
                        tail.next = None

                # 如果分成两个List后没有剩余，说明处理完了
                done = done and not remaining

                # merge
                if l[-1]:
                    while l[0] or l[-1]:
                        if not l[-1] or l[0] and l[0].val <= l[-1].val:
                            idx = 0
                        else:
                            idx = 1
                        pre.next = l[idx]
                        l[idx] = l[idx].next
                        pre = pre.next
                    pre.next = None
                else:
                    pre.next = l[0]

            step *= 2
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        def split(node):
            prev, slow, fast = None, node, node
            while fast and fast.next:
                prev, slow, fast = slow, slow.next, fast.next.next
            if prev:
                prev.next = None
            return node, slow

        def merge(a, b):
            res = ListNode(0)
            curr = res
            while a and b:
                if a.val < b.val:
                    curr.next = curr = a
                    a = a.next
                else:
                    curr.next = curr = b
                    b = b.next
            curr.next = a or b
            return res.next

        if not head or not head.next:
            return head
        return merge(*map(self.sortList, split(head)))

    def sortList(self, head: ListNode) -> ListNode:
        """
        cheat
        """
        vals = []
        tmp = head
        while tmp:
            vals.append(tmp.val)
            tmp = tmp.next
        vals.sort()
        count, tmp = 0, head
        while tmp:
            tmp.val = vals[count]
            count += 1
            tmp = tmp.next
        return head


def main():
    node1 = ListNode(4)
    node2 = ListNode(2)
    node3 = ListNode(1)
    node4 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    Solution().sortList(node1)


if __name__ == '__main__':
    main()
