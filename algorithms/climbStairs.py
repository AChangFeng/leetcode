#! python3
# -*- coding:UTF-8 -*-
"""
# 70. Climbing Stairs
# Created on 2019/11/26 16:12
# climbStairs
# @author: ChangFeng
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def helper(m):
            if m in memo:
                return memo[m]
            res = helper(m - 1) + helper(m - 2)
            memo[m] = res
            return res

        return helper(n)

    def climbStairs(self, n: int) -> int:
        """
        dynamic program
        :param n:
        :return:
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1], dp[2] = 0, 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


def main():
    test_case = 1
    print(Solution().climbStairs(test_case))


if __name__ == '__main__':
    main()
