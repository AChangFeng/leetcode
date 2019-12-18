#! python3
# -*- coding:UTF-8 -*-
"""
# 347. Top K Frequent Elements
# Created on 2019/12/18 19:41
# topKFrequent
# @author: ChangFeng
"""
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [entry[0] for entry in counter.most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [entry[0] for entry in Counter(nums).most_common(k)]


def main():
    test_case = [[1, 1, 1, 2, 2, 3], 2]
    print(Solution().topKFrequent(*test_case))


if __name__ == '__main__':
    main()
