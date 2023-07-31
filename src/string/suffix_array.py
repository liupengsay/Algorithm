import unittest

from src.fast_io import FastIO

"""
算法：后缀数组
功能：生成字符串的后缀排序
参考：OI WiKi（https://oi-wiki.org/string/sa/）
题目：

===================================力扣===================================
1754. 构造字典序最大的合并字符串（https://leetcode.cn/problems/largest-merge-of-two-strings/）
1698. 字符串的不同子字符串个数（https://leetcode.cn/problems/number-of-distinct-substrings-in-a-string/）经典后缀数组应用题，利用height特性

===================================洛谷===================================
P3809 【模板】后缀排序（https://www.luogu.com.cn/problem/P3809）

===================================AcWing=====================================
140. 后缀数组（https://www.acwing.com/problem/content/142/）后缀数组模板题

"""


class SuffixArray:
    def __init__(self, ind: dict):
        self.ind = ind
        return

    def get_array(self, s):
        # sa[i]:排名为i的后缀的起始位置
        # rk[i]:起始位置为i的后缀的排名
        # height[i]: 第i名的后缀与它前一名的后缀的最长公共前缀  # 高度数组的定义，所有高度之和就是相同子串的个数
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


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lc_1754_1(word1: str, word2: str) -> str:
        # 模板：后缀数组计算后缀的字典序大小
        ind = {chr(ord("a") - 1 + i): i for i in range(27)}
        word = word1 + chr(ord("a")-1) + word2
        sa, rk, height = SuffixArray(ind).get_array(word)
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

    @staticmethod
    def lc_1754_2(word1: str, word2: str) -> str:
        # 模板：贪心比较后缀的字典序大小
        merge = ""
        i = j = 0
        m, n = len(word1), len(word2)
        while i < m and j < n:
            if word1[i:] > word2[j:]:
                merge += word1[i]
                i += 1
            else:
                merge += word2[j]
                j += 1
        merge += word1[i:]
        merge += word2[j:]
        return merge

    @staticmethod
    def lg_3809(ac=FastIO()):
        # 模板：计算数组的后缀排序
        words = [str(x) for x in range(10)] + [chr(i + ord("A")) for i in range(26)] + [chr(i + ord("a")) for i in
                                                                                        range(26)]
        ind = {st: i for i, st in enumerate(words)}
        s = ac.read_str()
        sa = SuffixArray(ind)
        ans, _, _ = sa.get_array(s)
        ac.lst([x + 1 for x in ans])
        return

    @staticmethod
    def ac_140(ac=FastIO()):
        # 模板：后缀数组模板题
        ind = {chr(ord("a") + i): i for i in range(26)}
        sa, rk, height = SuffixArray(ind).get_array(ac.read_str())
        ac.lst(sa)
        ac.lst(height)
        return

    @staticmethod
    def lc_1698(s: str) -> int:
        # 模板：经典后缀数组应用题，利用 height 特性
        ind = {chr(ord("a") + i): i for i in range(26)}
        # 高度数组的定义，所有高度之和就是相同子串的个数
        sa, rk, height = SuffixArray(ind).get_array(s)
        n = len(s)
        print(height)
        return n*(n+1)//2 - sum(height)


class TestGeneral(unittest.TestCase):

    def test_suffix_array(self):
        return


if __name__ == '__main__':
    unittest.main()