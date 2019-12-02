#! python3
# -*- coding:UTF-8 -*-
"""
# 581. Shortest Unsorted Continuous Subarray
# Created on 2019/11/29 10:53
# findUnsortedSubarray
# @author: ChangFeng
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_1 = sorted(nums)
        left, right = len(nums) - 1, 0
        for i, n in enumerate(nums):
            if nums_1[i] != n:
                left = min(i, left)
                right = max(i, right)
        return right - left + 1 if right - left >= 0 else 0


def main():
    test_case = [2, 6, 4, 8, 10, 9, 15]
    print(Solution().findUnsortedSubarray(test_case))


if __name__ == '__main__':
    main()
