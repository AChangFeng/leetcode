#! python3
# -*- coding:UTF-8 -*-
"""
#287. Find the Duplicate Number
# Created on 2019/12/21 16:49
# findDuplicate
# @author: ChangFeng
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        sort
        """
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    def findDuplicate(self, nums: List[int]) -> int:
        """
        set
        """
        s = set()
        for n in nums:
            if n in s:
                return n
            else:
                s.add(n)

    def findDuplicate(self, nums: List[int]) -> int:
        t = r = nums[0]
        while True:
            t = nums[t]
            r = nums[nums[r]]
            if t == r:
                break
        p1, p2 = nums[0], t
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1

    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            cnt = sum(x <= mid for x in nums)
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low


def test(test_case, expect):
    r = Solution().findDuplicate(test_case)
    assert r == expect, "test_case fail. input: {}, expect: {}, actual: {}".format(test_case, expect, r)


def main():
    test_cases = [([1, 3, 4, 2, 2], 2), ([3, 1, 3, 4, 2], 3)]
    for test_case in test_cases:
        test(*test_case)


if __name__ == '__main__':
    main()
