#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2020/1/17 18:43
# subarraySum
# @author: ChangFeng
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, _sum, dic = 0, 0, {0: 1}
        for num in nums:
            _sum += num
            if _sum - k in dic:
                ans += dic[_sum - k]
            dic[_sum] = dic.setdefault(_sum, 0) + 1
        return ans


def main():
    test_case = [[1, 1, 1], 2]
    print(Solution().subarraySum(*test_case))  # 2


if __name__ == '__main__':
    main()
