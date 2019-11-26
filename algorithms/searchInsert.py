#! python3
# -*- coding:UTF-8 -*-
"""
# 35. Search Insert Position
# Created on 2019/9/30 10:09
# searchInsert
# @author: ChangFeng
"""


class Solution:
    def searchInsert(self, nums, target) -> int:
        print(nums, target)
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high) // 2
            if target == nums[middle]:
                return middle
            if target < nums[middle]:
                high = middle - 1
            else:
                low = middle + 1
            print(low, high, nums[low], nums[high])
        return low


def main():
    test_case = [[1, 3, 5, 6], 2]
    print(Solution().searchInsert(*test_case))


if __name__ == '__main__':
    main()
