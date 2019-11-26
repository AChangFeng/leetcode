#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/9/25 9:09
# removeDuplicates
# @author: ChangFeng
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 没有元素或者只有一个元素 直接返回
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        # j为不重复区间最大的index i作为循环变量
        i, j = 1, 0
        while i < len(nums) and j < len(nums):
            # skip duplicate element
            # 跳过等于重复区间最大值的元素
            while i < len(nums) and nums[i] == nums[j]:
                i += 1
            # nums[i]是下一个不重复元素，如果i还是在数组范围内，将其放到j+1的位置上
            if i < len(nums):
                j += 1
                nums[j] = nums[i]
            # i++ 下次循环不再计算i这个位置上的元素了
            i += 1
        return j + 1

    def removeDuplicatesV1(self, nums: List[int]) -> int:
        # 没有元素或者只有一个元素 直接返回
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        tail = 0
        for i in range(1, len(nums)):
            # 只关注不等于的情况就行了
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1


def main():
    test_case1 = [[1, 1]]
    print(Solution().removeDuplicatesV1(*test_case1))
    test_case1 = [[1, 1, 2]]
    print(Solution().removeDuplicatesV1(*test_case1))
    test_case1 = [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    print(Solution().removeDuplicatesV1(*test_case1))


if __name__ == '__main__':
    main()
