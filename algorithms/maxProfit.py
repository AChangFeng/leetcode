#! python3
# -*- coding:UTF-8 -*-
"""
# 121. Best Time to Buy and Sell Stock
# Created on 2019/9/25 17:29
# maxProfit
# @author: ChangFeng
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        只能进行一次交易，也就是一次买一次卖
        :param prices:
        :return:
        """
        # 记录最低价格
        min_price = prices[0]
        # 记录最大利润
        max_profit = 0
        for price in prices:
            if price < min_price:
                # 更新最低价格
                min_price = price
            elif price > min_price:
                # 如果当前价格大于最低价格
                # 则计算当前价格的利润，和历史利润之间的较大者为最大利润
                max_profit = max(price - min_price, max_profit)
        return max_profit


def main():
    test_case1 = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(test_case1))
    test_case1 = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(test_case1))


if __name__ == '__main__':
    main()
