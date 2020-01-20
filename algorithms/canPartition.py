#! python3
# -*- coding:UTF-8 -*-
"""
# 416. Partition Equal Subset Sum
# Created on 2020/1/20 18:22
# canPartition
# @author: ChangFeng
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Brute Force
        TLE
        """
        if sum(nums) % 2 != 0:
            return False

        def helper(index, sum1, sum2):
            if sum(nums[index:]) < abs(sum1 - sum2):
                return False
            if index == len(nums):
                return sum1 == sum2
            for i in range(index, len(nums)):
                return helper(index + 1, sum1 + nums[index], sum2) or helper(index + 1, sum1, sum2 + nums[index])

        return helper(0, 0, 0)

    def canPartition(self, nums: List[int]) -> bool:
        """
        既然是两个相同和的子集，那么所有元素的和一定是2的倍数，否则不能切分。
        因为切分出来的两个子组和相同，所以我们只需要看在数组中是否有若干个数字的和等于总和除以2即可
        """
        if not nums:
            return False
        _sum = sum(nums)
        if _sum % 2 == 1:
            return False
        target = _sum / 2
        dp = [[False for _ in range(int(target) + 1)] for _ in range(len(nums))]
        # first row
        if nums[0] <= target:
            dp[0][nums[0]] = True
        # first column
        for i in range(len(nums)):
            dp[i][0] = True
        for m in range(1, len(nums)):
            for n in range(1, len(dp[0])):
                if n < nums[m]:
                    dp[m][n] = dp[m - 1][n]
                else:
                    dp[m][n] = dp[m - 1][n] or dp[m - 1][n - nums[m]]
        return dp[-1][-1]

    def canPartition(self, nums: List[int]) -> bool:
        """
        注意到上一个解法中，dp中每一行的状态只和上一行的状态相关，
        所以将二维数组替换为一维数组，为了不让前面的计算影响到后面的值，内层循环倒置一下
        """
        if not nums:
            return False
        _sum = sum(nums)
        if _sum % 2 == 1:
            return False
        target = _sum / 2
        dp = [False for _ in range(int(target) + 1)]
        # first row
        if nums[0] <= target:
            dp[nums[0]] = True
        # first column
        dp[0] = True
        for m in range(1, len(nums)):
            for n in range(len(dp) - 1, 0, -1):
                if nums[m] <= n:
                    dp[n] = dp[n] or dp[n - nums[m]]
        return dp[-1]

    def canPartition(self, nums: List[int]) -> bool:
        """
        使用dfs搜索是否有若干个元素的和等于sum//2
        """
        _sum = sum(nums)
        if _sum % 2 == 1:
            return False
        target = _sum // 2

        def dfs(pos, sm):
            if pos < 0 or sm > target or nums[pos] > target:
                return False
            if sm == target:
                return True
            return dfs(pos - 1, sm + nums[pos]) or dfs(pos - 1, sm)

        return dfs(len(nums) - 1, 0)


def main():
    test_case = [1, 5, 11, 5]
    print(Solution().canPartition(test_case))
    test_case = [1, 2, 3, 5]
    print(Solution().canPartition(test_case))
    test_case = [1, 2, 5]
    print(Solution().canPartition(test_case))


if __name__ == '__main__':
    main()
