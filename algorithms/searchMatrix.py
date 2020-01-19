#! python3
# -*- coding:UTF-8 -*-
"""
# 240. Search a 2D Matrix II
# Created on 2020/1/19 19:31
# searchMatrix
# @author: ChangFeng
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        r, c = 0, n - 1
        while c >= 0 and r < m:
            if matrix[c][r] == target:
                return True
            elif matrix[c][r] > target:
                c -= 1
            else:
                r += 1
        return False


def main():
    test_case = [[
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5]
    print(Solution().searchMatrix(*test_case))  # true
    test_case = [[
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 20]
    print(Solution().searchMatrix(*test_case))  # false


if __name__ == '__main__':
    main()
