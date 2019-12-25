#! python3
# -*- coding:UTF-8 -*-
"""
# 49. Group Anagrams
# Created on 2019/12/24 18:09
# groupAnagrams
# @author: ChangFeng
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return d.values()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            d[tuple(cnt)].append(s)
        return d.values()


def test(test_case, expect):
    r = Solution().groupAnagrams(test_case)


def main():
    test_cases = [(["eat", "tea", "tan", "ate", "nat", "bat"],
                   [
                       ["ate", "eat", "tea"],
                       ["nat", "tan"],
                       ["bat"]
                   ]
                   )]
    for test_case in test_cases:
        test(*test_case)


if __name__ == '__main__':
    main()
