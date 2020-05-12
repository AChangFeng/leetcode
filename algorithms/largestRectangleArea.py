#! python3
# -*- coding:UTF-8 -*-
"""
# 84. Largest Rectangle in Histogram
# Created on 2020/5/11 20:25
# largestRectangleArea
# @author: ChangFeng
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        1、栈里面存储的是升序的高度的下标。在将一个新的下标入栈之前，先将栈中大于新下标所在位置的高度的所有下标出栈。
        出栈的下标所在位置的高度就是新下标为右边界，栈顶下标为左边界的矩形的高。计算出其面积并更新结果。使用0高度处理了边界情况。
        2、对于任意高度x，如果它在以其为高的矩形里面，则此矩形里面其他的高度都要比x高。那么剩下的问题就是找到左右边界，也就是小于x的高度。
        从代码中可以看出，当高度出栈时，它必定比i位置上的高度高，所以i是有边界（不包含）；
        栈顶高度（也就是前面出栈高度的前一个高度）也是是第一个小于出栈高度的值，因此，它就是左边界（不包含）。
        有了左边界有边界和高度，就能求出矩形的面积。
        """
        if not heights:
            return 0
        heights.append(0)
        stack, ans = [-1], 0
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                ans = max(ans, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        return ans


def main():
    test_case = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(test_case))


if __name__ == '__main__':
    main()
