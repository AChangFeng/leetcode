#! python3
# -*- coding:UTF-8 -*-
"""
# 198. House Robber
# Created on 2019/11/27 10:11
# rob
# @author: ChangFeng
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        TLE
        :param nums:
        :return:
        """

        def helper(opts, i):
            if i < 0:
                return 0
            return max(helper(opts, i - 1), helper(opts, i - 2) + opts[i])

        return helper(nums, len(nums) - 1)

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0 for _ in range(len(nums) + 1)]
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre1 = pre2 = 0
        for num in nums:
            tmp = pre1
            pre1 = max(pre1, pre2 + num)
            pre2 = tmp
        return pre1


def main():
    test_case = [2, 7, 9, 3, 1]
    print(Solution().rob(test_case))


if __name__ == '__main__':
    main()
