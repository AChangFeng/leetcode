#! python3
# -*- coding:UTF-8 -*-
"""
# 295. Find Median from Data Stream
# Created on 2020/4/21 18:46
# medianFinder
# @author: ChangFeng
"""
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
            return
        largest = -self.max_heap[0]
        if num <= largest:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        self.ensure_median()

    def ensure_median(self):
        if self.size % 2 == 0:
            # even
            max_heap_size = int(self.size / 2)
        else:
            # odd
            max_heap_size = self.size // 2 + 1
        for i in range(len(self.max_heap) - max_heap_size):
            n = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, n)
        for i in range(len(self.min_heap) - self.size // 2):
            n = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -n)

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        if len(self.nums) % 2 == 0:
            return (self.nums[len(self.nums) // 2 - 1] + self.nums[len(self.nums) // 2]) / 2
        else:
            return self.nums[len(self.nums) // 2]


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


def main():
    obj = MedianFinder()
    test_case = [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0]
    test_case = [1, 2, 3]
    for i in range(len(test_case)):
        num = test_case[i]
        obj.addNum(num)
        param_2 = obj.findMedian()
        print(param_2)


if __name__ == '__main__':
    main()
