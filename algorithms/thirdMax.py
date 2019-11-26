#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""
import sys
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -sys.maxsize
        for x in nums:
            if x > max1:
                max3, max2, max1 = max2, max1, x
            elif max2 < x < max1:
                max3, max2 = max2, x
            elif max3 < x < max2:
                max3 = x
        return max3 if max3 != -sys.maxsize else max1

    def thirdMax1(self, nums: List[int]) -> int:
        one = two = three = -sys.maxsize
        for i in nums:
            if i > one:
                one, two, three = i, one, two
            elif i > two and i < one:
                two, three = i, two
            elif i > three and i < two:
                three = i
        return three if three != -sys.maxsize else one


def main():
    _input = [3, 2, 1]
    print(Solution().thirdMax(_input))


if __name__ == '__main__':
    main()
