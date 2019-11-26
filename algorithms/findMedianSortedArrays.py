#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2
        even = l % 2 == 0
        res = l // 2 + 1
        nums = [0] * res
        i = j = 0
        for x in range(res):
            if j <= l2 - 1 and i <= l1 - 1:
                if nums2[j] < nums1[i]:
                    nums[x] = nums2[j]
                    j += 1
                else:
                    nums[x] = nums1[i]
                    i += 1
            else:
                if j <= l2 - 1:
                    nums[x] = nums2[j]
                    j += 1
                if i <= l1 - 1:
                    nums[x] = nums1[i]
                    i += 1
        if even:
            return (nums[-1] + nums[-2]) / 2
        else:
            return nums[-1]


def main():
    testcase1 = [[1, 3], [2]]
    testcase2 = [[1, 2], [3, 4]]
    print(Solution().findMedianSortedArrays(*testcase1))
    print(Solution().findMedianSortedArrays(*testcase2))


if __name__ == '__main__':
    main()
