#! python3
# -*- coding:UTF-8 -*-
"""
# 300. Longest Increasing Subsequence
# Created on 2020/3/16 18:50
# lengthOfLIS
# @author: ChangFeng
"""
import bisect
import sys
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        TLE
        """

        def lenOfLIS(pre, cur):
            if cur == len(nums):
                return 0
            taken = 0
            if nums[cur] > pre:
                taken = 1 + lenOfLIS(nums[cur], cur + 1)
            not_taken = lenOfLIS(pre, cur + 1)
            return max(taken, not_taken)

        return lenOfLIS(-sys.maxsize, 0)

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp
        """
        if len(nums) == 0:
            return 0
        # 构建最长升序序列长度的数组
        dp = [1 for _ in nums]
        res = 1
        for i in range(1, len(nums)):
            # 找到dp[0]到dp[i-1]中最大的升序序列长度且nums[j]<nums[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    # 要么是从这个最大的升序序列长度上+1，要么从这个i这个位置上开始
                    dp[i] = max(dp[j] + 1, dp[i])
            # 更新结果值
            res = max(dp[i], res)

        return res

    def lengthOfLIS(self, nums: List[int]) -> int:
        # every element in sub, sub[i]=val, it is stored in a way that the location i is exactly the length of the
        # best solution that ended with value val.
        sub = []
        for val in nums:
            pos, sub_len = 0, len(sub)
            while pos <= sub_len:
                if pos == sub_len:
                    sub.append(val)
                    break
                elif val <= sub[pos]:
                    sub[pos] = val
                    break
                else:
                    pos += 1
        return len(sub)

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for val in nums:
            idx = bisect.bisect_left(sub, val)
            if idx == len(sub):
                sub.append(val)
            else:
                sub[idx] = val
        return len(sub)


def main():
    test_case = [10, 9, 2, 5, 3, 7, 101, 18]
    print(Solution().lengthOfLIS(test_case))


if __name__ == '__main__':
    main()
