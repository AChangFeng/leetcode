#! python3
# -*- coding:UTF-8 -*-
"""
# 221. Maximal Square
# Created on 2020/4/1 19:29
# maximalSquare
# @author: ChangFeng
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dp[i][j] represents the length of the square which lower right corner is located at (i, j).
        If the value of this cell is also 1, then the length of the square is the minimum of:
        the one above, its left, and diagonal up-left value +1. Because if one side is short or missing,
        it will not form a square.
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]]) + 1
                    res = max(res, dp[i][j])
        return res * res

    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_width = 0
        for i in range(m):
            width = 0
            for j in range(n):
                # populates heights arr
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
                # calculates max square width using greedy approach
                if heights[j] > max_width:
                    width += 1
                    if width > max_width:
                        max_width, width = width, 0
                else:
                    width = 0
        return max_width * max_width


def main():
    test_case = [["0", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"],
                 ["0", "1", "1", "1"]]
    print(Solution().maximalSquare(test_case))


if __name__ == '__main__':
    main()
