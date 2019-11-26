#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/9/26 9:28
# removeElement
# @author: ChangFeng
"""
import sys
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        # 排序的解法
        nums.sort()
        val_start_index, val_end_index = len(nums), len(nums)
        # 找到目标val出现的开始index和结束index+1
        # 然后将index以后的元素替换为index+1后的元素 就删除了val这个元素
        for i in range(0, len(nums)):
            if nums[i] == val:
                if i < val_start_index:
                    val_start_index = i
                if i + 1 < len(nums) and nums[i + 1] != val:
                    val_end_index = i + 1
                    break
        nums[val_start_index:] = nums[val_end_index:]
        return len(nums)

    def removeElementV1(self, nums, val):
        if not nums:
            return 0
        # 这个解法我们关注与不等于i的也就是我们要保留的
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

    def removeElementV2(self, nums, val):
        if not nums:
            return 0
        # 双指针解法
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            else:
                start += 1
        return start + 1


def main():
    test_case = [[3, 2, 2, 3], 3]
    print(Solution().removeElement(*test_case))
    print(Solution().removeElementV1(*test_case))
    print(Solution().removeElementV2(*test_case))
    test_case = [[0, 1, 2, 2, 3, 0, 4, 2], 2]
    print(Solution().removeElement(*test_case))
    print(Solution().removeElementV1(*test_case))
    print(Solution().removeElementV2(*test_case))
    test_case = [[1], 1]
    print(Solution().removeElement(*test_case))
    print(Solution().removeElementV1(*test_case))
    print(Solution().removeElementV2(*test_case))
    test_case = [[2], 3]
    print(Solution().removeElement(*test_case))
    print(Solution().removeElementV1(*test_case))
    print(Solution().removeElementV2(*test_case))


if __name__ == '__main__':
    main()
