#! python3
# -*- coding:UTF-8 -*-
"""
# 438. Find All Anagrams in a String
# Created on 2020/3/19 19:43
# findAnagrams
# @author: ChangFeng
"""
import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """TLE"""
        if not p or not s:
            return []
        if len(p) > len(s):
            return []
        counter = collections.Counter(p)
        res = []
        for i in range(len(s) - len(p) + 1):
            tmp_counter = counter.copy()
            candidates = s[i: i + len(p)]
            for candidate in candidates:
                if candidate in tmp_counter and tmp_counter[candidate] > 0:
                    tmp_counter.subtract([candidate])
            if sum(tmp_counter.values()) == 0:
                res.append(i)
        return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        slide window
        """
        if not p or not s or len(p) > len(s):
            return []
        chars = [0 for _ in range(26)]
        for char in p:
            chars[ord(char) - ord('a')] += 1
        res = []
        start = end = 0
        count = 0
        while end < len(s):
            c = s[end]
            # 扩大窗口
            end += 1
            # 更新窗口内数据
            chars[ord(c) - ord('a')] -= 1
            if chars[ord(c) - ord('a')] >= 0:
                count += 1
            # 更新结果集
            if count == len(p):
                res.append(start)
            # 是否要收缩窗口
            if end - start == len(p):
                d = s[start]
                # 收缩窗口
                start += 1
                # 更新窗口内数据
                if chars[ord(d) - ord('a')] >= 0:
                    count -= 1
                chars[ord(d) - ord('a')] += 1
        return res


def main():
    test_case = ['cbaebabacd', 'abc']
    print(Solution().findAnagrams(*test_case))


if __name__ == '__main__':
    main()
