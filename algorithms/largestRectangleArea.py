#! python3
# -*- coding:UTF-8 -*-
"""
# 84. Largest Rectangle in Histogram
# Created on 2020/5/11 20:25
# largestRectangleArea
# @author: ChangFeng
"""


class Solution:
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                pop = stack.pop()
                h = height[pop]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
                print("index: ({},{}). height: {}. width: {}. ans: {}".format(pop, i, h, w, ans))
            stack.append(i)
        height.pop()
        return ans


def main():
    test_case = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(test_case))


if __name__ == '__main__':
    main()
