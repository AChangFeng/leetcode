#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/14 9:11
# jumpGame1
# @author: ChangFeng
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> bool:
        return canJumpFromPositionV3(nums)


def canJumpFromPositionV3(nums):
    last_index = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= last_index:
            last_index = i
    return last_index == 0


def canJumpFromPositionV2(nums):
    memo = [-1] * len(nums)
    for i in range(len(nums) - 2, -1, -1):
        furthest_jump = min(nums[i] + i, len(nums) - 1)
        for j in range(i + 1, furthest_jump):
            if memo[j] == 1:
                memo[i] = 1
                break
    return memo[0] == 1


def canJumpFromPositionV1(nums, position, memo):
    if memo[position] != -1:
        return memo[position] == 1
    furthest_jump = min(nums[position] + position, len(nums) - 1)
    for i in range(position + 1, furthest_jump + 1):
        if canJumpFromPositionV1(nums, i, memo):
            memo[position] = 1
            return True
    memo[position] = 0
    return False


def canJumpFromPosition(nums, position):
    if position == len(nums) - 1:
        return True
    furthest_jump = min(nums[position] + position, len(nums) - 1)
    for i in range(position + 1, furthest_jump + 1):
        if canJumpFromPosition(nums, i):
            return True
    return False





def main():
    test_case = [2, 3, 1, 1, 4]
    print(Solution().jump(test_case))
    test_case = [3, 2, 1, 0, 4]
    print(Solution().jump(test_case))
    test_case = [0, 2, 3]
    print(Solution().jump(test_case))


if __name__ == '__main__':
    main()
