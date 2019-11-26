#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/9/27 9:19
# nextPermutation
# @author: ChangFeng
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_index = -1
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_index = i
                break
        if first_index == -1:
            # reverse
            self.reverse(nums, 0, n - 1)
            return
        second_index = -1
        for i in range(n - 1, first_index, -1):
            if nums[i] > nums[first_index]:
                second_index = i
                break
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        self.reverse(nums, first_index + 1, n - 1)

    def reverse(self, nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


def main():
    test_case = [1, 2, 3]
    Solution().nextPermutation(test_case)
    print(test_case)
    test_case = [3, 2, 1]
    Solution().nextPermutation(test_case)
    print(test_case)
    test_case = [1, 1, 5]
    Solution().nextPermutation(test_case)
    print(test_case)
    test_case = [1, 2, 7, 4, 3, 1]
    Solution().nextPermutation(test_case)
    print(test_case)
    test_case = [1, 3, 2]
    Solution().nextPermutation(test_case)
    print(test_case)  # 2 1 3


if __name__ == '__main__':
    main()
