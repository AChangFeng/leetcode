#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)


def main():
    print(Solution().trailingZeroes(25))


if __name__ == '__main__':
    main()
