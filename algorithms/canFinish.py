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

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 0:
            return False
        completed = []
        dependents = {}
        in_degree = [0 for _ in range(numCourses)]
        for prerequisite in prerequisites:
            in_degree[prerequisite[0]] += 1
            if prerequisite[1] not in dependents:
                dependents.setdefault(prerequisite[1], [prerequisite[0]])
            else:
                dependents.get(prerequisite[1]).append(prerequisite[0])

        completed_num = 0
        for i in range(numCourses):
            if in_degree[i] == 0:
                completed.append(i)
                completed_num += 1
        while completed:
            if completed_num >= numCourses:
                return True
            completed_num += 1
            complete = completed.pop()
            if complete not in dependents:
                continue
            for dependent in dependents.get(complete):
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    completed.append(dependent)
        return False


def main():
    test_case = [2, [[0, 1],[1, 0]]]
    print(Solution().canFinish(*test_case))


if __name__ == '__main__':
    main()
