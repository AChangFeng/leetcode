#! python3
# -*- coding:UTF-8 -*-
"""
# 155. Min Stack
# Created on 2019/11/28 11:05
# MinStack
# @author: ChangFeng
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.table = []

    def push(self, x: int) -> None:
        """
        每个节点存储一个键值对，
        key是从栈底到当前位置的最小元素，value是当前位置的元素
        :param x:
        :return:
        """
        if not self.table:
            self.table.append([x, x])
        else:
            self.table.append([min(self.table[-1][0], x), x])

    def pop(self) -> None:
        self.table.pop()

    def top(self) -> int:
        return self.table[-1][-1]

    def getMin(self) -> int:
        return self.table[-1][0]


def main():
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())


if __name__ == '__main__':
    main()
