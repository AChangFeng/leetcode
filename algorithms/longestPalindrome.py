#! python3
# -*- coding:UTF-8 -*-
"""
# Created on 2019/10/22 19:00
# longestPalindrome
# @author: ChangFeng
"""


class Solution:
    def longestPalindrome2(self, s: str) -> str:
        """
        expand from center
        :param s:
        :return:
        """

        ans = ""
        max_len = len(ans)
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left:right + 1]) > max_len:
                    ans = s[left:right + 1]
                    max_len = len(ans)
                left -= 1
                right += 1
            if i < len(s) - 1 and s[i] == s[i + 1]:
                left, right = i, i + 1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if len(s[left:right + 1]) > max_len:
                        ans = s[left:right + 1]
                        max_len = len(ans)
                    left -= 1
                    right += 1
        return ans

    def longestPalindrome1(self, s: str) -> str:
        '''
        dp
        :param s:
        :return:
        '''
        if not s:
            return ""
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            if i < len(s) - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 2, len(s)):
                if i > j:
                    continue
                dp[i][j] = 1 if dp[i + 1][j - 1] and s[i] == s[j] else 0
        max_len = -1
        start, end = 0, 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j]:
                    if j - i > max_len:
                        max_len = j - i
                        start = i
                        end = j
        return s[start:end + 1]

    def longestPalindrome(self, s: str) -> str:
        """
        brute-force
        :param s:
        :return:
        """
        pass
        ans = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_palindrome(s[i:j + 1]) and len(s[i:j + 1]) > len(ans):
                    ans = s[i:j + 1]
        return ans

    def is_palindrome(self, s1):
        if not s1:
            return False
        l, r = 0, len(s1) - 1
        while l <= r:
            if s1[l] != s1[r]:
                return False
            l += 1
            r -= 1
        return True


def main():
    test_case = "cdda"
    print(Solution().longestPalindrome2(test_case))


if __name__ == '__main__':
    main()
