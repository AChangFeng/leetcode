#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/9/29 13:31
# searchInRotatedSortedArray
# @author: ChangFeng
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            # 如果左边是有序的
            if nums[start] <= nums[mid]:
                # target在[start,mid)之间
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            # 如果右边是有序的
            if nums[mid] <= nums[end]:
                # target在(mid,end]之间
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


def main():
    test_case = [[4, 5, 6, 7, 0, 1, 2], 0]
    print(Solution().search(*test_case))


if __name__ == '__main__':
    main()
