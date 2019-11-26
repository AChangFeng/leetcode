#! python3
# -*- coding:UTF-8 -*-
"""
# 48. Rotate Image
# Created on 2019/10/15 9:42
# rotateImage
# @author: ChangFeng
"""
from typing import List


class Solution:

    def rotate1(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        for i in range(l):
            for j in range(i + 1, l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        顺时针旋转九十度：行逆序，列变行
        逆时针旋转九十度：列变行，行逆序
        :param matrix:
        :return:
        """
        matrix[::] = zip(*matrix[::-1])

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 只旋转row_num//2层
        for i in range(n // 2):
            # 旋转元素个数为row_num-i-1，每往里面一层，需要旋转的元素都要减去i，
            # 因为定点是另外一边的起点，所以-1
            for j in range(i, n - i - 1):
                # top坐标为 i j
                top = matrix[i][j]
                # right的列固定为i，行为col_num-1-i，每往里面一层，需要旋转的元素都要减去i
                right = matrix[n - j - 1][i]
                # bottom的行和right的列一样，列为col_num-i-j
                bottom = matrix[n - i - 1][n - j - 1]
                # left的行固定为j 和bottom的行一样
                left = matrix[j][n - i - 1]
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][
                    n - i - 1] = right, bottom, left, top


def main():
    test_cast = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix(test_cast)
    Solution().rotate(test_cast)
    print_matrix(test_cast)

    test_cast = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print_matrix(test_cast)
    Solution().rotate(test_cast)
    print_matrix(test_cast)


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
