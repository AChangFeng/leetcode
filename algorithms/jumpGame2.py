#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/14 9:11
# jumpGame2
# @author: ChangFeng
"""
from typing import List


def jump_count1(nums, position, count, counts):
    print(position)
    if position == len(nums) - 1:
        counts.append(count)
        return count
    furthest_jump = min(nums[position] + position, len(nums) - 1)
    for i in range(position + 1, furthest_jump + 1):
        count = min(count, jump_count1(nums, i, count + 1, counts))
    return count


class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        :param nums:
        :return:
        '''
        jumps = cur_end = cur_farthest = 0
        for i in range(len(nums) - 1):
            # cur_start-cur_end能够跳得最远的位置
            cur_farthest = max(cur_farthest, nums[i] + i)
            # 遍历到了最远的位置
            if i == cur_end:
                # 进行跳跃，更新跳跃次数
                jumps += 1
                # 更新边界为当前区间能够跳跃到的最远的位置
                cur_end = cur_farthest
        return jumps

    def jump1(self, nums) -> int:
        '''
        TLE O(n^2)
        从后往前，起跳的位置为：
        从左往右循环，能跳到pos的第一个值
        :param nums:
        :return:
        '''
        pos = len(nums) - 1
        jumps = 0
        while pos != 0:
            for i in range(pos):
                if i + nums[i] >= pos:
                    pos = i
                    jumps += 1
                    break
        return jumps


def main():
    test_case = [2, 3, 1, 1, 4]
    print(Solution().jump(test_case))  # 2
    # test_case = [2, 9, 6, 5, 7, 0, 7, 2, 7, 9, 3, 2, 2, 5, 7, 8, 1, 6, 6, 6, 3, 5, 2, 2, 6, 3]
    # print(Solution().jump(test_case))  # 5


if __name__ == '__main__':
    main()
