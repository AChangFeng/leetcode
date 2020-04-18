#! python3
# -*- coding:UTF-8 -*-
"""
# 301. Remove Invalid Parentheses
# Created on 2020/4/17 19:18
# removeInvalidParentheses
# @author: ChangFeng
"""
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """
        https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution
        """
        ans = []

        def helper(str_to_check, start_to_count, start_to_remove, pair):
            count, count_i = 0, start_to_count
            for count_i in range(start_to_count, len(str_to_check)):
                if str_to_check[count_i] == pair[0]:
                    count += 1
                if str_to_check[count_i] == pair[1]:
                    count -= 1
                if count >= 0:
                    continue
                for j in range(start_to_remove, count_i + 1):
                    if str_to_check[j] == pair[1] and (j == start_to_remove or str_to_check[j - 1] != pair[1]):
                        helper(str_to_check[:j] + str_to_check[j + 1:], count_i, j, pair)
                return

            reversed_ss = str_to_check[::-1]
            if pair[0] == "(":
                helper(reversed_ss, 0, 0, [")", "("])
            else:
                ans.append(reversed_ss)

        helper(s, 0, 0, ["(", ")"])
        return ans


def main():
    test_case = "()())()"
    print(Solution().removeInvalidParentheses(test_case))


if __name__ == '__main__':
    main()
