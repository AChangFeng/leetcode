#! python3
# -*- coding:UTF-8 -*-
"""
# 85. Maximal Rectangle
# Created on 2020/5/11 18:53
# maximalRectangle
# @author: ChangFeng
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0]) + 1
        height = [0 for _ in range(n)]
        res = 0
        for i in range(m):
            stack = [-1]
            for j in range(n):
                # 记录连续1的高度
                if j < n - 1:
                    if matrix[i][j] == '1':
                        height[j] += 1
                    else:
                        height[j] = 0

                # 取出比当前高度大的高度，计算其面积并更新结果
                while height[stack[-1]] > height[j]:
                    res = max(res, height[stack.pop()] * (j - stack[-1] - 1))
                stack.append(j)
        return res


def main():
    test_case = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(Solution().maximalRectangle(test_case))


if __name__ == '__main__':
    main()
