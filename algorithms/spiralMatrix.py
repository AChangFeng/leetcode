#! python3
# -*- coding:UTF-8 -*-
"""
# 54. Spiral Matrix
# Created on 2019/10/17 9:38
# spiralMatrix
# @author: ChangFeng
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        ans = [*matrix.pop(0)]
        # 逆时针旋转90度 就是原矩阵行列变换，然后列逆序
        rotate90 = [*zip(*matrix)][::-1]
        return ans + self.spiralOrder(rotate90)


def main():
    # test_case = [[1, 2, 3]]
    # print(Solution().spiralOrder(test_case))
    test_case = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
    print(Solution().spiralOrder(test_case))
    test_case = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(Solution().spiralOrder(test_case))


if __name__ == '__main__':
    main()
