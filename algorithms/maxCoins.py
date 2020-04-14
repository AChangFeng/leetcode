#! python3
# -*- coding:UTF-8 -*-
"""
# 312. Burst Balloons
# Created on 2020/4/14 19:00
# maxCoins
# @author: ChangFeng
"""
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        Memoization
        """
        # burst all the zero balloons in the first round since they won't give any coins
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        # memo[i][j]: coins obtained from bursting all the balloons between index i and j (not including i or j)
        memo = [[0] * n for _ in range(n)]

        def burst(left, right):
            if left + 1 == right:
                return 0
            if memo[left][right] > 0:
                return memo[left][right]
            ans = 0
            for i in range(left + 1, right):
                ans = max(ans, nums[left] * nums[i] * nums[right] + burst(left, i) + burst(i, right))
            memo[left][right] = ans
            return ans

        return burst(0, n - 1)

    def maxCoins(self, nums: List[int]) -> int:
        """
        dynamic program
        dp[i][j]: coins obtained from bursting all the balloons between index i and j (not including i or j)
        dp[i][j] = max(nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) (k in (i+1,j))
        If k is the index of the last balloon burst in (i, j), the coins that burst will get are
        nums[i] * nums[k] * nums[j], and to calculate dp[i][j], we also need to add the coins obtained from
        bursting balloons between i and k, and between k and j, i.e., dp[i][k] and dp[k][j]
        """
        # burst all the zero balloons in the first round since they won't give any coins
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]


def main():
    pass


if __name__ == '__main__':
    main()
