#! python3
# -*- coding:UTF-8 -*-
"""
# 39. Combination Sum
#
# Created on 2019/10/8 9:39
# combinationSum
# @author: ChangFeng
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res

    def dfs(self, candidates, index, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            self.dfs(candidates, i, target - candidates[i], path + [candidates[i]], res)

    def dfs1(self, nums, index, path, res):
        if path:
            res.append(path)
        for i in range(index + 1, len(nums)):
            self.dfs1(nums, i, path + [nums[i]], res)

    def all(self, candidates):
        res = []
        self.dfs1(candidates, -1, [], res)
        return res

    def dfsUseStack(self, nums):
        result = []
        nums.sort()

        def dfs(index, stack):
            if stack:
                result.append(stack)
            for i in range(index, len(nums)):
                dfs(i + 1, stack + [nums[i]])

        dfs(0, [])
        return result


def main():
    test_case = [[2, 3, 6, 7], 7]
    print(Solution().combinationSum(*test_case))
    print(Solution().all([2, 3, 6]))
    print(Solution().dfsUseStack([2, 3, 6]))


if __name__ == '__main__':
    main()
