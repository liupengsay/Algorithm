"""
算法：后缀数组
功能：生成字符串的后缀排序
题目：P3809 【模板】后缀排序（https://www.luogu.com.cn/problem/P3809）

【1754. 构造字典序最大的合并字符串】（https://leetcode.cn/problems/largest-merge-of-two-strings/solution/by-liupengsay-fhoo/）
参考：OI WiKi（https://oi-wiki.org/string/sa/）
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


class SuffixArray:
    def __init__(self, ind):
        self.ind = ind
        return

    def doubling(self, s):
        # sa[i]:排名为i的后缀的起始位置
        # rk[i]:起始位置为i的后缀的排名
        # height[i]: 第i名的后缀与它前一名的后缀的最长公共前缀
        n = len(s)
        sa = []
        rk = []
        for i in range(n):
            rk.append(self.ind[s[i]])  # 刚开始时，每个后缀的排名按照它们首字母的排序
            sa.append(i)  # 而排名第i的后缀就是从i开始的后缀

        l = 0  # l是已经排好序的长度，现在要按2l长度排序
        sig = len(self.ind)  # sig是unique的排名的个数，初始是字符集的大小
        while True:
            p = []
            # 对于长度小于l的后缀来说，它们的第二关键字排名肯定是最小的，因为都是空的
            for i in range(n - l, n):
                p.append(i)
            # 对于其它长度的后缀来说，起始位置在`sa[i]`的后缀排名第i，而它的前l个字符恰好是起始位置为`sa[i]-l`的后缀的第二关键字
            for i in range(n):
                if sa[i] >= l:
                    p.append(sa[i] - l)
            # 然后开始基数排序，先对第一关键字进行统计
            # 先统计每个值都有多少
            cnt = [0] * sig
            for i in range(n):
                cnt[rk[i]] += 1
            # 做个前缀和，方便基数排序
            for i in range(1, sig):
                cnt[i] += cnt[i - 1]
            # 然后利用基数排序计算新sa
            for i in range(n - 1, -1, -1):
                cnt[rk[p[i]]] -= 1
                sa[cnt[rk[p[i]]]] = p[i]

            # 然后利用新sa计算新rk
            def equal(i, j, l):
                if rk[i] != rk[j]:
                    return False
                if i + l >= n and j + l >= n:
                    return True
                if i + l < n and j + l < n:
                    return rk[i + l] == rk[j + l]
                return False

            sig = -1
            tmp = [None] * n
            for i in range(n):
                # 直接通过判断第一关键字的排名和第二关键字的排名来确定它们的前2l个字符是否相同
                if i == 0 or not equal(sa[i], sa[i - 1], l):
                    sig += 1
                tmp[sa[i]] = sig
            rk = tmp
            sig += 1
            if sig == n:
                break
            # 更新有效长度
            l = l << 1 if l > 0 else 1
        # 计算height数组
        k = 0
        height = [0] * n
        for i in range(n):
            if rk[i] > 0:
                j = sa[rk[i] - 1]
                while i + k < n and j + k < n and s[i + k] == s[j + k]:
                    k += 1
                height[rk[i]] = k
                k = max(0, k - 1)  # 下一个height的值至少从max(0,k-1)开始
        return sa, rk, height

    def largestMerge(self, word1: str, word2: str) -> str:
        word = word1 + [k for k in self.ind if self.ind[k] == 0][0] + word2
        sa, rk, height = self.doubling(word)
        m, n = len(word1), len(word2)
        i = 0
        j = 0
        merge = ""
        while i < m and j < n:
            if rk[i] > rk[j + m + 1]:
                merge += word1[i]
                i += 1
            else:
                merge += word2[j]
                j += 1
        merge += word1[i:]
        merge += word2[j:]
        return merge


class TestGeneral(unittest.TestCase):

    def test_suffix_array(self):
        words = [str(x) for x in range(10)] + [chr(i + ord("A"))
                                               for i in range(26)] + [chr(i + ord("a")) for i in range(26)]
        ind = {st: i for i, st in enumerate(words)}
        nt = SuffixArray(ind)
        assert nt.largestMerge("abcabc", "abdcaba") == "abdcabcabcaba"
        return


if __name__ == '__main__':
    unittest.main()