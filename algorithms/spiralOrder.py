#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2020/7/6 10:38
# spiralOrder
# @author: ChangFeng
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix:
            return []
        left, right, top, bottom, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            # top: left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            # right: top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            # bottom: right to left
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break
            # left: bottom to top
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if right < left:
                break
        return res

    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = [0] * len(matrix[0]) * len(matrix)
        i = 0
        while True:
            # top
            for x in range(left, right + 1):
                res[i] = matrix[top][x]
                i += 1
            top += 1
            if top > bottom:
                break
            # right
            for x in range(top, bottom + 1):
                res[i] = matrix[x][right]
                i += 1
            right -= 1
            if right < left:
                break
            # bottom
            for x in range(right, left - 1, -1):
                res[i] = matrix[bottom][x]
                i += 1
            bottom -= 1
            if bottom < top:
                break
            # left
            for x in range(bottom, top - 1, -1):
                res[i] = matrix[x][left]
                i += 1
            left += 1
            if left > right:
                break
        return res


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
    print(Solution().spiralOrder1(matrix))

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))
    print(Solution().spiralOrder1(matrix))


if __name__ == '__main__':
    main()
