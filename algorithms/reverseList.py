# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre, curr, nxt = None, head, head.next
        while nxt:
            curr.next = pre
            pre, curr, nxt = curr, nxt, nxt.next
        curr.next = pre
        return curr


def main():
    pass


if __name__ == '__main__':
    main()
