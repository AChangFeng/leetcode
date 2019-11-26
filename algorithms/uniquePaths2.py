#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/29 9:09
# uniquePaths2
# @author: ChangFeng
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for x in range(m):
            for y in range(n):
                if obstacleGrid[y][x]:
                    dp[y][x] = 0
                else:
                    if x > 0 or y > 0:
                        dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
        return dp[-1][-1]

    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        obs = False
        for x in range(m):
            if obstacleGrid[0][x] or obs:
                dp[0][x] = 0
                obs = True
            else:
                dp[0][x] = 1
        obs = False
        for y in range(n):
            if obstacleGrid[y][0] or obs:
                dp[y][0] = 0
                obs = True
            else:
                dp[y][0] = 1
        for x in range(1, m):
            for y in range(1, n):
                if obstacleGrid[y][x]:
                    dp[y][x] = 0
                else:
                    dp[y][x] = dp[y - 1][x] + dp[y][x - 1]
        return dp[-1][-1]


def main():
    test_case = [[0, 1]]
    print(Solution().uniquePathsWithObstacles(test_case))
    test_case = [[1, 0]]
    print(Solution().uniquePathsWithObstacles(test_case))
    test_case = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(Solution().uniquePathsWithObstacles(test_case))
    test_case = [[0]]
    print(Solution().uniquePathsWithObstacles(test_case))
    test_case = [[1]]
    print(Solution().uniquePathsWithObstacles(test_case))
    test_case = [[0, 0]]
    print(Solution().uniquePathsWithObstacles(test_case))


if __name__ == '__main__':
    main()
