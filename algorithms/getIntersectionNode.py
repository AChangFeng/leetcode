#! python3
# -*- coding:UTF-8 -*-
"""
# 160. Intersection of Two Linked Lists
# Created on 2019/11/29 9:59
# getIntersectionNode
# @author: ChangFeng
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None

        pa, pb = headA, headB
        achanged = bchanged = False
        while pa and pb:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
            if not pa and not achanged:
                pa = headB
                achanged = True
            if not pb and not bchanged:
                pb = headA
                bchanged = True
        return pa

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa, pb = headA, headB
        # 如果pa=pb=None，退出循环；或者pa=pb说明这一个结点就是答案
        while pa != pb:
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
        return pa


def main():
    intersectionNode = ListNode(7)
    intersectionNode.next = ListNode(8)
    intersectionNode.next.next = ListNode(9)
    headA = ListNode(1)
    headA.next = ListNode(3)
    headA.next.next = ListNode(5)
    headA.next.next.next = intersectionNode
    headB = ListNode(2)
    headB.next = ListNode(4)
    headB.next.next = ListNode(6)
    headB.next.next.next = intersectionNode

    test_case = [headA, headB]
    print(Solution().getIntersectionNode(*test_case))  # 7


if __name__ == '__main__':
    main()
