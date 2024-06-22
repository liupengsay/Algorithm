"""
Algorithm：prime_factorization|min_prime|factorization
Description：

====================================LeetCode====================================
2183（https://leetcode.cn/problems/count-array-pairs-divisible-by-k/description/）brute_force|counter|group_by_mul|classical
2584（https://leetcode.cn/problems/split-the-array-to-make-coprime-products/）prime_factorization|counter
=====================================LuoGu======================================
P8319（https://www.luogu.com.cn/problem/P8319）prime_factorization|counter

===================================CodeForces===================================
1176D（https://codeforces.com/contest/1176/problem/D）construction|greedy|implemention
1884D（https://codeforces.com/contest/1884/problem/D）factor_dp|gcd_pair|counter|classical
1900D（https://codeforces.com/contest/1900/problem/D）inclusion_exclusion|gcd_pair|counter|classical
1034A（https://codeforces.com/contest/1034/problem/A）prime_factorization
1366D（https://codeforces.com/problemset/problem/1366/D）min_prime|construction
1978E（https://codeforces.com/contest/1978/problem/F）union_find|matrix|math|brain_teaser
1627D（https://codeforces.com/contest/1627/problem/D）euler_series|prime_factor|all_factor|implemention|brute_force
1499D（https://codeforces.com/contest/1499/problem/D）math|prime_factor_cnt|classical

====================================AtCoder=====================================
ABC215D（https://atcoder.jp/contests/abc215/tasks/abc215_d）prime_factorization

=====================================AcWing=====================================
199（https://www.acwing.com/problem/content/199/）factorial|prime_factorization

1（https://www.codechef.com/problems/COUNTN）min_prime|prime_number

"""
import math
from collections import Counter
from collections import defaultdict
from functools import reduce
from itertools import permutations
from typing import List

from src.graph.union_find.template import UnionFind
from src.mathmatics.number_theory.template import PrimeSieve
from src.mathmatics.prime_factor.template import PrimeFactor
from src.utils.fast_io import FastIO
from src.utils.fast_io import inf


class Solution:
    def __init__(self):
        return

    @staticmethod
    def ac_199(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/199/
        tag: factorial|prime_factorization
        """
        n = ac.read_int()
        pf = PrimeFactor(n)
        dct = defaultdict(int)
        for num in range(2, n + 1):
            for p, c in pf.prime_factor[num]:
                dct[p] += c
        for p in sorted(dct):
            ac.lst([p, dct[p]])
        return

    @staticmethod
    def lc_2584(nums: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/split-the-array-to-make-coprime-products/
        tag: prime_factorization|counter
        """
        pf = PrimeFactor(10 ** 6)
        n = len(nums)
        dct = defaultdict(list)
        for i, num in enumerate(nums):
            for p, _ in pf.prime_factor[num]:
                dct[p].append(i)

        diff = [0] * (n + 1)
        for p in dct:
            i, j = dct[p][0], dct[p][-1]
            a, b = i, j - 1
            if a <= b:
                diff[a] += 1
                diff[b + 1] -= 1
        for i in range(1, n + 1):
            diff[i] += diff[i - 1]
        for i in range(n - 1):
            if not diff[i]:
                return i
        return -1

    @staticmethod
    def cf_1366d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1366/D
        tag: min_prime|construction
        """
        ac.read_int()
        nums = ac.read_list_ints()
        ceil = max(nums)
        pf = PrimeFactor(ceil)
        ans1 = []
        ans2 = []
        for num in nums:
            p = pf.min_prime[num]
            v = num
            while v % p == 0:
                v //= p
            if v == 1:
                ans1.append(-1)
                ans2.append(-1)
            else:
                ans1.append(v)
                ans2.append(num // v)
        ac.lst(ans1)
        ac.lst(ans2)
        return

    @staticmethod
    def cf_1034a(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1034/problem/A
        tag: prime_factorization|min_prime|classical|hard
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        ceil = max(nums)
        pf = PrimeFactor(ceil)
        g = reduce(math.gcd, nums)
        cnt = [0] * (ceil + 1)
        for num in nums:
            b = num // g
            while b > 1:
                fac = pf.min_prime[b]  # classical_skills which can speed up a lot
                cnt[fac] += 1
                while b % fac == 0:
                    b //= fac
        res = max(cnt)
        if res == 0:
            ac.st(-1)
        else:
            ac.st(n - res)
        return

    @staticmethod
    def lg_p8319(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8319
        tag: prime_factorization|counter
        """
        q = ac.read_int()
        nums = [ac.read_int() for _ in range(q)]
        n = max(nums)
        f = [1] * (n + 1)
        pf = PrimeFactor(n)
        for x in range(2, n + 1):
            f[x] = f[x // pf.min_prime[x]] - 1 + pf.min_prime[x]

        for i in range(1, n + 1):
            f[i] = ac.max(f[i - 1], f[i])
        for num in nums:
            ac.st(f[num])
        return

    @staticmethod
    def cf_1034a(ac=FastIO()):

        n = ac.read_int()
        nums = ac.read_list_ints()
        ceil = max(nums)

        # 快速 1~ceil 的质数因子数
        p = [0] * (ceil + 1)
        for i in range(2, ceil + 1):
            if p[i] == 0:
                p[i] = i
                # 从 i*i 开始作为 p[j] 的最小质数因子
                for j in range(i * i, ceil + 1, i):
                    p[j] = i

        # gcd
        g = reduce(math.gcd, nums)
        cnt = [0] * (ceil + 1)
        for i in range(n):
            b = nums[i] // g
            while b > 1:
                #  num[i] 除掉 g 以后的质数因子数
                fac = p[b]
                # counter| 1 也可以记录由多少个因子
                cnt[fac] += 1
                while b % fac == 0:
                    b //= fac
        res = max(cnt)
        if res == 0:
            ac.st(-1)
        else:
            ac.st(n - res)
        return

    @staticmethod
    def lc_6334(nums: List[int]) -> int:
        # 非空子集乘积不含除 1 之外任何平方整除数，即乘积质数因子的幂次均为 1（bag_dp|counter）
        dct = {2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30}
        # 集合为质数因子幂次均为 1
        mod = 10 ** 9 + 7
        cnt = Counter(nums)
        pre = defaultdict(int)
        for num in cnt:
            if num in dct:
                cur = pre.copy()
                for p in pre:
                    if math.gcd(p, num) == 1:
                        cur[p * num] += pre[p] * cnt[num]
                        cur[p * num] %= mod
                cur[num] += cnt[num]
                pre = cur.copy()
        # 1 需要特殊处理
        p = pow(2, cnt[1], mod)
        ans = sum(pre.values()) * p
        ans += p - 1
        return ans % mod

    @staticmethod
    def cf_1366d(ac=FastIO()):
        ac.read_int()
        nums = ac.read_list_ints()
        ceil = max(nums)

        # 利用linear_sieve的思想最小的质因数
        min_div = [i for i in range(ceil + 1)]
        for i in range(2, len(min_div)):
            if min_div[i] != i:
                continue
            if i * i >= len(min_div):
                break
            for j in range(i, len(min_div)):
                if i * j >= len(min_div):
                    break
                if min_div[i * j] == i * j:
                    min_div[i * j] = i

        # construction结果
        ans1 = []
        ans2 = []
        for num in nums:
            p = min_div[num]
            v = num
            while v % p == 0:
                v //= p
            if v == 1:
                # 只有一个质因子
                ans1.append(-1)
                ans2.append(-1)
            else:
                ans1.append(v)
                ans2.append(num // v)
        ac.lst(ans1)
        ac.lst(ans2)
        return

    @staticmethod
    def lc_2183(nums: List[int], k: int) -> int:
        """
        url: https://leetcode.cn/problems/count-array-pairs-divisible-by-k/description/
        tag: brute_force|counter|group_by_mul|classical
        """
        # 可以所有因子遍历brute_forcecounter解决，正解为按照 k 的最大公因数分组
        nt = PrimeFactor(10 ** 5)
        ans = 0
        dct = defaultdict(int)
        for i, num in enumerate(nums):
            w = k // math.gcd(num, k)
            ans += dct[w]
            for w in nt.all_factor[num]:
                dct[w] += 1
        return ans

    @staticmethod
    def lc_2464(nums: List[int]) -> int:
        #  1 到 n 的数所有的质因子并动态规划counter
        nt = PrimeFactor(max(nums))
        ind = dict()
        n = len(nums)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i, num in enumerate(nums):
            while num > 1:
                p = nt.min_prime[num]
                while num % p == 0:
                    num //= p
                if p not in ind or dp[i] < dp[ind[p]]:
                    ind[p] = i
                if dp[ind[p]] + 1 < dp[i + 1]:
                    dp[i + 1] = dp[ind[p]] + 1
                if dp[i] + 1 < dp[i + 1]:
                    dp[i + 1] = dp[i] + 1
        return dp[-1] if dp[-1] < inf else -1

    @staticmethod
    def lc_8041(nums: List[int]) -> int:
        # preprocess幂次为奇数的质因子hash分组counter
        n = len(nums)
        nt = PrimeFactor(n)
        dct = defaultdict(int)
        for i in range(1, n + 1):
            cur = nt.prime_factor[i]
            cur = [p for p, c in cur if c % 2]
            dct[tuple(cur)] += nums[i - 1]
        return max(dct.values())

    @staticmethod
    def lc_lcp14(nums: List[int]) -> int:
        #  1 到 n 的数所有的质因子并动态规划counter
        nt = PrimeFactor(max(nums))
        ind = dict()
        n = len(nums)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i, num in enumerate(nums):
            while num > 1:
                p = nt.min_prime[num]
                while num % p == 0:
                    num //= p
                if p not in ind or dp[i] < dp[ind[p]]:
                    ind[p] = i
                if dp[ind[p]] + 1 < dp[i + 1]:
                    dp[i + 1] = dp[ind[p]] + 1
                if dp[i] + 1 < dp[i + 1]:
                    dp[i + 1] = dp[i] + 1
        return dp[-1] if dp[-1] < inf else -1

    @staticmethod
    def cf_1176d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1176/problem/D
        tag: construction|greedy|implemention
        """
        primes = PrimeSieve().eratosthenes_sieve(2750131)
        ind = {num: i + 1 for i, num in enumerate(primes)}
        m = 2 * 10 ** 5
        max_factor = [0] * (m + 1)
        for i in range(2, m + 1):
            for j in range(2 * i, m + 1, i):
                max_factor[j] = i
        cnt = [0] * (m + 1)
        ac.read_int()
        nums = ac.read_list_ints()
        nums.sort(reverse=True)
        for num in nums:
            if num <= m:
                cnt[num] += 1
        ans = []
        for num in nums:
            if num <= m and not cnt[num]:
                continue
            if num in ind:
                if num <= m:
                    cnt[num] -= 1
                ans.append(ind[num])
                cnt[ind[num]] -= 1
            else:
                ans.append(num)
                if num <= m:
                    cnt[num] -= 1
                cnt[max_factor[num]] -= 1
        ac.lst(ans)
        return

    @staticmethod
    def cf_1349a(ac=FastIO()):
        # prime_factorization|，brute_force最终结果当中质因子的幂次
        n = ac.read_int()
        nums = ac.read_list_ints()
        nmp = PrimeFactor(max(nums))
        dct = defaultdict(list)

        for num in nums:
            for p, c in nmp.prime_factor[num]:
                dct[p].append(c)

        ans = 1
        for p in dct:
            if len(dct[p]) >= n - 1:
                dct[p].sort()
                ans *= p ** dct[p][-n + 1]
        ac.st(ans)
        return

    @staticmethod
    def cf_1458a(ac=FastIO()):
        # gcdmath|求解gcd(x,y)=gcd(x-y,y)
        m, n = ac.read_list_ints()
        a = ac.read_list_ints()
        b = ac.read_list_ints()
        g = 0
        # 推广到n维
        for i in range(1, m):
            g = math.gcd(g, a[i] - a[i - 1])
        ans = [math.gcd(g, a[0] + num) for num in b]
        ac.lst(ans)
        return

    @staticmethod
    def abc_114d(ac=FastIO()):
        # prime_factorization|counter
        n = ac.read_int()
        nt = PrimeFactor(n + 10)
        cnt = Counter()
        for x in range(1, n + 1):
            for p, c in nt.prime_factor[x]:
                cnt[p] += c
        ans = set()
        for item in permutations(list(cnt.keys()), 3):
            x, y, z = item
            if cnt[x] >= 2 and cnt[y] >= 4 and cnt[z] >= 4:
                if y > z:
                    y, z = z, y
                ans.add((x, y, z))

        for item in permutations(list(cnt.keys()), 2):
            x, y = item
            if cnt[x] >= 2 and cnt[y] >= 24:
                ans.add((x, y, 325))
            if cnt[x] >= 4 and cnt[y] >= 14:
                ans.add((x, y, 515))
        for x in cnt:
            if cnt[x] >= 74:
                ans.add(x)
        ac.st(len(ans))
        return

    @staticmethod
    def ac_124(ac=FastIO()):
        # 不同进制之间的转换
        st = "0123456789"
        for i in range(26):
            st += chr(i + ord("A"))
        for i in range(26):
            st += chr(i + ord("a"))
        ind = {w: i for i, w in enumerate(st)}
        for _ in range(ac.read_int()):
            a, b, word = ac.read_list_strs()
            a = int(a)
            b = int(b)
            num = 0
            for w in word:
                num *= a
                num += ind[w]
            ac.lst([a, word])
            ans = ""
            while num:
                ans += st[num % b]
                num //= b
            if not ans:
                ans = "0"
            ac.lst([b, ans[::-1]])
            ac.st("")
        return

    @staticmethod
    def ac_197(ac=FastIO()):
        # n!阶乘的prime_factorization|即因子与因子的个数
        ceil = ac.read_int()
        min_prime = [0] * (ceil + 1)
        #  1 到 ceil 所有数字的最小质数因子
        for i in range(2, ceil + 1):
            if not min_prime[i]:
                min_prime[i] = i
                for j in range(i * i, ceil + 1, i):
                    min_prime[j] = i

        #  1 到 ceil 所有数字的prime_factorization|结果
        dct = defaultdict(int)
        for num in range(2, ceil + 1):
            while num > 1:
                p = min_prime[num]
                cnt = 0
                while num % p == 0:
                    num //= p
                    cnt += 1
                dct[p] += cnt
        for p in sorted(dct):
            ac.lst([p, dct[p]])
        return

    @staticmethod
    def ac_199(ac=FastIO()):
        #  sum(k%i for i in range(n))
        n, k = ac.read_list_ints()
        ans = n * k
        left = 1
        while left <= min(n, k):
            right = min(k // (k // left), n)
            ans -= (k // left) * (left + right) * (right - left + 1) // 2
            left = right + 1
        ac.st(ans)
        return

    @staticmethod
    def lc_p2429(ac=FastIO()):
        # brute_force质因数组合|inclusion_exclusioncounter
        n, m = ac.read_list_ints()
        primes = sorted(ac.read_list_ints())

        def dfs(i):
            nonlocal ans, value, cnt
            if value > m:
                return
            if i == n:
                if cnt:
                    num = m // value
                    ans += value * (num * (num + 1) // 2) * (-1) ** (cnt + 1)
                    ans %= mod
                return

            value *= primes[i]
            cnt += 1
            dfs(i + 1)
            cnt -= 1
            value //= primes[i]
            dfs(i + 1)
            return

        cnt = ans = 0
        value = 1
        mod = 376544743
        dfs(0)
        ac.st(ans)
        return

    @staticmethod
    def lg_p2527(ac=FastIO()):
        # 丑数即只含特定质因子的数
        n, k = ac.read_list_ints()
        primes = ac.read_list_ints()
        dp = [1] * (k + 1)
        pointer = [0] * n
        for i in range(k):
            num = min(dp[pointer[i]] * primes[i] for i in range(n))
            for x in range(n):
                if dp[pointer[x]] * primes[x] == num:
                    pointer[x] += 1
            dp[i + 1] = num
        ac.st(dp[-1])
        return

    @staticmethod
    def lg_p5248(ac=FastIO()):
        # 进制题目
        m, fm = ac.read_list_ints()
        lst = []
        while fm:
            lst.append(fm % m)
            fm //= m
        ac.st(len(lst))
        ac.lst(lst)
        return

    @staticmethod
    def lg_p7960(ac=FastIO()):
        # 类似prime_sieve的思路preprocess
        n = 10 ** 7
        dp = [0] * (n + 1)
        for x in range(1, n + 1):
            if "7" in str(x):
                y = 1
                while x * y <= n:
                    dp[x * y] = 1
                    y += 1
        post = 10 ** 7 + 1
        for i in range(n, -1, -1):
            if dp[i] == 1:
                dp[i] = -1
            else:
                dp[i] = post
                post = i

        for _ in range(ac.read_int()):
            ac.st(dp[ac.read_int()])
        return

    @staticmethod
    def lg_p8319(ac=FastIO()):
        # prime_factorization|greedy
        n = 2 * 10 ** 6
        f = [1] * (n + 1)
        prime = [0] * (n + 1)
        for x in range(2, n + 1):
            if not prime[x]:
                # 当前值作为质因子的花费次数
                t = 1
                while t * x <= n:
                    c = 1
                    xx = t
                    while xx % x == 0:
                        xx //= x
                        c += 1
                    f[t * x] += (x - 1) * c
                    prime[t * x] = 1
                    t += 1

        # 前缀最大值处理
        for i in range(1, n + 1):
            f[i] = ac.max(f[i - 1], f[i])
        for _ in range(ac.read_int()):
            ac.st(f[ac.read_int()])
        return

    @staticmethod
    def lg_p8646(ac=FastIO()):
        # peishu_theorem|与背包 DP
        n = ac.read_int()
        nums = [ac.read_int() for _ in range(n)]
        s = 10000
        dp = [0] * (s + 1)
        dp[0] = 1
        for num in nums:
            for i in range(num, s + 1):
                if dp[i - num]:
                    dp[i] = 1
        ans = s + 1 - sum(dp)
        if reduce(math.gcd, nums) != 1:
            ac.st("INF")
        else:
            ac.st(ans)
        return

    @staticmethod
    def cf_1900d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1900/problem/D
        tag: inclusion_exclusion|gcd_pair|counter|classical
        """
        ceil = 10 ** 5 + 1
        for _ in range(ac.read_int()):
            n = ac.read_int()
            nums = ac.read_list_ints()
            nums.sort()
            cnt = [0] * ceil
            last = [-1] * ceil
            for i, num in enumerate(nums):
                cnt[num] += 1
                last[num] = i

            gcd = [0] * ceil
            for g in range(1, ceil):
                small = 0
                for mid in range(g, ceil, g):
                    if not cnt[mid]:
                        continue
                    cur = cnt[mid]
                    cur2 = cur * (cur - 1) // 2
                    cur3 = cur * (cur - 1) * (cur - 2) // 6
                    bigger = n - last[mid] - 1
                    gcd[g] += small * bigger * cur + small * cur2 + bigger * cur2 + cur3
                    small += cur

            for g in range(ceil - 1, 0, -1):
                for gg in range(2 * g, ceil, g):
                    gcd[g] -= gcd[gg]
            ac.st(sum(gcd[i] * i for i in range(ceil)))
        return

    @staticmethod
    def lc_1390(nums: List[int]) -> int:
        # preprocess所有数的所有因子
        nt = PrimeFactor(10 ** 5)
        ans = 0
        for num in nums:
            if len(nt.all_factor[num]) == 4:
                ans += sum(nt.all_factor[num])
        return ans

    @staticmethod
    def lc_1819(nums: List[int]) -> int:
        # preprocess所有整数的所有因子，再brute_forcegcd
        nt = PrimeFactor(2 * 10 ** 5 + 10)
        dct = defaultdict(list)
        for num in set(nums):
            for x in nt.all_factor[num]:
                dct[x].append(num)
        ans = 0
        for num in dct:
            if reduce(math.gcd, dct[num]) == num:
                ans += 1
        return ans

    @staticmethod
    def cf_1884d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1884/problem/D
        tag: factor_dp|gcd_pair|counter|classical
        """
        for _ in range(ac.read_int()):
            n = ac.read_int()
            nums = ac.read_list_ints()
            cnt = [0] * (n + 1)
            dp = [0] * (n + 1)
            for num in nums:
                cnt[num] += 1
            for num in range(n, 0, -1):
                tot = post = 0
                y = 1
                while num * y <= n:
                    post += dp[num * y]
                    tot += cnt[num * y]
                    y += 1
                dp[num] = tot * (tot - 1) // 2 - post
            for num in range(1, n + 1):
                if cnt[num]:
                    for x in range(num, n + 1, num):
                        dp[x] = 0
            ac.st(sum(dp))
        return

    @staticmethod
    def ac_3727(ac=FastIO()):
        # brain_teaser转换成进制表达问题

        for _ in range(ac.read_int()):
            def check():
                n, k = ac.read_list_ints()
                cnt = Counter()
                for num in ac.read_list_ints():
                    lst = []
                    while num:
                        lst.append(num % k)
                        num //= k
                    for i, va in enumerate(lst):
                        cnt[i] += va
                        if cnt[i] > 1:
                            ac.no()
                            return
                ac.yes()
                return

            check()

        return

    @staticmethod
    def ac_4319(ac=FastIO()):
        # prime_factorization|后prefix_hashcounter
        n, k = ac.read_list_ints()
        a = ac.read_list_ints()
        nt = PrimeFactor(max(a))
        pre = defaultdict(int)
        ans = 0
        for num in a:
            cur = []
            lst = []
            for p, c in nt.prime_factor[num]:
                c %= k
                if c:
                    cur.append((p, c))
                    lst.append((p, k - c))
            ans += pre[tuple(lst)]
            pre[tuple(cur)] += 1
        ac.st(ans)
        return

    @staticmethod
    def ac_4484(ac=FastIO()):
        # 分数在某个进制下是否为有限小数问题
        for _ in range(ac.read_int()):

            def check():
                nonlocal q
                while q > 1:
                    gg = math.gcd(q, b)
                    if gg == 1:
                        break
                    q //= gg

                return q == 1

            p, q, b = ac.read_list_ints()
            g = math.gcd(p, q)
            p //= g
            q //= g

            ac.st("YES" if check() else "NO")
        return

    @staticmethod
    def ac_5049(ac=FastIO()):
        # prime_factorization|组合数
        n, m, h = ac.read_list_ints()
        a = ac.read_list_ints()
        h -= 1
        s = sum(a)
        if s < n:
            ac.st(-1)
            return
        if s - a[h] < n - 1:
            ac.st(1)
            return
        nt = PrimeFactor(s)
        total = nt.comb(s - 1, n - 1)
        part = nt.comb(s - a[h], n - 1)
        ac.st(1 - part / total)
        return

    @staticmethod
    def cf_1978e(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1978/problem/F
        tag: union_find|matrix|math|brain_teaser
        """
        pf = PrimeFactor(10 ** 6)

        for _ in range(ac.read_int()):
            n, k = ac.read_list_ints()
            nums = ac.read_list_ints()
            dct = dict()
            uf = UnionFind(2 * n - 1)
            for i in range(1, 2 * n):
                num = nums[i % n]
                for p, _ in pf.prime_factor[num]:
                    if p in dct and i - dct[p] <= k and p > 1:
                        uf.union(dct[p] - 1, i - 1)
                    dct[p] = i
            ans = uf.part
            for i in range(n):
                if nums[i] == 1:
                    ans += n - 2 if i else n - 1
            ac.st(ans)
        return

    @staticmethod
    def cf_1627d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1627/problem/D
        tag: euler_series|prime_factor|all_factor|implemention|brute_force
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        ceil = max(nums)
        cnt = [0] * (ceil + 1)
        for num in nums:
            cnt[num] = 1
        ans = 0
        for i in range(ceil, 0, -1):
            if cnt[i]:
                continue
            g = 0
            for j in range(i * 2, ceil + 1, i):
                if cnt[j]:
                    if g == 0:
                        g = j
                    elif math.gcd(g, j) == i:
                        cnt[i] = 1
                        ans += 1
                        break
        ac.st(ans)
        return

    @staticmethod
    def cf_1499d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1499/problem/D
        tag: math|prime_factor_cnt|classical
        """
        n = 2 * 10 ** 7
        min_prime = [0] * (n + 1)
        min_prime[1] = 1
        prime_factor_cnt = [0] * (n + 1)
        for i in range(2, n + 1):
            if not min_prime[i]:
                min_prime[i] = i
                for j in range(i * i, n + 1, i):
                    if not min_prime[j]:
                        min_prime[j] = i
            pre = i // min_prime[i]
            prime_factor_cnt[i] = prime_factor_cnt[pre] + int(min_prime[i] != min_prime[pre])

        def check(g):
            if (x // g + d) % c:
                return 0
            return p[prime_factor_cnt[(x // g + d) // c]]

        p = [1<< x for x in range(32)]
        res = []
        for _ in range(ac.read_int()):
            c, d, x = ac.read_list_ints()
            ans = 0
            for w in range(1, x + 1):
                if w * w > x:
                    break
                if x % w == 0:
                    ans += check(w)
                    if x // w > w:
                        ans += check(x // w)
            res.append(ans)
        for a in res:
            ac.st(a)
        return