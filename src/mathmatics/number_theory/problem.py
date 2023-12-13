"""
Algorithm：number_theory|euler_sieve|linear_sieve|prime|euler_phi|factorization|prime_factorization|base
Description：digital_dp|n-base|prime_factorization|factorization|linear_sieve|euler_phi|pollard_rho|meissel_lehmer|range_prime_count

====================================LeetCode====================================
264（https://leetcode.cn/problems/ugly-number-ii/）pointer|dp|ugly_number|classical
1201（https://leetcode.cn/problems/ugly-number-iii/）ugly_number
313（https://leetcode.cn/problems/super-ugly-number/）ugly_number
12（https://leetcode.cn/problems/integer-to-roman/）integer_to_roman
13（https://leetcode.cn/problems/roman-to-integer/）roman_to_integer
6364（https://leetcode.cn/problems/count-the-number-of-square-free-subsets/）ag_dp|counter
1994（https://leetcode.cn/problems/the-number-of-good-subsets/）bag_dp|counter
6309（https://leetcode.cn/problems/split-the-array-to-make-coprime-products/）prime_factorization|counter
2464（https://leetcode.cn/problems/minimum-subarrays-in-a-valid-split/）prime_factorization|counter|dp
LCP 14（https://leetcode.cn/problems/qie-fen-shu-zu/）prime_factorization|counter|dp
279（https://leetcode.cn/problems/perfect-squares/）four_square
650（https://leetcode.cn/problems/2-keys-keyboard/）prime_factorization
1390（https://leetcode.cn/problems/four-divisors/）preprocess|factorization
1819（https://leetcode.cn/problems/number-of-different-subsequences-gcds/）preprocess|factorization|brute_force|gcd
1017（https://leetcode.cn/problems/convert-to-base-2/）negative_base|classical
1073（https://leetcode.cn/problems/adding-two-negabinary-numbers/）negative_base|classical
8041（https://leetcode.cn/problems/maximum-element-sum-of-a-complete-subset-of-indices/description/）prime_factorization|hash|classical|odd

=====================================LuoGu======================================
P1865（https://www.luogu.com.cn/problem/P1865）linear_sieve|prime|binary_search|range_prime_count
P1748（https://www.luogu.com.cn/problem/P1748）heapq|implemention|pointer|inclusion_exclusion|binary_search
P2723（https://www.luogu.com.cn/problem/P2723）ugly_number
P1952（https://www.luogu.com.cn/problem/P1952）n-base
P1555（https://www.luogu.com.cn/problem/P1555）2-base|3-base
P1465（https://www.luogu.com.cn/problem/P1465）int_to_roman
P1112（https://www.luogu.com.cn/problem/P1112）brute_force
P2926（https://www.luogu.com.cn/problem/P2926）prime_factorization|counter
P5535（https://www.luogu.com.cn/problem/P5535）prime|is_prime5|greedy|brain_teaser
P1876（https://www.luogu.com.cn/problem/P1876）odd_even|factorization|classical
P1887（https://www.luogu.com.cn/problem/P1887）classical|maximum_mul
P2043（https://www.luogu.com.cn/problem/P2043）prime_factorization|prime_sieve|factorial
P2192（https://www.luogu.com.cn/problem/P2192）divide|property|classical
P7191（https://www.luogu.com.cn/problem/P7191）mod|math|factorization
P7517（https://www.luogu.com.cn/problem/P7517）prime_sieve|brute_force|factorization|counter
P7588（https://www.luogu.com.cn/problem/P7588）prime|brute_force|is_prime4
P7696（https://www.luogu.com.cn/problem/P7696）prime_factorization
P4718（https://www.luogu.com.cn/problem/P4718）pollard_rho|prime_factorization|prime
P2429（https://www.luogu.com.cn/problem/P2429）brute_force|prime_factorization|inclusion_exclusion|counter
P1069（https://www.luogu.com.cn/problem/P1069）prime_factorization|counter
P1072（https://www.luogu.com.cn/problem/P1072）brute_force|factorization
P1593（https://www.luogu.com.cn/problem/P1593）prime_factorization|fast_power|classical
P2527（https://www.luogu.com.cn/problem/P2527）ugly_number
P2557（https://www.luogu.com.cn/problem/P2557）prime_factorization|math
P4446（https://www.luogu.com.cn/problem/P4446）is_prime
P4752（https://www.luogu.com.cn/problem/P4752）is_prime
P5248（https://www.luogu.com.cn/problem/P5248）base
P5253（https://www.luogu.com.cn/problem/P5253）math
P7960（https://www.luogu.com.cn/problem/P7960）prime_sieve|preprocess
P8319（https://www.luogu.com.cn/problem/P8319）prime_factorization|counter
P8646（https://www.luogu.com.cn/problem/P8646）peishu_theorem|bag_dp
P8762（https://www.luogu.com.cn/problem/P8762）inclusion_exclusion|prefix_sum|counter
P8778（https://www.luogu.com.cn/problem/P8778）brute_force|prime_factorization|O(n^0.25)|classical
P8782（https://www.luogu.com.cn/problem/P8782）base|greedy|classical

===================================CodeForces===================================
1771C（https://codeforces.com/problemset/problem/1771/C）pollard_rho|prime_factorization
1034A（https://codeforces.com/problemset/problem/1034/A）prime_factorization
1366D（https://codeforces.com/problemset/problem/1366/D）min_prime|construction
1349A（https://codeforces.com/contest/1349/problem/A）prime_factorization|brute_force
1295D（https://codeforces.com/problemset/problem/1295/D）euler_phi|n_coprime
1538D（https://codeforces.com/problemset/problem/1538/D）pollard_rho|prime_factorization
1458A（https://codeforces.com/problemset/problem/1458/A）gcd|math
1444A（https://codeforces.com/problemset/problem/1444/A）greedy|brute_force|prime_factorization
1823C（https://codeforces.com/contest/1823/problem/C）prime_factorization|greedy
1744E2（https://codeforces.com/contest/1744/problem/E2）brute_force|factorization
1612D（https://codeforces.com/contest/1612/problem/D）gcd_like

====================================AtCoder=====================================
ABC114D（https://atcoder.jp/contests/abc114/tasks/abc114_d）prime_factorization|counter
ABC134D（https://atcoder.jp/contests/abc134/tasks/abc134_d）reverse_thinking|construction

=====================================AcWing=====================================
97（https://www.acwing.com/problem/content/99/）a^b|math|factorization
124（https://www.acwing.com/problem/content/126/）base
197（https://www.acwing.com/problem/content/199/）factorial|prime_factorization
196（https://www.acwing.com/problem/content/198/）counter
198（https://www.acwing.com/problem/content/200/）anti_prime_number
199（https://www.acwing.com/problem/content/description/201/）brute_force
3727（https://www.acwing.com/solution/content/54479/）brain_teaser|base
3999（https://www.acwing.com/problem/content/description/4002/）CF1295D
4319（https://www.acwing.com/problem/content/4322/）prime_factorization|prefix_hash|counter
4484（https://www.acwing.com/problem/content/4487/）base
4486（https://www.acwing.com/problem/content/description/4489/）prime_factorization|greedy
4622（https://www.acwing.com/problem/content/description/4625/）brain_teaser|greedy|construction
5049（https://www.acwing.com/problem/content/description/5052/）prime_factorization|comb


"""
import math
from collections import Counter
from collections import defaultdict
from functools import reduce
from math import inf
from operator import mul
from typing import List

from src.mathmatics.number_theory.template import NumberTheory
from src.utils.fast_io import FastIO


class Solution:
    def __init__(self):
        return

    @staticmethod
    def cf_1034a(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1034/A
        tag: prime_factorization
        """

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
        """
        url: https://codeforces.com/problemset/problem/1366/D
        tag: min_prime|construction
        """
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
    def lc_6309(nums: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/split-the-array-to-make-coprime-products/
        tag: prime_factorization|counter
        """
        #  1 到 n 的数所有的质因子并差分确定作用范围
        prime = NumberTheory().get_num_prime_factor(10 ** 6)
        n = len(nums)
        dct = defaultdict(list)
        for i, num in enumerate(nums):
            for p in prime[num]:
                dct[p].append(i)

        # 确定action_scope
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
    def cf_1295d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1295/D
        tag: euler_phi|n_coprime
        """
        # euler_phi求解
        for _ in range(ac.read_int()):
            a, m = ac.read_list_ints()
            g = math.gcd(a, m)
            mm = m // g
            ans = NumberTheory().euler_phi(mm)
            ac.st(ans)
        return

    @staticmethod
    def cf_1458a(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1458/A
        tag: gcd|math
        """
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
    def main(ac=FastIO()):
        # 预先brute_force质因子，再prime_factorization|
        primes = NumberTheory().euler_flag_prime((4 * 10 ** 3))
        for _ in range(ac.read_int()):
            ac.read_int()
            nums = ac.read_list_ints()
            cnt = defaultdict(int)
            for num in nums:
                for x in primes:
                    if x > num:
                        break
                    y = 0
                    while num % x == 0:
                        num //= x
                        y += 1
                    if y:
                        cnt[x] += y
                if num != 1:
                    cnt[num] += 1
            lst = list(cnt.values())
            even = sum(x // 2 for x in lst)
            odd = sum(x % 2 for x in lst)
            ans = odd // 3
            odd %= 3
            if odd:
                if ans or even:
                    ac.st(ans + even)
                else:
                    ac.st(0)
            else:
                ac.st(ans + even)
        return

    @staticmethod
    def ac_97_1(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/99/
        tag: a^b|math|factorization
        """
        # a^b的所有约数之和
        a, b = ac.read_list_ints()
        lst = NumberTheory().get_prime_factor(a)
        mod = 9901
        ans = 1
        for p, c in lst:
            ans *= (pow(p, b * c + 1, mod) - 1) * pow(p - 1, -1, mod)
            ans %= mod
        ac.st(ans)
        return

    @staticmethod
    def ac_97_2(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/99/
        tag: a^b|math|factorization
        """

        # a^b的所有约数之和

        def check(pp, cc):

            # 等比数列求和recursiondivide_and_conquer
            if cc == 0:
                return 1
            if cc % 2 == 1:
                return (1 + pow(pp, (cc + 1) // 2, mod)) * check(pp, (cc - 1) // 2)
            return (1 + pow(pp, (cc + 0) // 2, mod)) * check(pp, (cc - 1) // 2) + pow(pp, cc, mod)

        a, b = ac.read_list_ints()
        if a == 0:
            ac.st(0)
            return
        lst = NumberTheory().get_prime_factor(a)
        mod = 9901
        ans = 1
        for p, c in lst:
            ans *= check(p, c * b)
            ans %= mod
        ac.st(ans)
        return

    @staticmethod
    def ac_124(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/126/
        tag: base
        """
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
        """
        url: https://www.acwing.com/problem/content/199/
        tag: factorial|prime_factorization
        """
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
    def ac_196(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/198/
        tag: counter
        """

        # 质数距离对
        primes = NumberTheory().sieve_of_eratosthenes(2 ** 16)
        while True:
            lst = ac.read_list_ints()
            if not lst:
                break

            left, right = lst
            dp = [0] * (right - left + 1)
            for p in primes:
                x = max(math.ceil(left / p), 2) * p
                while left <= x <= right:
                    dp[x - left] = 1
                    x += p

            rest = [x + left for x in range(right - left + 1) if not dp[x] and x + left > 1]
            if len(rest) < 2:
                ac.st("There are no adjacent primes.")
            else:
                ans1 = [rest[0], rest[1]]
                ans2 = [rest[0], rest[1]]
                m = len(rest)
                for i in range(2, m):
                    a, b = rest[i - 1], rest[i]
                    if b - a < ans1[1] - ans1[0]:
                        ans1 = [a, b]
                    if b - a > ans2[1] - ans2[0]:
                        ans2 = [a, b]
                ac.st(f"{ans1[0]},{ans1[1]} are closest, {ans2[0]},{ans2[1]} are most distant.")
        return

    @staticmethod
    def ac_198(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/200/
        tag: anti_prime_number
        """

        # 最大的反质数（反prime，即约数或者说因数个数大于任何小于它的数的因数个数）
        n = ac.read_int()
        primes = NumberTheory().sieve_of_eratosthenes(50)
        x = reduce(mul, primes)
        while x > n:
            x //= primes.pop()
        # 充要条件为 2^c1*3^c2...且c1>=c2
        m = len(primes)
        ans = [1, 1]
        stack = [[1, 1, int(math.log2(n)) + 1, 0]]
        while stack:
            x, cnt, mi, i = stack.pop()
            if mi == 0 or i == m:
                if cnt > ans[1] or (cnt == ans[1] and x < ans[0]):
                    ans = [x, cnt]
                continue
            for y in range(mi, -1, -1):
                if x * primes[i] ** y <= n:
                    stack.append([x * primes[i] ** y, cnt * (y + 1), y, i + 1])
        ac.st(ans[0])
        return

    @staticmethod
    def ac_199(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/description/201/
        tag: brute_force
        """
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
    def lg_p1069(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1069
        tag: prime_factorization|counter
        """
        # prime_factorization|，greedy匹配implemention
        ac.read_int()
        m1, m2 = ac.read_list_ints()
        lst = NumberTheory().get_prime_factor(m1)
        ans = inf
        for num in ac.read_list_ints():
            res = 0
            for p, c in lst:
                if num % p != 0:
                    break
                tmp = num
                x = 0
                while tmp % p == 0:
                    tmp //= p
                    x += 1
                res = ac.max(res, math.ceil(c * m2 / x))
            else:
                ans = ac.min(ans, res)
        ac.st(ans if ans < inf else -1)
        return

    @staticmethod
    def lg_p1072(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1072
        tag: brute_force|factorization
        """
        # brute_force所有因数
        nt = NumberTheory()
        for _ in range(ac.read_int()):
            a0, a1, b0, b1 = ac.read_list_ints()
            factor = [num for num in nt.get_all_factor(b1)
                      if num % a1 == 0 and math.gcd(num, a0) == a1
                      and b0 * num // math.gcd(num, b0) == b1]
            ac.st(len(factor))
        return

    @staticmethod
    def lg_p1593(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1593
        tag: prime_factorization|fast_power|classical
        """
        # prime_factorization|与fast_power|a^b的所有因子之和
        mod = 9901
        a, b = ac.read_list_ints()
        if a == 1 or b == 0:
            ac.st(1)
        else:
            # prime_factorization
            cnt = dict()
            for p, c in NumberTheory().get_prime_factor(a):
                cnt[p] = c
            # (1+p1+p1^2+...+p1^cb)*...
            ans = 1
            for k in cnt:
                c = cnt[k] * b
                if (k - 1) % mod:  # 即 k % mod ！= 1 此时才有逆元
                    # 等比数列multiplicative_reverse，逆元要求与modcoprime否则需要额外
                    ans *= (pow(k, c + 1, mod) - 1) * pow(k - 1, -1, mod)
                    ans %= mod
                else:
                    # 此时无multiplicative_reverse
                    ans *= (c + 1)
                    ans %= mod
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
        """
        url: https://www.luogu.com.cn/problem/P2527
        tag: ugly_number
        """
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
    def lg_p2557(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2557
        tag: prime_factorization|math
        """
        # 利用prime_factorization|与等比数列因子之和
        a, b = ac.read_list_ints()
        if a == 1 or b == 0:
            ac.st(1)
        else:
            # prime_factorization
            cnt = dict()
            for p, c in NumberTheory().get_prime_factor(a):
                cnt[p] = c
            # (1+p1+p1^2+...+p1^cb)*...
            ans = 1
            for k in cnt:
                c = cnt[k] * b
                ans *= (k ** (c + 1) - 1) // (k - 1)
            ac.st(ans)
        return

    @staticmethod
    def lg_p4446(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4446
        tag: is_prime
        """
        # 预先处理出prime然后最大的完全立方数因子
        prime = NumberTheory().sieve_of_eratosthenes(int(10 ** (18 / 4)) + 1)
        ac.read_int()
        for num in ac.read_list_ints():
            ans = 1
            for p in prime:
                if p > num:
                    break
                c = 0
                while num % p == 0:
                    c += 1
                    num //= p
                ans *= p ** (c // 3)

            # binary_search判断数字是否为完全立方数
            low = 1
            high = int(num ** (1 / 3)) + 1
            while low < high - 1:
                mid = low + (high - low) // 2
                if mid ** 3 <= num:
                    low = mid
                else:
                    high = mid
            if high ** 3 == num:
                ans *= high
            elif low ** 3 == num:
                ans *= low
            ac.st(ans)
        return

    @staticmethod
    def lg_p4752(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4752
        tag: is_prime
        """
        # 判断除数是否为质数
        nt = NumberTheory()
        for _ in range(ac.read_int()):
            ac.read_list_ints()
            cnt = Counter(sorted(ac.read_list_ints()))
            if cnt[0]:
                ac.st("NO")
                continue
            for num in ac.read_list_ints():
                cnt[num] -= 1

            rest = []
            for num in cnt:
                if cnt[num] and num != 1:
                    rest.append([num, cnt[num]])
            if len(rest) >= 2:
                ac.st("NO")
            elif len(rest) == 1:
                if rest[0][1] > 1:
                    ac.st("NO")
                else:
                    if nt.is_prime4(rest[0][0]):
                        ac.st("YES")
                    else:
                        ac.st("NO")
            else:
                ac.st("NO")
        return

    @staticmethod
    def lg_p5248(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P5248
        tag: base
        """
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
    def lg_p5253(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P5253
        tag: math
        """
        # 方程变换 (x-n)*(y-n)=n^2 的对数
        n = ac.read_int()
        lst = NumberTheory().get_prime_factor(n)
        ans = 1
        for _, c in lst:
            # 转换为求数字的因数个数
            ans *= (2 * c + 1)
        ac.st((ans + 1) // 2)
        return

    @staticmethod
    def lg_p7960(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P7960
        tag: prime_sieve|preprocess
        """
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
        """
        url: https://www.luogu.com.cn/problem/P8319
        tag: prime_factorization|counter
        """
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
        """
        url: https://www.luogu.com.cn/problem/P8646
        tag: peishu_theorem|bag_dp
        """
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
    def lg_8778(ac=FastIO()):
        # brute_force素因子后O(n^0.25)是否为完全平方数与立方数
        primes = NumberTheory().sieve_of_eratosthenes(4000)

        def check(xx):
            for r in range(2, 6):
                a = int(xx ** (1 / r))
                for ww in [a - 1, a, a + 1, a + 2]:
                    if ww ** r == xx:
                        return True
            return False

        n = ac.read_int()
        for _ in range(n):
            num = ac.read_int()
            flag = True
            for p in primes:
                if p > num:
                    break
                x = 0
                while num % p == 0:
                    x += 1
                    num //= p
                if x == 1:
                    flag = False
                    break
            if flag and check(num):
                ac.st("yes")
            else:
                ac.st("no")
        return

    @staticmethod
    def lc_1073(arr1: List[int], arr2: List[int]) -> List[int]:
        """
        url: https://leetcode.cn/problems/adding-two-negabinary-numbers/
        tag: negative_base|classical
        """

        # 负进制题
        def check(tmp):
            res = 0
            for num in tmp:
                res = (-2) * res + num
            return res

        ans = check(arr1) + check(arr2)
        return NumberTheory().get_k_bin_of_n(ans, -2)

    @staticmethod
    def ac_3727(ac=FastIO()):
        """
        url: https://www.acwing.com/solution/content/54479/
        tag: brain_teaser|base
        """
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
                            ac.st("NO")
                            return
                ac.st("YES")
                return

            check()

        return

    @staticmethod
    def ac_4484(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/4487/
        tag: base
        """
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
    def ac_4486(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/description/4489/
        tag: prime_factorization|greedy
        """
        # prime_factorization|greedy题
        n = ac.read_int()
        if n == 1:
            ac.lst([1, 0])
            return

        res = NumberTheory().get_prime_factor(n)

        ans = 1
        x = 0
        ind = [2 ** i for i in range(32)]
        lst = []
        for p, c in res:
            ans *= p
            for i in range(32):
                if ind[i] >= c:
                    if ind[i] > c:
                        x = 1
                    lst.append(i)
                    break
        cnt = max(w for w in lst)
        if any(w < cnt for w in lst) or x:
            cnt += 1
        ac.lst([ans, cnt])
        return

    @staticmethod
    def ac_4622(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/description/4625/
        tag: brain_teaser|greedy|construction
        """
        # brain_teaser|greedyconstruction
        n = ac.read_int()
        if n < 4:
            ac.st(1)
        elif n % 2 == 0:
            ac.st(2)
        else:
            if NumberTheory().is_prime4(n - 2):
                ac.st(2)
            else:
                ac.st(3)

        return

    @staticmethod
    def cf_1612d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1612/problem/D
        tag: gcd_like
        """
        for _ in range(ac.read_int()):
            a, b, x = ac.read_list_ints()
            while True:
                if a < b:
                    a, b = b, a
                if x == a or x == b:
                    ac.st("YES")
                    break
                if x > a or b == 0:
                    ac.st("NO")
                    break
                if (a - x) % b == 0:
                    ac.st("YES")
                    break
                y = ac.ceil(a, b) - 1
                a -= y * b
                if y == 0:
                    ac.st("NO")
                    break

        return

    @staticmethod
    def cf_1744_e2(ac=FastIO()):
        # 因数brute_force
        for _ in range(ac.read_int()):
            a, b, c, d = ac.read_list_ints()
            lst_a = NumberTheory().get_all_factor(a)
            lst_b = NumberTheory().get_all_factor(b)

            def check():
                for x in lst_a:
                    for y in lst_b:
                        g = x * y
                        yy = a * b // g
                        low_1 = a // g + 1
                        high_1 = c // g

                        low_2 = b // yy + 1
                        high_2 = d // yy
                        if low_2 <= high_2 and low_1 <= high_1:
                            ac.lst([low_1 * g, low_2 * yy])
                            return
                ac.lst([-1, -1])
                return

            check()
        return

    @staticmethod
    def lc_1017(n: int) -> str:
        """
        url: https://leetcode.cn/problems/convert-to-base-2/
        tag: negative_base|classical
        """
        # 负进制转换模板题
        lst = NumberTheory().get_k_bin_of_n(n, -2)
        return "".join(str(x) for x in lst)
