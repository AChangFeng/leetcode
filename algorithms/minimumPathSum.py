#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/30 9:18
# minimumPathSum
# @author: ChangFeng
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [grid[0][0]]
        for y in range(1, n):
            dp.append(dp[-1] + grid[y][0])
        for x in range(1, m):
            for y in range(n):
                if y == 0:
                    dp[0] = dp[0] + grid[0][x]
                else:
                    dp[y] = min(dp[y], dp[y - 1]) + grid[y][x]
        return dp[- 1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        for x in range(m):
            for y in range(n):
                if x == 0:
                    if y > 0:
                        dp[y][x] = dp[y - 1][x] + grid[y][x]
                elif y == 0:
                    if x > 0:
                        dp[y][x] = dp[y][x - 1] + grid[y][x]
                else:
                    dp[y][x] = min(dp[y][x - 1], dp[y - 1][x]) + grid[y][x]
        return dp[-1][-1]

    def minPathSum22(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for x in range(m):
            for y in range(n):
                if x == 0:
                    if y > 0:
                        grid[y][x] = grid[y - 1][x] + grid[y][x]
                elif y == 0:
                    if x > 0:
                        grid[y][x] = grid[y][x - 1] + grid[y][x]
                else:
                    grid[y][x] += min(grid[y][x - 1], grid[y - 1][x])
        return grid[-1][-1]

    def minPathSum1(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        for x in range(1, m):
            dp[0][x] = dp[0][x - 1] + grid[0][x]
        for y in range(1, n):
            dp[y][0] = dp[y - 1][0] + grid[y][0]
        for x in range(1, m):
            for y in range(1, n):
                dp[y][x] = min(dp[y][x - 1], dp[y - 1][x]) + grid[y][x]
        return dp[-1][-1]

    def minPathSum11(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for x in range(1, m):
            grid[0][x] = grid[0][x - 1] + grid[0][x]
        for y in range(1, n):
            grid[y][0] = grid[y - 1][0] + grid[y][0]
        for x in range(1, m):
            for y in range(1, n):
                grid[y][x] += min(grid[y][x - 1], grid[y - 1][x])
        return grid[-1][-1]

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


def main():
    test_case = [[1]]
    print(Solution().minPathSum22(test_case))
    test_case = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(Solution().minPathSum22(test_case))


if __name__ == '__main__':
    main()
