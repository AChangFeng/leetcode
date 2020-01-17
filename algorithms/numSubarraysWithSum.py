#! python3
# -*- coding:UTF-8 -*-
"""
# Created on #DATE #TIME
# #NAME
# @author: ChangFeng
"""
import collections


class Solution:
    def numSubarraysWithSum(self, arr, s):
        # sum(j)-sum[i]就是i-j子组的和
        counter = collections.Counter({0: 1})
        _sum = ans = 0
        for x in arr:
            # 更新和
            _sum += x
            # 当前和减去目标S 差值出现的次数就是和为s的子组的数量
            # 如果没有_sum-x这个key 则返回0
            ans += counter[_sum - s]
            # 更新计数器值
            counter[_sum] += 1
        return ans

    def numSubarraysWithSum1(self, arr, s):
        pre_sum_arr = [0]
        for x in arr:
            pre_sum_arr.append(pre_sum_arr[-1] + x)
        counter = collections.Counter()
        ans = 0
        for x in pre_sum_arr:
            ans += counter[x - s]
            counter[x] += 1
        return ans


def main():
    _input = [0, 0, 0, 0, 0]
    s = 0
    r = Solution().numSubarraysWithSum(_input, s)
    print(r)
    r = Solution().numSubarraysWithSum1(_input, s)
    print(r)


if __name__ == '__main__':
    main()
