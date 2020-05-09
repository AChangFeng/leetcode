#! python3
# -*- coding:UTF-8 -*-
"""
# 239. Sliding Window Maximum
# Created on 2020/5/9 19:59
# maxSlidingWindow
# @author: ChangFeng
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        TLE
        """
        if not nums or not k:
            return []
        n = len(nums)
        return [max(nums[i:i + k]) for i in range(n - k + 1)]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []
        if k == 1:
            return nums
        d = deque()
        res = []
        for i, n in enumerate(nums):
            # 移除比当前元素小的所有元素，它们不可能是最大的。
            while d and nums[d[-1]] < n:
                d.pop()
            # 将当前元素添加到双向队列中。
            d += i,
            # 左边元素移出窗口
            if d[0] == i - k:
                d.popleft()
            # 将 deque[0] 添加到输出中。
            if i >= k - 1:
                res += nums[d[0]],
        return res


def main():
    pass


if __name__ == '__main__':
    main()
