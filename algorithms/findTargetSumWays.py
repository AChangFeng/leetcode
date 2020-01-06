#! python3
# -*- coding:UTF-8 -*-
"""
# 494. Target Sum
# Created on 2020/1/6 16:36
# findTargetSumWays
# @author: ChangFeng
"""
import sys
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        Brute Force
        TLE
        """
        ans = 0

        def helper(pos, val):
            nonlocal ans
            if pos == len(nums):
                if val == S:
                    ans += 1
            else:
                helper(pos + 1, val + nums[pos])
                helper(pos + 1, val - nums[pos])

        helper(0, 0)
        return ans

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        Recursion with Memoization
        """
        memo = [[-sys.maxsize for _ in range(2002)] for _ in nums]

        def helper(pos, val):
            if pos == len(nums):
                if val == S:
                    return 1
                else:
                    return 0
            else:
                if memo[pos][val + 1000] > -sys.maxsize:
                    return memo[pos][val + 1000]
                add_r = helper(pos + 1, val + nums[pos])
                sub_r = helper(pos + 1, val - nums[pos])
                memo[pos][val + 1000] = add_r + sub_r
                return memo[pos][val + 1000]

        return helper(0, 0)

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        dynamic program
        """
        dp = [0 for _ in range(2002)]
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        for i in range(1, len(nums)):
            next = [0 for _ in range(2002)]
            for j in range(-1000, 1001):
                if dp[j + 1000] > 0:
                    next[j + nums[i] + 1000] += dp[j + 1000]
                    next[j - nums[i] + 1000] += dp[j + 1000]
            dp = next
        return 0 if S > 1000 else dp[S + 1000]

    def findTargetSumWays(self, nums, S):
        from collections import defaultdict
        memo = {0: 1}
        for x in nums:
            m = defaultdict(int)
            for s, n in memo.items():
                m[s + x] += n
                m[s - x] += n
            memo = m
        return memo[S]


def main():
    test_case = [[1, 1, 1, 1, 1], 3]
    print(Solution().findTargetSumWays(*test_case))


if __name__ == '__main__':
    main()
