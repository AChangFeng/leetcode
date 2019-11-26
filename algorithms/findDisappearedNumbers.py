#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/11/26 10:12
# findDisappearedNumbers
# @author: ChangFeng
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = [0] * len(nums)
        for i in nums:
            all_nums[i - 1] = i
        ans = []
        for i in range(len(all_nums)):
            if not all_nums[i]:
                ans.append(i + 1)
        return ans

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            index = abs(i) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def main():
    test_case = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(test_case))


if __name__ == '__main__':
    main()
