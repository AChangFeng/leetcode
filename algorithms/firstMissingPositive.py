#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/10 9:15
# firstMissingPositive
# @author: ChangFeng
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums) + 1
        n = [0] * (length + 1)
        for i, num in enumerate(nums):
            if num < 1 or num > length:
                continue
            n[num] = num
        for i in range(1, length):
            if not n[i]:
                return i
        return length

    # O(n) time
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 0 <= nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

    # O(nlgn) time
    def firstMissingPositiveV1(self, nums):
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res


def main():
    test_case = [1, 2, 0]
    print(Solution().firstMissingPositive(test_case))
    test_case = [3, 4, -1, 1]
    print(Solution().firstMissingPositive(test_case))
    test_case = [7, 8, 9, 11, 12]
    print(Solution().firstMissingPositive(test_case))
    test_case = [1, 2, 3, 4, 5]
    print(Solution().firstMissingPositive(test_case))


if __name__ == '__main__':
    main()
