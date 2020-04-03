#! python3
# -*- coding:UTF-8 -*-
"""
# 322. Coin Change
# Created on 2020/4/3 18:47
# coinChange
# @author: ChangFeng
"""
import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Brute force
        TLE
        """
        res = []

        def bfs(sum, count):
            if sum == amount:
                res.append(count)
                return
            if sum > amount:
                return
            for i in coins:
                if sum + i <= amount:
                    bfs(sum + i, count + 1)

        bfs(0, 0)
        if not res:
            return -1
        return min(res)

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins or min(coins) > amount:
            return -1
        dp = [-1 for _ in range(amount + 1)]
        for i in range(amount + 1):
            candidates = []
            for coin in coins:
                if i == coin:
                    candidates.append(1)
                elif i - coin > 0 and dp[i - coin] > 0:
                    candidates.append(dp[i - coin] + 1)
            if candidates:
                dp[i] = min(candidates)
        return dp[-1]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins or min(coins) > amount:
            return -1
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != sys.maxsize else -1


def main():
    test_case = [[1, 2, 5], 11]
    print(Solution().coinChange(*test_case))


if __name__ == '__main__':
    main()
