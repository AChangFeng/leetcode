#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # skip same number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            # find other two numbers
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    # skip same number
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # skip same number
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # move forward two pointer
                    l += 1
                    r -= 1
        return res


def main():
    testcase = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(testcase))


if __name__ == '__main__':
    main()
