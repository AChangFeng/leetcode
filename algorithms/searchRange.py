#! python3
# -*- coding:UTF-8 -*-
"""
# 34. Find First and Last Position of Element in Sorted Array
# Created on 2019/9/30 9:05
# searchRange
# @author: ChangFeng
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                start, end = mid, mid
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                return [start, end]
            elif nums[mid] < target:
                # search right
                start = mid + 1
            else:
                # search left
                end = mid - 1
        return [-1, -1]

    def searchRange1(self, nums, target):
        def binarySearchLeft(A, x):
            l, r = 0, len(A) - 1
            while l <= r:
                mid = (l + r) // 2
                if x <= A[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def binarySearchRight(A, x):
            l, r = 0, len(A) - 1
            while l <= r:
                mid = (l + r) // 2
                if x >= A[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return [left, right] if left <= right else [-1, -1]


def main():
    test_case = [[5, 7, 7, 8, 8, 10], 8]
    print(Solution().searchRange1(*test_case))  # [3,4]
    test_case = [[5, 7, 7, 8, 8, 10], 6]
    print(Solution().searchRange1(*test_case))  # [-1,-1]
    test_case = [[5, 7, 7, 8, 8, 8, 8, 10], 8]
    print(Solution().searchRange1(*test_case))  # [3,6]
    test_case = [[8, 8, 8, 8], 8]
    print(Solution().searchRange1(*test_case))  # [0,3]


if __name__ == '__main__':
    main()
