#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/22 9:17
# insertInterval
# @author: ChangFeng
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
        return merged

    def insert1(self, intervals, newInterval):
        s, e = newInterval[0], newInterval[-1]
        left = [i for i in intervals if i[-1] < s]
        right = [i for i in intervals if i[0] > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][-1])
        return left + [intervals(s, e)] + right


def main():
    test_case = [[[1, 3], [6, 9]], [2, 5]]
    print(Solution().insert1(*test_case))
    test_case = [[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]]
    print(Solution().insert1(*test_case))


if __name__ == '__main__':
    main()
