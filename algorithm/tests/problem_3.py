
import bisect
import itertools
import random
from typing import List
import heapq
import math
import re
import unittest
from collections import defaultdict, Counter, deque
from functools import lru_cache

from sortedcontainers import SortedList, SortedDict, SortedSet

from sortedcontainers import SortedDict
import heapq
from itertools import combinations
from sortedcontainers import SortedList



# 标准并查集
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1] * n
        self.part = n

    def find(self, x):
        if x != self.root[x]:
            # 在查询的时候合并到顺带直接根节点
            root_x = self.find(self.root[x])
            self.root[x] = root_x
            return root_x
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] >= self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        # 将非根节点的秩赋0
        self.size[root_x] = 0
        self.part -= 1
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_root_part(self):
        # 获取每个根节点对应的组
        part = defaultdict(list)
        n = len(self.root)
        for i in range(n):
            part[self.find(i)].append(i)
        return part

    def get_root_size(self):
        # 获取每个根节点对应的组大小
        size = defaultdict(int)
        n = len(self.root)
        for i in range(n):
            size[self.find(i)] = self.size[self.find(i)]
        return size


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        #roads.sort(key=lambda x: x[2])
        dct = [dict() for _ in range(n+1)]

        for a, b, c in roads:
            dct[a][b] = c
            dct[b][a] = c
        visit = [float("inf")]*(n+1)
        stack = [[0, 1]]
        while stack:
            dis, i = heapq.heappop(stack)
            if visit[i] <= dis:
                continue
            visit[i] = dis
            for j in dct[i]:
                heapq.heappush(stack, [min(dis, dis[i][j]), j])
        return visit[n]




class TestGeneral(unittest.TestCase):
    def test_solution(self):
        assert Solution().bestClosingTime("YYNY") == 2

        return


if __name__ == '__main__':
    unittest.main()