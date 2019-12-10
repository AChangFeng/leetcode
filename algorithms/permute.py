#! python3
# -*- coding:UTF-8 -*-
"""
#46. Permutations
# Created on 2019/12/9 8:22
# permute
# @author: ChangFeng
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(path, candidates):
            if len(path) == len(nums):
                ans.append(path)
                return
            for n in candidates:
                candidates1 = candidates.copy()
                candidates1.remove(n)
                helper(path + [n], candidates1)

        for i in range(len(nums)):
            nums1 = nums.copy()
            nums1.remove(nums[i])
            helper([nums[i]], nums1)
        return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(path: List[int]):
            if len(path) == len(nums):
                ans.append(path)
                return
            for n in nums:
                if n in path:
                    continue
                helper(path + [n])

        helper([])
        return ans


def main():
    test_case = [1, 2, 3]
    print(Solution().permute(test_case))


if __name__ == '__main__':
    main()
