#! python3
# -*- coding:UTF-8 -*-
"""
# 309. Best Time to Buy and Sell Stock with Cooldown
# Created on 2020/1/8 18:57
# maxProfitWithCooldown
# @author: ChangFeng
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy[i]为到第i个位置为购买的最大收益
        # sell[i]为到第i个位置为出售的最大收益
        # 有如下公式
        # i==0也就是在第一天buy[i]=-price[0],sell[i]=0
        # i>0有：
        # buy[i]=max(buy[i-1],sell[i-2]-prices[i])
        # sell[i]=max(sell[i-1],buy[i-1]+prices[i])
        if not prices:
            return 0
        buy = [0 for _ in prices]
        sell = [0 for _ in prices]
        for i in range(len(prices)):
            if i == 0:
                buy[i] = -prices[i]
                sell[i] = 0
                continue
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        return max(buy + sell)


def main():
    test_case = [1, 2, 3, 0, 2]
    print(Solution().maxProfit(test_case))  # 3


if __name__ == '__main__':
    main()
