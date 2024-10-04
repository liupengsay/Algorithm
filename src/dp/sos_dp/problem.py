"""
Algorithm：sos_dp
Description：sum_of_subsets_dp|md_prefix_sum
Reference：https://codeforces.com/blog/entry/45223


====================================LeetCode====================================


=====================================AtCoder======================================
ABC100C（https://atcoder.jp/contests/arc100/tasks/arc100_c）sos_dp|classical|state_dp|bit_operation


=====================================LuoGu======================================

===================================CodeForces===================================
1234F（https://codeforces.com/contest/1234/problem/F）sos_dp|classical|state_dp|bit_operation
449D（https://codeforces.com/problemset/problem/449/D）sos_dp|fill_table|prefix_sum|diff_array|data_range|classical
1208F（https://codeforces.com/problemset/problem/1208/F）
383E（https://codeforces.com/contest/383/problem/E）sos_dp|classical|state_dp|bit_operation
165E（https://codeforces.com/contest/165/problem/E）sos_dp|classical|state_dp|bit_operation

"""

from src.utils.fast_io import FastIO


class Solution:
    def __init__(self):
        return

    @staticmethod
    def cf_1234f(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1234/problem/F
        tag: sos_dp|classical|state_dp|bit_operation
        """
        lst = [ord(w) - ord("a") for w in ac.read_str()]
        n = len(lst)
        dp = [0] * (1 << 20)
        for i in range(n):
            cur = 1 << lst[i]
            dp[cur] = 1
            for j in range(i + 1, n):
                if cur & (1 << lst[j]):
                    break
                cur |= (1 << lst[j])
                dp[cur] = j - i + 1

        for i in range(1 << 20):
            for j in range(20):
                if not i & (1 << j):
                    dp[i | (1 << j)] = ac.max(dp[i | (1 << j)], dp[i])

        ans = 1
        tot = (1 << 20) - 1
        for i in range(n):
            cur = 1 << lst[i]
            for j in range(i + 1, n):
                if cur & (1 << lst[j]):
                    break
                cur |= 1 << lst[j]
                ans = ac.max(ans, j - i + 1 + dp[tot ^ cur])
        ac.st(ans)
        return

    @staticmethod
    def cf_165e(ac=FastIO()):
        """
        url: https://codeforces.com/contest/165/problem/E
        tag: sos_dp|classical|state_dp|bit_operation
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        dp = [-1] * (1 << 22)
        for num in nums:
            dp[num] = num
        for i in range(1 << 22):
            if dp[i] == -1:
                continue
            for j in range(22):
                if not i & (1 << j):
                    dp[i | (1 << j)] = dp[i]
        ans = [-1] * n
        tot = (1 << 22) - 1
        for i in range(n):
            ans[i] = dp[nums[i] ^ tot]
        ac.lst(ans)
        return

    @staticmethod
    def cf_383e(ac=FastIO()):
        """
        url: https://codeforces.com/contest/383/problem/E
        tag: sos_dp|classical|state_dp|bit_operation
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        dp = [-1] * (1 << 22)
        for num in nums:
            dp[num] = num
        for i in range(1 << 22):
            if dp[i] == -1:
                continue
            for j in range(22):
                if not i & (1 << j):
                    dp[i | (1 << j)] = dp[i]
        ans = [-1] * n
        tot = (1 << 22) - 1
        for i in range(n):
            ans[i] = dp[nums[i] ^ tot]
        ac.lst(ans)
        return

    @staticmethod
    def arc_100c(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/arc100/tasks/arc100_c
        tag: sos_dp|classical|state_dp|bit_operation
        """
        n = ac.read_int()
        nums = ac.read_list_ints()

        def merge(x1, y1, x2, y2):
            if x1 >= x2:
                return x1, max(x2, y1)
            return x2, max(x1, y2)

        maximum = nums[:]
        second = [0] * (1 << n)
        for j in range(n):
            for i in range(1 << n):
                if i & (1 << j):
                    x, y = maximum[i], second[i]
                    a, b = maximum[i ^ (1 << j)], second[i ^ (1 << j)]
                    maximum[i], second[i] = merge(x, y, a, b)
        ans = 0
        for i in range(1, 1 << n):
            ans = max(ans, maximum[i] + second[i])
            ac.st(ans)
        return

    @staticmethod
    def cf_449d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/449/D
        tag: sos_dp|fill_table|prefix_sum|diff_array|data_range|classical
        """
        n = ac.read_int()
        mod = 10 ** 9 + 7
        m = 20
        nums = ac.read_list_ints()
        ceil = 1 << m
        p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = (p[i - 1] * 2) % mod
        dp = [0] * ceil
        for num in nums:
            dp[num] += 1
        for j in range(m):
            for i in range(ceil - 1, -1, -1):
                if not (i >> j) & 1:
                    dp[i] += dp[i | (1 << j)]
        assert dp[0] == n
        for i in range(ceil - 1, -1, -1):
            dp[i] = (p[dp[i]] - 1) % mod
        for j in range(m):
            for i in range(ceil - 1, -1, -1):
                if not (i >> j) & 1:
                    dp[i] -= dp[i | (1 << j)]
                    dp[i] %= mod
        ac.st(dp[0])
        return
