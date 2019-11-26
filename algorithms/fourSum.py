#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/9/24 9:17
# fourSum
# @author: ChangFeng
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            threeRes = self.threeSum(nums[i + 1:], target - nums[i])
            for item in threeRes:
                res.append([nums[i]] + item)
        return res

    def threeSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


def main():
    testcase1 = [[], 1]
    print(Solution().fourSum(*testcase1))


if __name__ == '__main__':
    main()
