#! python3
# -*- coding:UTF-8 -*-
"""
# 279. Perfect Squares
# Created on 2020/1/16 17:25
# numSquares
# @author: ChangFeng
"""
import math
import sys


class Solution:
    def numSquares(self, n: int) -> int:
        """
        BFS
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1
        cnt = 0
        to_check = {n}
        while to_check:
            cnt += 1
            tmp = set()
            for m in to_check:
                for n in lst:
                    if m < n:
                        continue
                    if m == n:
                        return cnt
                    tmp.add(m - n)
            to_check = tmp
        return cnt

    def numSquares(self, n: int) -> int:
        """
        dp
        """
        dp = [sys.maxsize for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            sqrt = int(math.sqrt(i))
            if sqrt * sqrt == i:
                dp[i] = 1
                continue
            for j in range(1, sqrt + 1):
                dif = i - j * j
                dp[i] = min(dp[i], dp[dif] + 1)
        return dp[-1]


def main():
    test_case = 12
    print(Solution().numSquares(test_case))


if __name__ == '__main__':
    main()
