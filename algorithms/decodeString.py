#! python3
# -*- coding:UTF-8 -*-
"""
394. Decode String
# Created on 2019/12/31 17:30
# decodeString
# @author: ChangFeng
"""


class Solution:
    def decodeString(self, s: str) -> str:
        num = []
        num_str = ""
        stack = []
        ans = []
        for c in s:
            if c.isdigit():
                num_str += c
            elif c == '[':
                stack.append(c)
                if num_str:
                    num.append(int(num_str))
                    num_str = ""
            elif c == ']':
                tmp = ''
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                stack.pop()
                tmp = tmp * num.pop()
                if not num:
                    ans.append(tmp)
                else:
                    stack.append(tmp)
            else:
                if not stack:
                    ans.append(c)
                else:
                    stack.append(c)
        return ''.join(ans)

    def decodeString(self, s):
        stack = []
        cur_num = 0
        cur_string = ''
        for c in s:
            if c == '[':
                stack.append(cur_string)
                stack.append(cur_num)
                cur_string = ''
                cur_num = 0
            elif c == ']':
                num = stack.pop()
                prev_string = stack.pop()
                cur_string = prev_string + num * cur_string
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_string += c
        return cur_string


def main():
    test_case = '"3[a]2[b4[F]c]"'
    print(Solution().decodeString(test_case))


if __name__ == '__main__':
    main()
