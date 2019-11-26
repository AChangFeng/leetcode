#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/9/23 10:28
# threeSumClosest
# @author: ChangFeng
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return res


def main():
    testcase1 = [[-1, 2, 1, -4], 1]
    print(Solution().threeSumClosest(*testcase1))  # 2
    testcase1 = [[1, 1, 1, 0], -100]
    print(Solution().threeSumClosest(*testcase1))  # 2
    testcase1 = [[1, 1, 1, 0], 100]
    print(Solution().threeSumClosest(*testcase1))  # 3
    testcase1 = [[1, 1, -1, -1, 3], -1]
    print(Solution().threeSumClosest(*testcase1))  # -1


if __name__ == '__main__':
    main()
