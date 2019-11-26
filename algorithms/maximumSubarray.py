#! python3
# -*- coding:UTF-8 -*-
"""
# 53. Maximum Subarray
# Created on 2019/10/16 10:46
# maximumSubarray
# @author: ChangFeng
"""
from typing import List


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        """
        Time Limit Exceeded
        :param nums:
        :return:
        """
        if not nums:
            return 0
        max_sum = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                max_sum = max(max_sum, sum(nums[i: j + 1]))
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        # dp[i]就是0-i的最大值
        # 因为题目中要求是连续子串，如果dp[i-1]<0，则dp[i-1]+num[i]<num[i],最大和是nums[i]
        # 状态转移方程是: dp[i]=max(nums[i],dp[i-1]+nums[i])
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            # dp[i] = dp[i - 1] + nums[i] if dp[i - 1] + nums[i] > nums[i] else nums[i]
            max_sum = max(max_sum, dp[i])
        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = s = nums[0]
        for i in range(1, len(nums)):
            if s < 0:
                s = nums[i]
            else:
                s += nums[i]
            m = max(m, s)
        return m


def main():
    test_case = [1, 2, 3]
    print(Solution().maxSubArray2(test_case))
    test_case = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray2(test_case))
    test_case = [-2, 1]
    print(Solution().maxSubArray2(test_case))


if __name__ == '__main__':
    main()
