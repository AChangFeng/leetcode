#! python3
# -*- coding:UTF-8 -*-
"""
# 207. Course Schedule
# Created on 2020/3/18 19:14
# canFinish
# @author: ChangFeng
"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 0:
            return False
        queue = []
        courses = [0 for _ in range(numCourses)]
        # 将有依赖的课放到数组中
        for prerequisite in prerequisites:
            courses[prerequisite[0]] += 1
        # 将没有依赖的课放到queue中
        for i in range(numCourses):
            if courses[i] == 0:
                queue.append(i)
        # 遍历
        while queue:
            # 取出没有依赖的课
            start_course = queue.pop()
            # 找其依赖的课，将其-1
            for prerequisite in prerequisites:
                if prerequisite[1] == start_course:
                    courses[prerequisite[0]] -= 1
                    # 如果其依赖的课已经没有依赖其的课了，则可以放入队列
                    if courses[prerequisite[0]] == 0:
                        queue.append(prerequisite[0])
        for course in courses:
            if course != 0:
                return False
        return True


def main():
    test_case = [2, [[0, 1]]]
    print(Solution().canFinish(*test_case))


if __name__ == '__main__':
    main()
