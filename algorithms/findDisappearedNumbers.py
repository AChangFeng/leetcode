#! python3
# -*- coding:UTF-8 -*-
"""
# 448. Find All Numbers Disappeared in an Array
# Created on 2019/11/26 10:12
# findDisappearedNumbers
# @author: ChangFeng
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = [0] * len(nums)
        for i in nums:
            all_nums[i - 1] = i
        ans = []
        for i in range(len(all_nums)):
            if not all_nums[i]:
                ans.append(i + 1)
        return ans

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        nums[i]-1就是数组下标
        使用nums[nums[i] -1] = -nums[nums[i]-1]将该位置上的数字设置为负数
        遍历数组，如果该位置上的数字不是负数，说明这个位置上的元素没有操作，
        也就是说，这个位置上的下标+1就是其中一个答案
        :param nums:
        :return:
        """
        for i in nums:
            index = abs(i) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def main():
    test_case = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(test_case))


if __name__ == '__main__':
    main()
