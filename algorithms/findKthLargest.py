#! python3
# -*- coding:UTF-8 -*-
"""
# 215. Kth Largest Element in an Array
# Created on 2019/12/23 18:46
# findKthLargest
# @author: ChangFeng
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) == k:
                if heap[0] > num:
                    continue
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
            else:
                heapq.heappush(heap, num)
        return heap[0]


def test(expect, test_case):
    r = Solution().findKthLargest(*test_case)
    assert r == expect, "test_case fail. input: {}, expect: {}, actual: {}".format(test_case, expect, r)


def main():
    test_cases = [([3, 2, 1, 5, 6, 4], 2, 5), ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)]
    for test_case in test_cases:
        test(test_case[-1], test_case[:-1])


if __name__ == '__main__':
    main()
