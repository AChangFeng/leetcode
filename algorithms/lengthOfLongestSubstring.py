#! python3
# -*- coding:UTF-8 -*-
"""
# 3. Longest Substring Without Repeating Characters
# Created on 2020/4/22 10:27
# lengthOfLongestSubstring
# @author: ChangFeng
"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        start_indices = []
        for i in range(len(s)):
            tmp = []
            for start_index in start_indices:
                substring = s[start_index:i]
                if s[i] in substring:
                    max_len = max(max_len, len(substring))
                else:
                    tmp.append(start_index)
            start_indices = tmp
            start_indices.append(i)
        if start_indices:
            max_len = max(max_len, len(s[start_indices[0]:]))
        return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        slide window:
        """
        if not s:
            return 0
        window = defaultdict(int)
        max_length = left = right = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1

            while window[c] > 1:
                d = s[left]
                left += 1
                if window[d]:
                    window[d] -= 1
            max_length = max(max_length, right - left)
        return max_length


def main():
    test_case = "pwwkew"
    count = Solution().lengthOfLongestSubstring(test_case)
    assert count == 3, "error, expected: {}, actual: {}".format(3, count)


if __name__ == '__main__':
    main()
