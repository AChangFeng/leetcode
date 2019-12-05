#! python3
# -*- coding:UTF-8 -*-
"""
# 739. Daily Temperatures
# Created on 2019/12/5 14:39
# dailyTemperatures
# @author: ChangFeng
"""
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T:
            return []
        stack = [0]
        ans = [0 for _ in T]
        for i in range(1, len(T)):
            # 处理比当前位置元素小的
            if T[i] > T[stack[-1]]:
                while stack and T[i] > T[stack[-1]]:
                    # 比当前位置元素小的元素索引出栈并计算出距离加入到返回结果中
                    top = stack.pop()
                    ans[top] = i - top
            # 当前元素索引入栈
            stack.append(i)
        return ans


def main():
    test_case = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(test_case))


if __name__ == '__main__':
    main()
