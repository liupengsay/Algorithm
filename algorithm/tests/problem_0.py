from __future__ import division
import copy
import random
import heapq
import math
import sys
import bisect
import datetime
from functools import lru_cache
from collections import deque
from collections import Counter
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from decimal import Decimal, getcontext, MAX_PREC
from types import GeneratorType
from functools import cmp_to_key

inf = float("inf")
sys.setrecursionlimit(10000000)

getcontext().prec = MAX_PREC


class FastIO:
    def __init__(self):
        return

    @staticmethod
    def _read():
        return sys.stdin.readline().strip()

    def read_int(self):
        return int(self._read())

    def read_float(self):
        return float(self._read())

    def read_ints(self):
        return map(int, self._read().split())

    def read_floats(self):
        return map(float, self._read().split())

    def read_ints_minus_one(self):
        return map(lambda x: int(x) - 1, self._read().split())

    def read_list_ints(self):
        return list(map(int, self._read().split()))

    def read_list_floats(self):
        return list(map(float, self._read().split()))

    def read_list_ints_minus_one(self):
        return list(map(lambda x: int(x) - 1, self._read().split()))

    def read_str(self):
        return self._read()

    def read_list_strs(self):
        return self._read().split()

    def read_list_str(self):
        return list(self._read())

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
    def bootstrap(f, stack=[]):
        def wrappedfunc(*args, **kwargs):
            if stack:
                return f(*args, **kwargs)
            else:
                to = f(*args, **kwargs)
                while True:
                    if isinstance(to, GeneratorType):
                        stack.append(to)
                        to = next(to)
                    else:
                        stack.pop()
                        if not stack:
                            break
                        to = stack[-1].send(to)
                return to
        return wrappedfunc


def square(x):
    return x*x

def sqrt(x):
    return math.sqrt(x)


def main(ac=FastIO()):
    sx, sy, tx, ty = ac.read_list_floats()
    ans = inf
    ans = ac.min(ans, sqrt(square(sx + tx + 2) + square(sy - ty)))   # I型计算
    ans = ac.min(ans, sqrt(square(-sx - tx + 2) + square(sy - ty)))
    ans = ac.min(ans, sqrt(square(sx - tx) + square(sy + ty + 2)))
    ans = ac.min(ans, sqrt(square(sx - tx) + square(-sy - ty + 2)))

    ans = ac.min(ans, sqrt(square(-sx - ty + 2) + square(-sy - tx + 1)))  # Z型计算
    ans = ac.min(ans, sqrt(square(-sx - ty + 1) + square(-sy - tx + 2)))
    ans = ac.min(ans, sqrt(square(sx - ty + 2) + square(-sy + tx + 1)))
    ans = ac.min(ans, sqrt(square(sx - ty + 1) + square(-sy + tx + 2)))
    ans = ac.min(ans, sqrt(square(-sx + ty + 2) + square(-sy + tx + 1)))
    ans = ac.min(ans, sqrt(square(-sx + ty + 1) + square(-sy + tx + 2)))
    ans = ac.min(ans, sqrt(square(sx + ty + 2) + square(sy + tx + 1)))
    ans = ac.min(ans, sqrt(square(sx + ty + 1) + square(sy + tx + 2)))
    ac.st("%.3f" % ans)
    return


main()
