#! python3
# -*- coding:UTF-8 -*-
"""
# 128. Longest Consecutive Sequence
# Created on 2020/4/16 19:34
# longestConsecutive
# @author: ChangFeng
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            #  If the number x is the start of a streak.
            if x - 1 not in nums:
                # test y = x+1, x+2, x+3, ... and stop at the first number y not in the set.
                y = x + 1
                while y in nums:
                    y += 1
                # The length of the streak is then simply y-x, update best with that.
                best = max(best, y - x)
        return best


def main():
    pass


if __name__ == '__main__':
    main()
