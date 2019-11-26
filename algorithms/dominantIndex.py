#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""


class Solution:
    def dominantIndex(self, nums) -> int:
        if not nums or len(nums) == 0:
            return -1
        max_index = 0
        max_v = -1
        sec_max_v = -1
        for i, v in enumerate(nums):
            if v > max_v:
                sec_max_v=v
                max_v = v
                max_index = i
            elif v > sec_max_v:
                sec_max_v = v
        print(max_v, sec_max_v)
        if sec_max_v * 2 > max_v:
            return -1
        else:
            return max_index


def main():
    _input = [0, 0, 2, 3]
    print(Solution().dominantIndex(_input))


if __name__ == '__main__':
    main()
