#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/28 9:04
# uniquePaths
# @author: ChangFeng
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for x in range(m):
            dp[0][x] = 1
        for y in range(n):
            dp[y][0] = 1
        for x in range(1, m):
            for y in range(1, n):
                dp[y][x] = dp[y][x - 1] + dp[y - 1][x]
        return dp[n - 1][m - 1]

    def uniquePaths1(self, m: int, n: int) -> int:
        # 初始化第一列
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # 除第一行外，每一行都是上一列+之前的这一列
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1] if m and n else 0


def main():
    test_case = [7, 3]
    print(Solution().uniquePaths(*test_case))  # 28
    test_case = [7, 3]
    print(Solution().uniquePaths1(*test_case))  # 28


if __name__ == '__main__':
    main()
