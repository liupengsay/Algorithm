

"""
线性基也叫Hamel基
WiKi: https://oi-wiki.org/math/linear-algebra/basis/
题目：P3812 【模板】线性基（https://www.luogu.com.cn/problem/P3812）

"""
import bisect
import random
import re
import unittest

from typing import List
import heapq
import math
from collections import defaultdict, Counter, deque
from functools import lru_cache
from itertools import combinations
from sortedcontainers import SortedList, SortedDict, SortedSet

from sortedcontainers import SortedDict
from functools import reduce
from operator import xor
from functools import lru_cache

import random
from itertools import permutations, combinations
import numpy as np

from decimal import Decimal

import heapq
import copy


class LinearBasis:
    def __init__(self, lst):
        """线性基类由原数组lst生成"""
        self.n = 64
        self.lst = lst
        self.gen_linear_basis()
        return

    def gen_linear_basis(self):
        self.linear_basis = [0] * self.n
        for num in self.lst:
            self.add(num)
        return

    def add(self, num):
        """加入新数字到线性基"""
        for i in range(self.n - 1, -1, -1):
            if num & (1 << i):
                if self.linear_basis[i]:
                    num ^= self.linear_basis[i]
                else:
                    self.linear_basis[i] = num
                    break
        return

    def query_xor(self, num):
        """查询数字是否可以由原数组中数字异或得到"""
        for i in range(self.n, -1, -1):
            if num & (1 << i):
                num ^= self.linear_basis[i]
        return num == 0

    def query_max(self):
        """查询原数组的最大异或和"""
        ans = 0
        for i in range(self.n - 1, -1, -1):
            if ans ^ self.linear_basis[i] > ans:
                ans ^= self.linear_basis[i]
        return ans

    def query_min(self):
        """查询原数组的最小异或和"""
        if 0 in self.lst or self.query_xor(0):
            return 0
        for i in range(0, self.n + 1):
            if self.linear_basis[i]:
                return self.linear_basis[i]
        return 0

    def query_k_rank(self, k):
        """查询原数组异或和的第K小"""
        if self.query_xor(0):
            k -= 1
        ans = 0
        for i in range(self.n - 1, -1, -1):
            if k & (1 << i) and self.linear_basis[i]:
                ans ^= self.linear_basis[i]
                k ^= (1 << i)
        return ans if not k else -1

    def query_k_smallest(self, num):
        """查询数字是原数组中数字异或的第K小"""
        if num == 0:
            return 1 if self.query_xor(0) else -1
        ans = 0
        for i in range(self.n - 1, -1, -1):
            if num & (self.linear_basis[i]):
                ans ^= (1 << i)
                num ^= self.linear_basis[i]
        return ans + 1 if not num else -1


class TestGeneral(unittest.TestCase):
    def test_euler_phi(self):
        lst = [0, 1, 2, 4, 8, 16]
        m = len(lst)

        # 计算所有的异或和
        nums = []
        for i in range(1, 1 << m):
            nums.append(reduce(xor, [lst[j] for j in range(m) if i & (1 << j)]))
        nums = sorted(set(nums))

        # 查询最大最小以及是否存在对应异或值
        lb = LinearBasis(lst)
        assert lb.query_max() == 31
        assert lb.query_min() == 0
        assert lb.query_xor(20)

        # 查询第k小与异或和是第几小
        n = len(nums)
        for i in range(n):
            assert lb.query_k_rank(i + 1) == nums[i]
            assert lb.query_k_smallest(nums[i]) == i + 1

        # 超出范围
        assert lb.query_k_rank(len(nums) + 1) == -1
        assert lb.query_k_smallest(nums[-1] + 1) == -1
        return


if __name__ == '__main__':
    unittest.main()