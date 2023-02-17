
import unittest
import heapq
from functools import reduce
from operator import xor

"""

算法：nim游戏也叫公平组合游戏，属于博弈论范畴
功能：用来判断游戏是否存在必胜态与必输态，博弈DP类型
题目：

===================================洛谷===================================
P2197 【模板】nim 游戏（https://www.luogu.com.cn/problem/P2197）有一个神奇的结论：当n堆石子的数量异或和等于0时，先手必胜，否则先手必败

================================CodeForces================================
B. Stoned Game（https://codeforces.com/problemset/problem/1396/B）博弈贪心，使用大顶堆优先选取最大数量的石头做选择

参考：OI WiKi（https://oi-wiki.org/graph/lgv/）

"""


class Solution:
    def __init__(self):
        return

    @staticmethod
    def cf_1396b(nums):
        # 模板：博弈贪心，使用大顶堆优先选取最大数量的石头做选择
        heapq.heapify(nums)
        order = 0
        pre = 0
        while nums:
            num = -heapq.heappop(nums)
            num -= 1
            tmp = num
            if pre:
                heapq.heappush(nums, -pre)
            pre = tmp
            order = 1 - order
        return "HL" if not order else "T"


class Nim:
    def __init__(self, lst):
        self.lst = lst
        return

    def gen_result(self):
        return reduce(xor, self.lst) != 0


class TestGeneral(unittest.TestCase):
    def test_euler_phi(self):
        nim = Nim([0, 2, 3])
        assert nim.gen_result()
        return


if __name__ == '__main__':
    unittest.main()
