#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""
import functools
import time


class Solution:
    def clumsy(self, n: int) -> int:
        magic = [1, 2, 2, -1, 1, 2, 6, 7]
        return n + (magic[n % 4]) if n > 4 else magic[n + 3]


def main():
    print(Solution().clumsy(4))


if __name__ == '__main__':
    main()
