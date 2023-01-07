"""

"""
"""
算法：数学排列组合计数
功能：全排列计数，选取comb计数，隔板法，错位排列，斯特林数、卡特兰数，容斥原理，可以通过乘法逆元快速求解组合数与全排列数
题目：


L2338 统计理想数组的数目（https://leetcode.cn/problems/count-the-number-of-ideal-arrays/）枚举可行的元素组合序列使用隔板法进行计数
L0634 寻找数组的错位排列（https://leetcode.cn/problems/find-the-derangement-of-an-array/）错位排列计数使用动态规划转移计算
P4071 排列计数（https://www.luogu.com.cn/problem/P4071）通过乘法逆元快速求解组合数与全排列数，同时递归计算错位排列数
P1287 盒子与球（https://www.luogu.com.cn/problem/P1287）斯特林数形式的DP，以及全排列数

P1375 小猫（https://www.luogu.com.cn/problem/P1375）卡特兰数
1259. 不相交的握手（https://leetcode.cn/problems/handshakes-that-dont-cross/）卡特兰数

参考：OI WiKi（xx）
卡特兰数（https://oi-wiki.org/math/combinatorics/catalan/）
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
from itertools import combinations
import math


class CombPerm:
    def __init__(self):
        return

    def cattelan_number(self, n, mod):
        # 卡特兰数 dp[i + 1] = sum(dp[j] * dp[i - j] for j in range(i + 1)) % MOD
        if n <= 1:
            return 1

        perm = self.produce_perm_mod(2*n+2, mod)
        # 利用乘法逆元求解组合数

        def comb(a, b):
            res = perm[a] * pow(perm[b], -1, mod) * pow(perm[a - b], -1, mod)
            return res % mod

        ans = (comb(2 * n, n) - comb(2 * n, n - 1)) % mod
        return ans

    @staticmethod
    def produce_perm_mod(n, mod):
        # 求全排列组合数
        perm = [1] * n
        for i in range(1, n):
            perm[i] = perm[i - 1] * i
            perm[i] %= mod

        return perm

    @staticmethod
    def combinnation(nums, k):
        return [list(item) for item in combinations(nums, k)]

    @staticmethod
    def permutation(nums, k):
        return [list(item) for item in permutations(nums, k)]

    @staticmethod
    def comb_perm(x, y):
        length = 10 ** 6 + 5
        mod = 10 ** 9 + 7

        # 求全排列组合数
        perm = [1] * length
        for i in range(1, length):
            perm[i] = perm[i - 1] * i
            perm[i] %= mod

        # 求错位排列组合数
        fault = [0] * length
        fault[0] = 1
        fault[2] = 1
        for i in range(3, length):
            fault[i] = (i - 1) * (fault[i - 1] + fault[i - 2])
            fault[i] %= mod

        # 利用乘法逆元求解组合数
        def comb(a, b):
            res = perm[a] * pow(perm[b], -1, mod) * pow(perm[a - b], -1, mod)
            return res % mod

        return comb(x, y)

    @staticmethod
    def main_p4071():
        import sys
        sys.setrecursionlimit(10 ** 8)

        def read():
            return sys.stdin.readline().strip()

        def ac(x):
            return sys.stdout.write(str(x) + '\n')

        length = 100
        mod = 10 ** 9 + 7

        # 求全排列组合数
        perm = [1] * length
        for i in range(1, length):
            perm[i] = perm[i - 1] * i
            perm[i] %= mod

        # 求错位排列组合数
        fault = [0] * length
        fault[0] = 1
        fault[2] = 1
        for i in range(3, length):
            fault[i] = (i - 1) * (fault[i - 1] + fault[i - 2])
            fault[i] %= mod

        # 利用乘法逆元求解组合数
        def comb(a, b):
            res = perm[a] * pow(perm[b], -1, mod) * pow(perm[a - b], -1, mod)
            return res % mod

        def main():
            t = int(input())
            for _ in range(t):
                n, m = [int(w) for w in input().strip().split() if w]
                while len(fault) <= n:
                    num = (len(fault) - 1) * (fault[-1] + fault[-2])
                    num %= mod
                    fault.append(num)

                    num = len(perm) * perm[-1]
                    num %= mod
                    perm.append(num)

                if m > n:
                    ac(0)
                else:
                    # m 个全排列乘 n-m 个错位排列
                    ans = (comb(n, m) * fault[n - m]) % mod
                    ac(ans)
            return

        main()
        return

    @staticmethod
    def main_p1287(n, r):

        @lru_cache(None)
        def dfs(a, b):
            # 斯特林数，把a个球放入b个盒子且不允许空盒的方案数
            if a < b or b < 0:
                return 0
            if a == b:
                return 1
            # 新球单独放新盒子，或者放入已经有的老盒子
            return dfs(a - 1, b - 1) + b * dfs(a - 1, b)

        # 由于是不同的球还要计算球的全排列
        x = dfs(n, r) * math.factorial(r)
        return x


class TestGeneral(unittest.TestCase):

    def test_comb_perm(self):
        cp = CombPerm()
        i = 500
        j = 10000
        mod = 10**9 + 7
        assert math.comb(j, i) % mod == cp.comb_perm(j, i)

        assert cp.main_p1287(3, 2) == 6

        nums = [1, 2, 3]
        ans = cp.combinnation(nums, 2)
        assert ans == [[1, 2], [1, 3], [2, 3]]

        ans = cp.permutation(nums, 1)
        assert ans == [[1], [2], [3]]

        return


if __name__ == '__main__':
    unittest.main()
