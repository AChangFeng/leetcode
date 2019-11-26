#! python3
# -*- coding:UTF-8 -*-
"""
# 42. Trapping Rain Water
# Created on 2019/10/10 18:56
# trappingRainWater
# @author: ChangFeng
"""


class Solution:
    def trapBruteForce(self, height) -> int:
        '''
        Brute force
        TLE
        :param height:
        :return:
        '''
        if not height:
            return 0
        ans = 0
        for i in range(len(height)):
            max_left = max_right = 0
            for x in range(i, -1, -1):
                max_left = max(max_left, height[x])
            for y in range(i, len(height)):
                max_right = max(max_right, height[y])
            ans += min(max_left, max_right) - height[i]
        return ans

    def trapDp(self, height) -> int:
        '''
        Dynamic Programing
        :param height:
        :return:
        '''
        if not height:
            return 0
        size = len(height)
        left_max = [0] * size
        right_max = [0] * size
        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])

        for i in range(size - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        ans = 0
        for i in range(1, size - 1):
            ans += min(right_max[i], left_max[i]) - height[i]
        return ans

    def trapStack(self, height) -> int:
        ans = current = 0
        stack = []
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                # It means that the stack element can be popped. Pop the top element as top.
                top = stack[-1]
                stack.pop()
                if not stack:
                    break
                # Find the distance between the current element and the element at top of stack,
                # which is to be filled. distance} = current - st.top - 1
                distance = current - stack[-1] - 1
                # Find the bounded height
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                # Add resulting trapped water to answer
                print('--{},{}'.format(distance, bounded_height))
                ans += distance * bounded_height
            # Push current index to top of the stack
            stack.append(current)
            # Move current to the next position
            current += 1
        return ans

    def trap(self, height) -> int:
        left_max = right_max = ans = left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans


def main():
    # test_case = [5, 2, 1, 2, 1, 5]
    # print(Solution().trap(test_case))
    # test_case = [2, 1, 0, 1, 3]
    # print(Solution().trap(test_case))
    test_case = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trapStack(test_case))
    print(Solution().trap(test_case))


if __name__ == '__main__':
    main()
