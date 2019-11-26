#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/11/2 9:08
# setMatrixZeroes
# @author: ChangFeng
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)
        fir_column_zero = False
        for y in range(n):
            if not fir_column_zero and not matrix[y][0]:
                fir_column_zero = True
            for x in range(1, m):
                if not matrix[y][x]:
                    matrix[y][0] = 0
                    matrix[0][x] = 0
        for y in range(1, n):
            for x in range(1, m):
                if not matrix[y][0] or not matrix[0][x]:
                    matrix[y][x] = 0
        if not matrix[0][0]:
            for x in range(m):
                matrix[0][x] = 0
        if fir_column_zero:
            for y in range(n):
                matrix[y][0] = 0

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)
        zero_y = [0 for _ in range(n)]
        zero_x = [0 for _ in range(m)]
        for y in range(n):
            for x in range(m):
                if not matrix[y][x]:
                    zero_x[x] = 1
                    zero_y[y] = 1
        for y in range(n):
            for x in range(m):
                if zero_x[x] or zero_y[y]:
                    matrix[y][x] = 0


def main():
    test_case = [[1, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1]]
    print(test_case)
    Solution().setZeroes(test_case)
    print(test_case)
    test_case = [[0, 1, 2, 0],
                 [3, 4, 5, 2],
                 [1, 3, 1, 5]]
    print(test_case)
    Solution().setZeroes(test_case)
    print(test_case)


if __name__ == '__main__':
    main()
