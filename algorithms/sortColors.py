#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/11/6 9:13
# sortColors
# @author: ChangFeng
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums) - 1
        while w < b:
            if nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
                r += 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1


def main():
    test_case = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(test_case)
    print(test_case)


if __name__ == '__main__':
    main()
