#! python3
# -*- coding:UTF-8 -*-
"""
# 169. Majority Element
# Created on 2019/11/26 9:52
# majorityElement
# @author: ChangFeng
"""
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common(1)[0][0]

    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement(self, nums):
        """
        Boyer-Moore Voting Algorithm
        每次从序列里选择两个不相同的数字删除掉（或称为“抵消”），
        最后剩下一个数字或几个相同的数字，就是出现次数大于总数一半的那个。
        :param nums:
        :return:
        """
        count = 0
        candi = None
        for i in nums:
            if count == 0:
                candi = i
            if i == candi:
                count += 1
            else:
                count -= 1
        return candi


def main():
    test_case = [3, 2, 3]
    print(Solution().majorityElement(test_case))


if __name__ == '__main__':
    main()
