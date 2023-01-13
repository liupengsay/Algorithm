import unittest

from typing import List

"""
算法：矩阵DP、二维DP
功能：在二维矩阵上进行转移的DP，经典的有矩阵前缀和，矩阵区间和，正方形最大边长或面积，编辑距离，公共子序列，最长回文子串
题目：
L2435 矩阵中和能被 K 整除的路径（https://leetcode.cn/problems/paths-in-matrix-whose-sum-is-divisible-by-k/）利用模 K 的特点进行路径计算
L2088 统计农场中肥沃金字塔的数目（https://leetcode.cn/problems/count-fertile-pyramids-in-a-land/）类似求正方形的边长和面积进行矩阵DP
P1681 最大正方形II（https://www.luogu.com.cn/problem/P1681）求黑白格子相间的最大正方形面积
221. 最大正方形（https://leetcode.cn/problems/maximal-square/）求全为 1 的最大正方形面积

P2049 魔术棋子（https://www.luogu.com.cn/problem/P2049）求左上角到右下角所有路径的乘积取模数
P2138 小Z的关系距离（https://www.luogu.com.cn/problem/P2138）最长公共子序列

P2268 [HNOI2002]DNA分子的最佳比对（https://www.luogu.com.cn/problem/P2268）类似编辑距离
72. 编辑距离（https://leetcode.cn/problems/edit-distance/）矩阵DP
P2301 就是干！（https://www.luogu.com.cn/problem/P2301）矩阵DP，注意最小值的更新处理
参考：OI WiKi（xx）
"""


class MatrixDP:
    def __init__(self):
        return

    @staticmethod
    def min_distance(word1: str, word2: str):
        m, n = len(word1), len(word2)
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        # 编辑距离注意起始开头的边界条件
        for i in range(m + 1):
            dp[i][n] = m - i
        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 删除，插入，替换
                dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j + 1] + 1, dp[i + 1][j + 1] + int(word1[i] != word2[j]))
        return dp[0][0]

    @staticmethod
    def path_mul_mod(m, n, k, grid):
        # 求矩阵左上角到右下角的乘积取模数
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0] % k)
        for i in range(1, m):
            x = grid[i][0]
            for p in dp[i - 1][0]:
                dp[i][0].add((p * x) % k)
        for j in range(1, n):
            x = grid[0][j]
            for p in dp[0][j - 1]:
                dp[0][j].add((p * x) % k)

        for i in range(1, m):
            for j in range(1, n):
                x = grid[i][j]
                for p in dp[i][j - 1]:
                    dp[i][j].add((p * x) % k)
                for p in dp[i - 1][j]:
                    dp[i][j].add((p * x) % k)
        ans = sorted(list(dp[-1][-1]))
        return ans

    @staticmethod
    def maximal_square(matrix: List[List[str]]) -> int:

        # 求全为 1 的最大正方形面积
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    # 转移公式
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    if dp[i + 1][j + 1] > ans:
                        ans = dp[i + 1][j + 1]
        return ans ** 2


class TestGeneral(unittest.TestCase):

    def test_matrix_dp(self):
        md = MatrixDP()
        matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
            "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
        assert md.maximal_square(matrix) == 4
        return


if __name__ == '__main__':
    unittest.main()
