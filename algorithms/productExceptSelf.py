#! python3
# -*- coding:UTF-8 -*-
"""
# 238. Product of Array Except Self
# Created on 2019/12/20 15:42
# productExceptSelf
# @author: ChangFeng
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        left_p = []
        right_p = [0 for _ in nums]
        for num in nums:
            if not left_p:
                left_p.append(num)
            else:
                left_p.append(left_p[-1] * num)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_p[i] = nums[i]
            else:
                right_p[i] = right_p[i + 1] * nums[i]
        for i in range(len(nums)):
            if not ans:
                ans.append(right_p[i + 1])
            elif i == len(nums) - 1:
                ans.append(left_p[i - 1])
            else:
                ans.append(left_p[i - 1] * right_p[i + 1])
        return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * l
        ans[0] = 1
        # ans[i]=i之前所有数字的乘积
        for i in range(1, l):
            ans[i] = ans[i - 1] * nums[i - 1]
        r = 1
        # 动态计算右边的乘积
        for i in reversed(range(l)):
            ans[i] = ans[i] * r
            r *= nums[i]
        return ans


def main():
    test_case = [1, 2, 3, 4]
    assert Solution().productExceptSelf(test_case) == [24, 12, 8, 6], "test_case fail"


if __name__ == '__main__':
    main()
