#! python3
# -*- coding:UTF-8 -*-
"""
# 152. Maximum Product Subarray
# Created on 2020/4/9 18:47
# maxProduct
# @author: ChangFeng
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mx = mn = res = nums[0]
        for i in range(1, len(nums)):
            tmp = mx
            mx = max(max(mx * nums[i], mn * nums[i]), nums[i])
            mn = min(min(tmp * nums[i], mn * nums[i]), nums[i])
            res = max(mx, res)
        return res

    def maxProduct(self, nums):
        """
        如果数字中没有0：
            如果负数的数量为偶数，则结果是从开头和结尾可以得到的总乘积；
            如果负数的数量为奇数，则可以从开头或结尾处得到结果。
        考虑数字中有0的情况，也只需要在遇到0的时候设置乘积为他本身。
        之所以要加上reverse，是因为[1,-3,4]这种情况没有reverse的话会返回错误结果：
        由于存在负数，从左往右的乘积和从右往左的乘积是不一样的。
        """
        nums_r = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] = nums[i] * nums[i - 1] if nums[i - 1] != 0 else nums[i]
            nums_r[i] = nums_r[i] * nums_r[i - 1] if nums[i - 1] != 0 else nums[i]
        return max(nums + nums_r)


def main():
    pass


if __name__ == '__main__':
    main()
