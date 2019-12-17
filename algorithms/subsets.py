#! python3
# -*- coding:UTF-8 -*-
"""
# 78. Subsets
# Created on 2019/12/17 17:56
# subsets
# @author: ChangFeng
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        def backtracking(i, path):
            ans.append(path)
            for x in range(i + 1, len(nums)):
                backtracking(x, path + [nums[x]])

        for i in range(len(nums)):
            backtracking(i, [nums[i]])
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i, path):
            ans.append(path)
            for x in range(i, len(nums)):
                dfs(x + 1, path + [nums[x]])

        dfs(0, [])
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            ans += [a + [n] for a in ans]
        return ans


def main():
    test_case = [1, 2, 3]
    print(Solution().subsets(test_case))


if __name__ == '__main__':
    main()
