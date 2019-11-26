#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/21 9:19
# mergeIntervals
# @author: ChangFeng
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > merged[-1][-1]:
                merged.append(intervals[i])
            else:
                merged[-1][-1] = max(intervals[i][-1], merged[-1][-1])
        return merged


def main():
    test_case = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(test_case))


if __name__ == '__main__':
    main()
