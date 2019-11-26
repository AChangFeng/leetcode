#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/9 9:39
# combinationSum2
# @author: ChangFeng
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res

    def dfs(self, nums, index, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.dfs(nums, i + 1, target - nums[i], path + [nums[i]], res)


def main():
    test_case = [[10, 1, 2, 7, 6, 1, 5], 8]
    print(Solution().combinationSum2(*test_case))
    test_case = [[2, 5, 2, 1, 2], 5]
    print(Solution().combinationSum2(*test_case))


if __name__ == '__main__':
    main()
