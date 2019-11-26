#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/11/5 9:14
# searcha2DMatrix
# @author: ChangFeng
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        if not len(matrix[0]):
            return False
        start, end = 0, len(matrix) - 1
        target_row = None
        while start <= end:
            mid = (start + end) // 2
            # if matrix[mid][0] == target or matrix[mid][-1] == target:
            #     return True
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = mid
                break
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1
        if target_row is None:
            return False
        start, end = 0, len(matrix[target_row]) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[target_row][mid] == target:
                return True
            if matrix[target_row][mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        l = []
        for row in matrix:
            l.extend(row)
        start, end = 0, len(l) - 1
        while start <= end:
            mid = (start + end) // 2
            if l[mid] == target:
                return True
            if l[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


def main():
    test_case = [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 10]
    print(Solution().searchMatrix(*test_case))
    test_case = [[
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3]
    print(Solution().searchMatrix(*test_case))
    test_case = [[
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 13]
    print(Solution().searchMatrix(*test_case))


if __name__ == '__main__':
    main()
