import bisect
import decimal
import heapq
from types import GeneratorType
from math import inf
import sys
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heappushpop
from functools import cmp_to_key
from collections import defaultdict, Counter, deque
import math
from functools import lru_cache
from heapq import nlargest
from functools import reduce
from decimal import Decimal
import random
from itertools import combinations, permutations
from operator import xor, add
from operator import mul
from typing import List, Callable, Dict, Set, Tuple, DefaultDict
from heapq import heappush, heappop, heapify

# sys.setrecursionlimit(10**8)设置最大递归次数


class FastIO:
    def __init__(self):
        self.seed = random.randint(0, 10 ** 9 + 7)
        self.dct = dict()
        return

    @staticmethod
    def read_int():
        return int(sys.stdin.readline().strip())

    @staticmethod
    def read_float():
        return float(sys.stdin.readline().strip())

    @staticmethod
    def read_ints():
        return map(int, sys.stdin.readline().strip().split())

    @staticmethod
    def read_floats():
        return map(float, sys.stdin.readline().strip().split())

    @staticmethod
    def read_ints_minus_one():
        return map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())

    @staticmethod
    def read_list_ints():
        return list(map(int, sys.stdin.readline().strip().split()))

    @staticmethod
    def read_list_floats():
        return list(map(float, sys.stdin.readline().strip().split()))

    @staticmethod
    def read_list_ints_minus_one():
        return list(map(lambda x: int(x) - 1,
                        sys.stdin.readline().strip().split()))

    @staticmethod
    def read_str():
        return sys.stdin.readline().strip()

    @staticmethod
    def read_list_strs():
        return sys.stdin.readline().strip().split()

    @staticmethod
    def read_list_str():
        return list(sys.stdin.readline().strip())

    @staticmethod
    def st(x):
        return sys.stdout.write(str(x) + '\n')

    @staticmethod
    def lst(x):
        return sys.stdout.write(" ".join(str(w) for w in x) + '\n')

    @staticmethod
    def round_5(f):
        res = int(f)
        if f - res >= 0.5:
            res += 1
        return res

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a, b):
        return a if a < b else b

    @staticmethod
    def ceil(a, b):
        return a // b + int(a % b != 0)

    def ask(self, lst):
        # CF交互题输出询问并读取结果
        self.lst(lst)
        sys.stdout.flush()
        res = self.read_int()
        # 记得任何一个输出之后都要 sys.stdout.flush() 刷新
        return res

    def out_put(self, lst):
        # CF交互题输出最终答案
        self.lst(lst)
        sys.stdout.flush()
        return

    @staticmethod
    def accumulate(nums):
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        return pre

    def add(self, x, cnt=1):
        self.dct[x ^ self.seed] = self.dct.get(x ^ self.seed, 0) + cnt
        return

    def rem(self, x, cnt=1):
        self.dct[x ^ self.seed] -= cnt
        return


class Solution:
    def __init__(self):
        return

    @staticmethod
    def main(ac=FastIO()):

        return


Solution().main()
import bisect
import decimal
import heapq
from types import GeneratorType
from math import inf
import sys
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heappushpop
from functools import cmp_to_key
from collections import defaultdict, Counter, deque
import math
from functools import lru_cache
from heapq import nlargest
from functools import reduce
from decimal import Decimal
import random
from itertools import combinations, permutations
from operator import xor, add
from operator import mul
from typing import List, Callable, Dict, Set, Tuple, DefaultDict
from heapq import heappush, heappop, heapify

# sys.setrecursionlimit(10**8)设置最大递归次数


class FastIO:
    def __init__(self):
        self.seed = random.randint(0, 10 ** 9 + 7)
        self.dct = dict()
        return

    @staticmethod
    def read_int():
        return int(sys.stdin.readline().strip())

    @staticmethod
    def read_float():
        return float(sys.stdin.readline().strip())

    @staticmethod
    def read_ints():
        return map(int, sys.stdin.readline().strip().split())

    @staticmethod
    def read_floats():
        return map(float, sys.stdin.readline().strip().split())

    @staticmethod
    def read_ints_minus_one():
        return map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())

    @staticmethod
    def read_list_ints():
        return list(map(int, sys.stdin.readline().strip().split()))

    @staticmethod
    def read_list_floats():
        return list(map(float, sys.stdin.readline().strip().split()))

    @staticmethod
    def read_list_ints_minus_one():
        return list(map(lambda x: int(x) - 1,
                        sys.stdin.readline().strip().split()))

    @staticmethod
    def read_str():
        return sys.stdin.readline().strip()

    @staticmethod
    def read_list_strs():
        return sys.stdin.readline().strip().split()

    @staticmethod
    def read_list_str():
        return list(sys.stdin.readline().strip())

    @staticmethod
    def st(x):
        return sys.stdout.write(str(x) + '\n')

    @staticmethod
    def lst(x):
        return sys.stdout.write(" ".join(str(w) for w in x) + '\n')

    @staticmethod
    def round_5(f):
        res = int(f)
        if f - res >= 0.5:
            res += 1
        return res

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a, b):
        return a if a < b else b

    @staticmethod
    def ceil(a, b):
        return a // b + int(a % b != 0)

    def ask(self, lst):
        # CF交互题输出询问并读取结果
        self.lst(lst)
        sys.stdout.flush()
        res = self.read_int()
        # 记得任何一个输出之后都要 sys.stdout.flush() 刷新
        return res

    def out_put(self, lst):
        # CF交互题输出最终答案
        self.lst(lst)
        sys.stdout.flush()
        return

    @staticmethod
    def accumulate(nums):
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        return pre

    def add(self, x, cnt=1):
        self.dct[x ^ self.seed] = self.dct.get(x ^ self.seed, 0) + cnt
        return

    def rem(self, x, cnt=1):
        self.dct[x ^ self.seed] -= cnt
        return


class Solution:
    def __init__(self):
        return

    @staticmethod
    def main(ac=FastIO()):

        return


Solution().main()
