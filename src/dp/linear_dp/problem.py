"""
Algorithm：liner_dp
Description：prefix_suffix|maximum_sub_consequence_sum

====================================LeetCode====================================
940（https://leetcode.cn/problems/distinct-subsequences-ii/）liner_dp|classical|different_subsequence
87（https://leetcode.cn/problems/scramble-string/）liner_dp|memory_search
2361（https://leetcode.cn/problems/minimum-costs-using-the-train-line/）linear_dp
2318（https://leetcode.cn/problems/number-of-distinct-roll-sequences/）linear_dp|brute_force|counter
2263（https://leetcode.cn/problems/make-array-non-decreasing-or-non-increasing/）linear_dp
2209（https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/）linear_dp|prefix_sum
2188（https://leetcode.cn/problems/minimum-time-to-finish-the-race/）preprocess|linear_dp
2167（https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/）prefix_suffix|linear_dp|preprocess|brute_force
2431（https://leetcode.cn/problems/maximize-total-tastiness-of-purchased-fruits/）liner_dp|implemention
2603（https://leetcode.cn/problems/collect-coins-in-a-tree/）liner_dp
2547（https://leetcode.cn/problems/minimum-cost-to-split-an-array/）liner_dp|counter
2638（https://leetcode.cn/problems/count-the-number-of-k-free-subsets/）liner_dp|counter
2597（https://leetcode.cn/problems/the-number-of-beautiful-subsets/）liner_dp|hash
2713（https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/）data_range|liner_dp
1526（https://leetcode.cn/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/）linear_dp|greedy
1553（https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/）brain_teaser|greedy|memory_search|liner_dp
1872（https://leetcode.cn/problems/stone-game-viii/）prefix_sum|reverse_order|linear_dp
1770（https://leetcode.cn/problems/maximum-score-from-performing-multiplication-operations/）liner_dp
823（https://leetcode.cn/problems/binary-trees-with-factors/description/）liner_dp|counter
2746（https://leetcode.cn/problems/decremental-string-concatenation/）hash|liner_dp|implemention
1911（https://leetcode.cn/problems/maximum-alternating-subsequence-sum/）liner_dp
2321（https://leetcode.cn/problems/maximum-score-of-spliced-array/description/）liner_dp|maximum_sub_consequence_sum
2320（https://leetcode.cn/problems/count-number-of-ways-to-place-houses/）liner_dp
1824（https://leetcode.cn/problems/minimum-sideway-jumps/description/）liner_dp|rolling_update
978（https://leetcode.cn/problems/longest-turbulent-subarray/description/）liner_dp|rolling_update
1027（https://leetcode.cn/problems/longest-arithmetic-subsequence/）liner_dp
1987（https://leetcode.cn/problems/number-of-unique-good-subsequences/description/）counter|linear_dp
2355（https://leetcode.cn/problems/maximum-number-of-books-you-can-take/）monotonic_stack|liner_do
2866（https://leetcode.cn/problems/beautiful-towers-ii/）monotonic_stack|liner_dp|prefix_suffix
2327（https://leetcode.cn/problems/number-of-people-aware-of-a-secret/description/）prefix_sum|diff_array|liner_dp
2572（https://leetcode.cn/problems/count-the-number-of-square-free-subsets/description/）liner_dp|counter
2289（https://leetcode.cn/problems/steps-to-make-array-non-decreasing/）liner_dp|counter|monotonic_stack|linked_list|
3041（https://leetcode.com/contest/biweekly-contest-124/problems/maximize-consecutive-elements-in-an-array-after-modification/）linear_dp

=====================================LuoGu======================================
P1970（https://www.luogu.com.cn/problem/P1970）greedy|liner_dp
P1564（https://www.luogu.com.cn/problem/P1564）liner_dp
P1481（https://www.luogu.com.cn/problem/P1481）liner_dp
P2029（https://www.luogu.com.cn/problem/P2029）liner_dp
P2031（https://www.luogu.com.cn/problem/P2031）liner_dp
P2062（https://www.luogu.com.cn/problem/P2062）liner_dp|prefix_max
P2072（https://www.luogu.com.cn/problem/P2072）liner_dp
P2096（https://www.luogu.com.cn/problem/P2096）liner_dp
P5761（https://www.luogu.com.cn/problem/P5761）liner_dp
P2285（https://www.luogu.com.cn/problem/P2285）liner_dp|prefix_max
P2642（https://www.luogu.com.cn/problem/P2642）brute_force|liner_dp
P1470（https://www.luogu.com.cn/problem/P1470）liner_dp
P1096（https://www.luogu.com.cn/problem/P1096）liner_dp
P2896（https://www.luogu.com.cn/problem/P2896）prefix_suffix|linear_dp
P2904（https://www.luogu.com.cn/problem/P2904）prefix_sum|preprocess|liner_dp
P3062（https://www.luogu.com.cn/problem/P3062）liner_dp|brute_force
P3842（https://www.luogu.com.cn/problem/P3842）liner_dp|implemention
P3903（https://www.luogu.com.cn/problem/P3903）liner_dp|brute_force
P5414（https://www.luogu.com.cn/problem/P5414）greedy|liner_dp
P6191（https://www.luogu.com.cn/problem/P6191）liner_dp|brute_force|counter
P6208（https://www.luogu.com.cn/problem/P6208）liner_dp|implemention
P7404（https://www.luogu.com.cn/problem/P7404）linear_dp|brute_force
P7541（https://www.luogu.com.cn/problem/P7541）liner_dp|memory_search|digital_dp
P7767（https://www.luogu.com.cn/problem/P7767）liner_dp
P2246（https://www.luogu.com.cn/problem/P2246）string|counter|liner_dp
P4933（https://www.luogu.com.cn/problem/P4933）liner_dp|counter
P1874（https://www.luogu.com.cn/problem/P1874）liner_dp
P2513（https://www.luogu.com.cn/problem/P2513）prefix_sum|linear_dp
P1280（https://www.luogu.com.cn/problem/P1280）reverse_order|linear_dp
P1282（https://www.luogu.com.cn/problem/P1282）classical|liner_dp|hash
P1356（https://www.luogu.com.cn/problem/P1356）classical|mod|linear_dp
P1385（https://www.luogu.com.cn/problem/P1385）liner_dp|prefix_sum|brain_teaser|lexicographical_order
P1809（https://www.luogu.com.cn/problem/P1809）brain_teaser|liner_dp|greedy
P1868（https://www.luogu.com.cn/problem/P1868）liner_dp|binary_search
P1978（https://www.luogu.com.cn/problem/P1978）liner_dp|mul|inclusion_exclusion
P2432（https://www.luogu.com.cn/problem/P2432）liner_dp|pointer
P2439（https://www.luogu.com.cn/problem/P2439）liner_dp|binary_search
P2476（https://www.luogu.com.cn/problem/P2476）counter|linear_dp|memory_search
P2849（https://www.luogu.com.cn/problem/P2849）matrix_dp
P3448（https://www.luogu.com.cn/problem/P3448）liner_dp|counter
P3558（https://www.luogu.com.cn/problem/P3558）linear_dp|implemention
B3734（https://www.luogu.com.cn/problem/B3734）linear_dp
P3901（https://www.luogu.com.cn/problem/P3901）pointer|linear_dp|pointer
P4401（https://www.luogu.com.cn/problem/P4401）linear_dp
P4933（https://www.luogu.com.cn/problem/P4933）linear_dp|counter
P5095（https://www.luogu.com.cn/problem/P5095）classical|linear_dp
P5810（https://www.luogu.com.cn/problem/P5810）linear_dp
P6040（https://www.luogu.com.cn/problem/P6040）monotonic_queue|linear_dp
P6120（https://www.luogu.com.cn/problem/P6120）linear_dp|implemention
P6146（https://www.luogu.com.cn/problem/P6146）linear_dp|brute_force|counter
P7994（https://www.luogu.com.cn/problem/P7994）linear_dp
P8656（https://www.luogu.com.cn/problem/P8656）linear_dp
P8725（https://www.luogu.com.cn/problem/P8725）classical|matrix_dp|pointer
P8784（https://www.luogu.com.cn/problem/P8784）linear_dp|fast_power
P8786（https://www.luogu.com.cn/problem/P8786）linear_dp|memory_search|implemention
P8816（https://www.luogu.com.cn/problem/P8816）classical|matrix_dp|implemention
P2359（https://www.luogu.com.cn/problem/P2359）linear_dp

===================================CodeForces===================================
75D（https://codeforces.com/problemset/problem/75/D）compress_array|linear_dp
1084C（https://codeforces.com/problemset/problem/1084/C）liner_dp|prefix_sum
166E（https://codeforces.com/problemset/problem/166/E）liner_dp|counter
1221D（https://codeforces.com/problemset/problem/1221/D）liner_dp|implemention
1437C（https://codeforces.com/problemset/problem/1437/C）liner_dp
1525D（https://codeforces.com/problemset/problem/1525/D）liner_dp
1286A（https://codeforces.com/problemset/problem/1286/A）liner_dp
1221D（https://codeforces.com/problemset/problem/1221/D）liner_dp
731E（https://codeforces.com/contest/731/problem/E）prefix_sum|reverse_order|liner_dp
1913D（https://codeforces.com/contest/1913/problem/D）monotonic_stack|linear_dp|prefix_sum
1703G（https://codeforces.com/contest/1703/problem/G）greedy|linear_dp|data_range|limit_operation
1829H（https://codeforces.com/contest/1829/problem/H）counter|linear_dp|classical|bit_operation|data_range
977F（https://codeforces.com/contest/977/problem/F）linear_dp|specific_plan
988F（https://codeforces.com/contest/988/problem/F）linear_dp|brute_force|classical|greedy
988D（https://codeforces.com/contest/988/problem/D）linear_dp|brute_force
999F（https://codeforces.com/contest/999/problem/F）linear_dp|brute_force
1066F（https://codeforces.com/contest/1066/problem/F）linear_dp|brute_force|greedy|sorting
1066D（https://codeforces.com/contest/1066/problem/D）linear_dp|two_pointer
1108D（https://codeforces.com/contest/1108/problem/D）linear_dp|specific_plan
1154F（https://codeforces.com/contest/1154/problem/F）linear_dp|reverse_thinking|brute_force|greedy|implemention|data_range
1176F（https://codeforces.com/contest/1176/problem/F）linear_dp|greedy|implemention
1249E（https://codeforces.com/contest/1249/problem/E）linear_dp|classical|greedy
1256E（https://codeforces.com/contest/1256/problem/E）linear_dp|greedy|brain_teaser
1353E（https://codeforces.com/contest/1353/problem/E）linear_dp|greedy|brute_force
1472F（https://codeforces.com/contest/1472/problem/F）linear_dp|classical
1624E（https://codeforces.com/contest/1624/problem/E）linear_dp|brute_force
1969C（https://codeforces.com/contest/1969/problem/C）linear_dp|data_range|implemention
264C（https://codeforces.com/contest/264/problem/C）linear_dp|classical|maximum_second
1894C2（https://codeforces.com/contest/1984/problem/C2）linear_dp|implemention|greedy

====================================AtCoder=====================================
ABC129E（https://atcoder.jp/contests/abc129/tasks/abc129_e）brain_teaser|digital_dp
ABC322E（https://atcoder.jp/contests/abc322/tasks/abc322_e）linear_dp
ABC318E（https://atcoder.jp/contests/abc318/tasks/abc318_e）linear_dp
ABC315F（https://atcoder.jp/contests/abc315/tasks/abc315_f）linear_dp|brute_force
ABC345E（https://atcoder.jp/contests/abc345/tasks/abc345_e）linear_dp
ABC291F（https://atcoder.jp/contests/abc291/tasks/abc291_f）linear_dp|prefix_suffix
ABC285E（https://atcoder.jp/contests/abc285/tasks/abc285_e）linear_dp|brain_teaser|circular_array|classical
ABC283E（https://atcoder.jp/contests/abc283/tasks/abc283_e）linear_dp
ABC275F（https://atcoder.jp/contests/abc275/tasks/abc275_f）matrix_dp|linear_dp|classical
ABC271D（https://atcoder.jp/contests/abc271/tasks/abc271_d）linear_dp|specific_plan
ABC270D（https://atcoder.jp/contests/abc270/tasks/abc270_d）linear_dp
ABC266D（https://atcoder.jp/contests/abc266/tasks/abc266_d）linear_dp|implemention
ABC267D（https://atcoder.jp/contests/abc267/tasks/abc267_d）linear_dp
ABC248F（https://atcoder.jp/contests/abc248/tasks/abc248_f）connected_graph|linear_dp|classical
ABC244E（https://atcoder.jp/contests/abc244/tasks/abc244_e）implemention|linear_dp
ABC243G（https://atcoder.jp/contests/abc243/tasks/abc243_g）prefix_sum|preprocess|linear_dp|brain_teaser|high_precision|sqrt_sqrt_n|math
ABC350E（https://atcoder.jp/contests/abc350/tasks/abc350_e）linear_dp|implemention|prob_dp|expectation_dp|classical
ABC234G（https://atcoder.jp/contests/abc234/tasks/abc234_g）monotonic_stack|linear_dp|prefix_sum|contribution_method|classical
ABC234F（https://atcoder.jp/contests/abc234/tasks/abc234_f）brute_force|linear_dp|comb|math
ABC224E（https://atcoder.jp/contests/abc224/tasks/abc224_e）reverse_thinking|linear_dp|classical
ABC224E（https://atcoder.jp/contests/abc224/tasks/abc224_f）linear_dp|contribution_method|math
ABC222D（https://atcoder.jp/contests/abc222/tasks/abc222_d）prefix|linear_dp
ABC214F（https://atcoder.jp/contests/abc214/tasks/abc214_f）prefix|linear_dp

=====================================AcWing=====================================
96（https://www.acwing.com/problem/content/98/）liner_dp|classical|hanoi_tower
4414（https://www.acwing.com/problem/content/description/4417/）liner_dp


=====================================LibraryChecker=====================================
1（https://www.51nod.com/Challenge/Problem.html#problemId=1202）liner_dp|classical|different_subsequence


"""
import bisect
from collections import defaultdict, Counter, deque
from functools import lru_cache
from typing import List

from src.basis.binary_search.template import BinarySearch
from src.mathmatics.comb_perm.template import Combinatorics
from src.mathmatics.number_theory.template import PrimeSieve
from src.utils.fast_io import FastIO
from src.utils.fast_io import inf


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lc_1770(nums: List[int], multipliers: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/maximum-score-from-performing-multiplication-operations/
        tag: liner_dp
        """

        @lru_cache(None)
        def dfs(i, j):
            ind = i + (n - 1 - j)
            if ind == m:
                return 0
            a, b = dfs(i + 1, j) + nums[i] * multipliers[ind], dfs(i, j - 1) + nums[j] * multipliers[ind]
            return a if a > b else b

        n = len(nums)
        m = len(multipliers)
        return dfs(0, n - 1)

    @staticmethod
    def lc_823(arr: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/binary-trees-with-factors/description/
        tag: liner_dp|counter
        """
        mod = 10 ** 9 + 7
        n = len(arr)
        arr.sort()
        dct = {num: i for i, num in enumerate(arr)}

        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = 1
            x = arr[i]
            for j in range(i):
                y = arr[j]
                if y * y > x:
                    break
                if x % y == 0 and x // y in dct:
                    if y == x // y:
                        dp[i] += dp[j] * dp[j]
                    else:
                        dp[i] += dp[j] * dp[dct[x // y]] * 2
                    dp[i] %= mod
        return sum(dp) % mod

    @staticmethod
    def lc_2289(nums: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/steps-to-make-array-non-decreasing/
        tag: liner_dp|counter|monotonic_stack|linked_list
        """
        n = len(nums)
        stack = []
        for i in range(n - 1, -1, -1):
            cnt = 0
            while stack and stack[-1][0] < nums[i]:
                _, x = stack.pop()
                cnt = cnt + 1 if cnt + 1 > x else x
            stack.append([nums[i], cnt])
        return max(ls[1] for ls in stack)

    @staticmethod
    def lc_2361(regular: List[int], express: List[int], express_cost: int) -> List[int]:
        """
        url: https://leetcode.cn/problems/minimum-costs-using-the-train-line/
        tag: linear_dp
        """
        n = len(regular)
        cost = [[0, 0] for _ in range(n + 1)]
        cost[0][1] = express_cost
        for i in range(1, n + 1):
            cost[i][0] = min(cost[i - 1][0] + regular[i - 1],
                             cost[i - 1][1] + express[i - 1])
            cost[i][1] = min(cost[i][0] + express_cost,
                             cost[i - 1][1] + express[i - 1])
        return [min(c) for c in cost[1:]]

    @staticmethod
    def cf_1913d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1913/problem/D
        tag: monotonic_stack|linear_dp|prefix_sum
        """
        mod = 998244353

        for _ in range(ac.read_int()):
            n = ac.read_int()
            nums = ac.read_list_ints()
            pre = [0] * (n + 1)
            dp = [0] * n
            stack = []
            ans = 0
            for i in range(n):
                while stack and nums[stack[-1]] > nums[i]:
                    ans -= dp[stack.pop()]
                j = -1 if not stack else stack[-1]
                dp[i] = (ans + pre[i] - pre[j + 1] + int(len(stack) == 0)) % mod
                ans += dp[i]
                ans %= mod
                stack.append(i)
                pre[i + 1] = (pre[i] + dp[i]) % mod
            ac.st(ans)
        return

    @staticmethod
    def cf_1286a(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1286/A
        tag: liner_dp
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        ex = set(nums)
        cnt = Counter([i % 2 for i in range(1, n + 1) if i not in ex])

        @ac.bootstrap
        def dfs(i, single, double, pre):
            if (i, single, double, pre) in dct:
                yield
            if i == n:
                dct[(i, single, double, pre)] = 0
                yield
            res = inf
            if nums[i] != 0:
                v = nums[i] % 2
                yield dfs(i + 1, single, double, v)
                cur = dct[(i + 1, single, double, v)]
                if pre != -1 and pre != v:
                    cur += 1
                res = ac.min(res, cur)
            else:
                if single:
                    yield dfs(i + 1, single - 1, double, 1)
                    cur = dct[(i + 1, single - 1, double, 1)]
                    if pre != -1 and pre != 1:
                        cur += 1
                    res = ac.min(res, cur)
                if double:
                    yield dfs(i + 1, single, double - 1, 0)
                    cur = dct[(i + 1, single, double - 1, 0)]
                    if pre != -1 and pre != 0:
                        cur += 1
                    res = ac.min(res, cur)
            dct[(i, single, double, pre)] = res
            yield

        dct = dict()
        dfs(0, cnt[1], cnt[0], -1)
        ac.st(dct[(0, cnt[1], cnt[0], -1)])
        return

    @staticmethod
    def lc_2638(nums: List[int], k: int) -> int:
        """
        url: https://leetcode.cn/problems/count-the-number-of-k-free-subsets/
        tag: liner_dp|counter
        """
        n = len(nums)
        dp = [1] * (n + 1)
        dp[1] = 2
        for i in range(2, 51):
            dp[i] = dp[i - 1] + dp[i - 2]
        dct = set(nums)
        ans = 1
        for num in nums:
            if num - k not in dct:
                cnt = 0
                while num in dct:
                    cnt += 1
                    num += k
                ans *= dp[cnt]
        return ans

    @staticmethod
    def lc_2597(nums: List[int], k: int) -> int:
        """
        url: https://leetcode.cn/problems/the-number-of-beautiful-subsets/
        tag: liner_dp|hash
        """
        power = [1 << i for i in range(21)]

        def check(tmp):
            m = len(tmp)
            dp = [1] * (m + 1)
            dp[1] = power[tmp[0]] - 1 + dp[0]
            for i in range(1, m):
                dp[i + 1] = dp[i - 1] * (power[tmp[i]] - 1) + dp[i]
            return dp[-1]

        cnt = Counter(nums)
        ans = 1
        for num in cnt:
            if num - k not in cnt:
                lst = []
                while num in cnt:
                    lst.append(cnt[num])
                    num += k
                ans *= check(lst)
        return ans - 1

    @staticmethod
    def cf_1525d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1525/D
        tag: liner_dp
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        busy = [i for i in range(n) if nums[i]]
        free = [i for i in range(n) if not nums[i]]
        if not busy:
            ac.st(0)
            return
        a, b = len(busy), len(free)
        dp = [[inf] * (b + 1) for _ in range(a + 1)]
        dp[0] = [0] * (b + 1)
        for i in range(a):
            for j in range(b):
                dp[i + 1][j + 1] = ac.min(dp[i + 1][j], dp[i][j] + abs(busy[i] - free[j]))
        ac.st(dp[-1][-1])
        return

    @staticmethod
    def cf_1437c(n, nums):
        """
        url: https://codeforces.com/problemset/problem/1437/C
        tag: liner_dp
        """
        nums.sort()
        m = 2 * n
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(m):
            dp[i + 1][0] = 0
            for j in range(n):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i][j] + abs(nums[j] - i - 1))
        return dp[m][n]

    @staticmethod
    def lg_p4933(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4933
        tag: linear_dp|counter
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        mod = 998244353
        ans = n
        dp = [defaultdict(int) for _ in range(n)]
        for i in range(n):
            for j in range(i):
                dp[i][nums[i] - nums[j]] += dp[j][nums[i] - nums[j]] + 1
                dp[i][nums[i] - nums[j]] %= mod
            for j in dp[i]:
                ans += dp[i][j]
                ans %= mod
        ac.st(ans)
        return

    @staticmethod
    def ac_96(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/98/
        tag: liner_dp|classical|hanoi_tower
        """
        n = 12
        dp3 = [inf] * (n + 1)
        dp3[0] = 0
        dp3[1] = 1
        for i in range(2, n + 1):
            dp3[i] = 2 * dp3[i - 1] + 1

        dp4 = [inf] * (n + 1)
        dp4[0] = 0
        dp4[1] = 1
        for i in range(2, n + 1):
            dp4[i] = min(2 * dp4[j] + dp3[i - j] for j in range(1, i))

        for x in range(1, n + 1):
            ac.st(dp4[x])
        return

    @staticmethod
    def lg_p1280(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1280
        tag: reverse_order|linear_dp
        """
        n, k = ac.read_list_ints()
        dct = [[] for _ in range(n + 1)]
        for _ in range(k):
            p, t = ac.read_list_ints()
            dct[p].append(p + t)
        dp = [0] * (n + 2)
        for i in range(n, 0, -1):
            if not dct[i]:
                dp[i] = dp[i + 1] + 1
            else:
                for end in dct[i]:
                    dp[i] = ac.max(dp[i], dp[end])
        ac.st(dp[1])
        return

    @staticmethod
    def lg_p1282(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1282
        tag: classical|liner_dp|hash
        """
        n = ac.read_int()
        nums = [ac.read_list_ints() for _ in range(n)]
        pre = defaultdict(lambda: inf)
        pre[0] = 0
        for i in range(n):
            a, b = nums[i]
            cur = defaultdict(lambda: inf)
            for p in pre:
                cur[p + a - b] = ac.min(cur[p + a - b], pre[p])
                cur[p + b - a] = ac.min(cur[p + b - a], pre[p] + 1)
            pre = cur.copy()
        x = min(abs(v) for v in pre.keys())
        ans = inf
        for v in pre:
            if abs(v) == x:
                ans = ac.min(ans, pre[v])
        ac.st(ans)
        return

    @staticmethod
    def lg_p1356(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1356
        tag: classical|mod|linear_dp
        """
        m = ac.read_int()
        for _ in range(m):
            n, k = ac.read_list_ints()
            nums = ac.read_list_ints()
            pre = [0] * k
            pre[nums[0] % k] = 1
            for num in nums[1:]:
                cur = [0] * k
                for a in [num, -num]:
                    for i in range(k):
                        if pre[i]:
                            cur[(i + a) % k] = 1
                pre = cur[:]
            ac.st("Divisible" if pre[0] else "Not divisible")
        return

    @staticmethod
    def lg_p1385(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1385
        tag: liner_dp|prefix_sum|brain_teaser|lexicographical_order
        """
        mod = 10 ** 9 + 7
        for _ in range(ac.read_int()):
            s = ac.read_str()
            n = len(s)
            t = sum(ord(w) - ord("a") + 1 for w in s)
            pre = [0] * (t + 1)
            pre[0] = 1

            for _ in range(n):
                cur = [0] * (t + 1)
                x = 0
                for i in range(t + 1):
                    cur[i] = x
                    x += pre[i]
                    x %= mod
                    if i >= 26:
                        x -= pre[i - 26]
                        x %= mod
                pre = cur[:]
            ac.st((pre[-1] - 1) % mod)
        return

    @staticmethod
    def lg_p1809(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1809
        tag: brain_teaser|liner_dp|greedy|specific_plan
        """
        n = ac.read_int()
        nums = [ac.read_int() for _ in range(n)]
        if n == 1:
            ac.st(nums[0])
            return
        nums.sort()
        dp = [inf] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        dp[2] = ac.max(nums[0], nums[1])
        for i in range(2, n):
            dp[i + 1] = ac.min(dp[i] + nums[0] + nums[i],
                               dp[i - 1] + nums[0] + 2 * nums[1] + nums[i])
        ac.st(dp[-1])
        return

    @staticmethod
    def lg_p1868(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1868
        tag: liner_dp|binary_search
        """
        n = ac.read_int()
        nums = [ac.read_list_ints() for _ in range(n)]
        dp = [0] * (n + 1)
        nums.sort(key=lambda it: it[1])
        pre = []
        for i in range(n):
            x, y = nums[i]
            dp[i + 1] = dp[i]
            j = bisect.bisect_right(pre, x - 1) - 1
            dp[i + 1] = ac.max(dp[i + 1], dp[j + 1] + y - x + 1)
            pre.append(y)
        ac.st(dp[-1])
        return

    @staticmethod
    def lg_p1978(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1978
        tag: liner_dp|mul|inclusion_exclusion
        """
        n, k = ac.read_list_ints()
        nums = ac.read_list_ints()
        dct = set(nums)
        ans = 0
        for num in nums:
            if num % k == 0 and num // k in dct:
                continue
            x = 0
            while num in dct:
                x += 1
                num *= k
            ans += (x + 1) // 2
        ac.st(ans)
        return

    @staticmethod
    def lg_p2246(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2246
        tag: string|counter|liner_dp
        """
        s = ""
        while True:
            cur = ac.read_str()
            if not cur or cur == "eof":
                break
            s += cur.lower()
        t = list("HelloWorld".lower())
        dct = set(t)
        ind = defaultdict(list)
        for i, w in enumerate(t):
            ind[w].append(i)
        m = len(t)
        pre = [0] * m
        mod = 10 ** 9 + 7
        for w in s:
            if w not in dct:
                continue
            cur = pre[:]
            for i in ind[w]:
                if i:
                    cur[i] += pre[i - 1]
                else:
                    cur[i] += 1
            pre = [num % mod for num in cur]
        ac.st(pre[-1])
        return

    @staticmethod
    def lg_p2359(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2359
        tag: linear_dp
        """
        primes = PrimeSieve().eratosthenes_sieve(10000)
        primes = [str(num) for num in primes if 1000 >
                  num >= 100 and "0" not in str(num)]
        cnt = defaultdict(list)
        for num in primes:
            cnt[num[:-1]].append(num)
        pre = defaultdict(int)
        for num in primes:
            pre[num[1:]] += 1

        mod = 10 ** 9 + 9
        n = ac.read_int()
        for _ in range(n - 3):
            cur = defaultdict(int)
            for num in pre:
                for nex in cnt[num]:
                    cur[nex[1:]] += pre[num]
            pre = defaultdict(int)
            for num in cur:
                pre[num] = cur[num] % mod
        ans = sum(pre.values()) % mod
        ac.st(ans)
        return

    @staticmethod
    def lg_p2432(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2432
        tag: liner_dp|pointer
        """
        w, n = ac.read_list_ints()
        sentence = ac.read_str()
        words = [ac.read_str()[::-1] for _ in range(w)]

        dp = [inf] * (n + 1)
        dp[0] = 0
        for x in range(n):
            ind = [0] * w
            for j in range(x, -1, -1):
                cur = x - j + 1
                for i in range(w):
                    m = len(words[i])
                    if ind[i] < m and sentence[j] == words[i][ind[i]]:
                        ind[i] += 1
                    if ind[i] == m:
                        cur = ac.min(cur, x - j + 1 - m)
                dp[x + 1] = ac.min(dp[x + 1], dp[j] + cur)
        ac.st(dp[-1])
        return

    @staticmethod
    def lg_p2439(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2439
        tag: liner_dp|binary_search
        """
        n = ac.read_int()
        nums = [ac.read_list_ints() for _ in range(n)]
        nums.sort(key=lambda it: it[1])
        dp = [0] * (n + 1)
        pre = []
        for i in range(n):
            a, b = nums[i]
            j = bisect.bisect_right(pre, a)
            dp[i + 1] = ac.max(dp[i], dp[j] + b - a)
            pre.append(b)
        ac.st(dp[-1])
        return

    @staticmethod
    def lg_p2476(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2476
        tag: counter|linear_dp|memory_search
        """

        @lru_cache(None)
        def dfs(a, b, c, d, e, pre):
            if a + b + c + d + e == 0:
                return 1
            res = 0
            if a:
                res += (a - int(pre == 2)) * dfs(a - 1, b, c, d, e, 1)
            if b:
                res += (b - int(pre == 3)) * dfs(a + 1, b - 1, c, d, e, 2)
            if c:
                res += (c - int(pre == 4)) * dfs(a, b + 1, c - 1, d, e, 3)
            if d:
                res += (d - int(pre == 5)) * dfs(a, b, c + 1, d - 1, e, 4)
            if e:
                res += e * dfs(a, b, c, d + 1, e - 1, 5)
            res %= mod
            return res

        ac.read_int()
        color = ac.read_list_ints()
        mod = 10 ** 9 + 7
        cnt = Counter(color)
        ac.st(dfs(cnt[1], cnt[2], cnt[3], cnt[4], cnt[5], -1))
        return

    @staticmethod
    def lg_p2849(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2849
        tag: matrix_dp
        """
        n, k = ac.read_list_ints()
        nums = [ac.read_list_ints() for _ in range(n)]
        dis = [[0] * n for _ in range(n)]
        for i in range(n):
            x1, y1 = nums[i]
            for j in range(i + 1, n):
                x2, y2 = nums[j]
                dis[i][j] = abs(x1 - x2) + abs(y1 - y2)

        dp = [[inf] * (k + 1) for _ in range(n)]
        dp[0][0] = 0
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + dis[i - 1][i]
            for j in range(1, k + 1):
                for x in range(i - 1, -1, -1):
                    skip = i - x - 1
                    if j - skip < 0:
                        break
                    dp[i][j] = ac.min(dp[i][j], dp[x][j - skip] + dis[x][i])
        ac.st(dp[-1][-1])
        return

    @staticmethod
    def lg_p3558(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3558
        tag: linear_dp|implemention
        """
        ac.read_int()
        nums = ac.read_list_ints()
        pre = [inf, inf, inf]
        pre[nums[0]] = 0
        for num in nums[1:]:
            cur = [inf, inf, inf]
            for x in [-1, 0, 1]:
                for k in range(3):
                    y = num + k * x
                    if x <= y and -1 <= y <= 1:
                        cur[y] = ac.min(cur[y], pre[x] + k)
            pre = cur[:]
        ans = min(pre)
        ac.st(ans if ans < inf else "BRAK")
        return

    @staticmethod
    def lc_2746(words: List[str]) -> int:
        """
        url: https://leetcode.cn/problems/decremental-string-concatenation/
        tag: hash|liner_dp|implemention
        """
        pre = defaultdict(int)
        pre[words[0][0] + words[0][-1]] = len(words[0])

        for a in words[1:]:
            cur = defaultdict(lambda: inf)
            for b in pre:

                if a[-1] == b[0]:
                    x = len(a) - 1 + pre[b]
                else:
                    x = len(a) + pre[b]
                cur[a[0] + b[-1]] = min(cur[a[0] + b[-1]], x)

                if b[-1] == a[0]:
                    x = len(a) - 1 + pre[b]
                else:
                    x = len(a) + pre[b]
                cur[b[0] + a[-1]] = min(cur[b[0] + a[-1]], x)
            pre = cur

        return min(pre.values())

    @staticmethod
    def lg_b3734(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/B3734
        tag: linear_dp
        """
        n, r1 = ac.read_list_ints()
        nums = [r1]
        while len(nums) < n:
            nums.append((nums[-1] * 6807 + 2831) % 201701)
        nums = [num % 100 for num in nums]

        dp = [[inf] * 100 for _ in range(2)]
        pre = 0
        for x in range(100):
            y = abs(x - nums[0])
            dp[pre][x] = ac.min(y * y, (100 - y) * (100 - y))
        for i in range(1, n):
            cur = 1 - pre
            for j in range(100):
                y = abs(j - nums[i])
                res = inf
                a = ac.min(y * y, (100 - y) * (100 - y))
                for k in range(j):
                    res = ac.min(res, a + dp[pre][k])
                dp[cur][j] = res
            pre = cur
        ac.st(min(dp[pre]))
        return

    @staticmethod
    def lg_p3901(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3901
        tag: pointer|linear_dp|pointer
        """
        n, q = ac.read_list_ints()
        nums = ac.read_list_ints()
        ind = dict()
        for i in range(n):
            x = nums[i]
            if x in ind:
                nums[i] = ind[x]
            else:
                nums[i] = -1
            ind[x] = i
            if i:
                nums[i] = ac.max(nums[i], nums[i - 1])
        for _ in range(q):
            left, right = ac.read_list_ints_minus_one()
            ac.st("Yes" if nums[right] < left else "No")
        return

    @staticmethod
    def lg_p4401(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4401
        tag: linear_dp
        """
        ac.read_int()
        s = ac.read_str()
        pre = defaultdict(int)
        pre[("", "")] = 0
        for w in s:
            cur = defaultdict(int)
            for p1, p2 in pre:
                st = p1 + w
                cur[(st[-2:], p2)] = ac.max(cur[(st[-2:], p2)], pre[(p1, p2)] + len(set(st)))

                st = p2 + w
                cur[(p1, st[-2:])] = ac.max(cur[(p1, st[-2:])], pre[(p1, p2)] + len(set(st)))
            pre = cur
        ac.st(max(pre.values()))
        return

    @staticmethod
    def lg_p5095(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P5095
        tag: classical|linear_dp
        """
        n, length = ac.read_list_ints()
        nums = [ac.read_list_ints() for _ in range(n)]
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(n):
            w = h = 0
            for j in range(i, -1, -1):
                w += nums[j][1]
                h = ac.max(h, nums[j][0])
                if w > length:
                    break
                if dp[j] + h < dp[i + 1]:
                    dp[i + 1] = dp[j] + h
        ac.st(dp[-1])
        return

    @staticmethod
    def lg_p5810(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P5810
        tag: linear_dp
        """
        n = ac.read_int()
        dp = [0]
        while dp[-1] < n:
            m = len(dp)
            cur = dp[-1] + 1
            x = 1
            while x * 2 + 5 <= m:
                cur = ac.max(dp[-x * 2 - 5] * (x + 1), cur)
                x += 1
            dp.append(cur)
        ac.st(len(dp) - 1)
        return

    @staticmethod
    def lg_p6040(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6040
        tag: monotonic_queue|linear_dp
        """
        n, k, d, x, tp = ac.read_list_ints()
        mod = 10 ** 9
        nums = []
        seed = 0
        xx = int("0x66CCFF", 16)
        if tp == 0:
            nums = ac.read_list_ints()
        else:
            seed = ac.read_int()
            seed = (seed * xx % mod + 20120712) % mod

        pre = nums[0] if not tp else seed
        stack = deque([[0, pre - d]])
        for i in range(1, n):
            seed = nums[i] if not tp else (seed * xx % mod + 20120712) % mod

            while stack and stack[0][0] < i - x:
                stack.popleft()
            cur = pre + seed + k
            if stack:
                cur = ac.min(cur, stack[0][1] + i * d + seed + k)

            while stack and stack[-1][1] >= cur - i * d - d:
                stack.pop()
            stack.append([i, cur - i * d - d])
            pre = cur
        ac.st(pre)
        return

    @staticmethod
    def lg_p6120(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6120
        tag: linear_dp|implemention
        """
        n = ac.read_int()
        ind = {w: i for i, w in enumerate("HSP")}
        dp = [[[0, -inf], [0, -inf], [0, -inf]] for _ in range(2)]
        pre = 0
        for _ in range(n):
            cur = 1 - pre
            i = ind[ac.read_str()]
            w = (i - 1) % 3
            for j in range(3):
                dp[cur][j][0] = dp[pre][j][0]
                dp[cur][j][1] = max(dp[pre][j][1], max(dp[pre][k][0] for k in range(3) if k != j))
                if j == w:
                    dp[cur][j][0] += 1
                    dp[cur][j][1] += 1
            pre = cur
        ac.st(max(max(d) for d in dp[pre]))
        return

    @staticmethod
    def lg_p6146(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6146
        tag: linear_dp|brute_force|counter
        """
        n = ac.read_int()
        nums = [ac.read_list_ints() for _ in range(n)]
        nums.sort(key=lambda it: it[0])
        mod = 10 ** 9 + 7
        pp = [1] * (n + 1)
        for i in range(1, n + 1):
            pp[i] = (pp[i - 1] * 2) % mod

        dp = [0] * n
        dp[0] = 1
        lst = [nums[0][1]]
        for i in range(1, n):
            a, b = nums[i]
            j = bisect.bisect_left(lst, a)
            dp[i] = 2 * dp[i - 1] + pp[j]
            dp[i] %= mod
            bisect.insort_left(lst, b)
        ac.st(dp[-1])
        return

    @staticmethod
    def lc_2713(mat: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/
        tag: data_range|liner_dp
        """
        m, n = len(mat), len(mat[0])
        dct = defaultdict(list)
        for i in range(m):
            for j in range(n):
                dct[mat[i][j]].append([i, j])
        row = [0] * m
        col = [0] * n
        for val in sorted(dct):
            lst = []
            for i, j in dct[val]:
                x = row[i] if row[i] > col[j] else col[j]
                lst.append([i, j, x + 1])
            for i, j, w in lst:
                if col[j] < w:
                    col[j] = w
                if row[i] < w:
                    row[i] = w
        return max(max(row), max(col))

    @staticmethod
    def lg_p7994(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P7994
        tag: linear_dp
        """
        n = ac.read_int()
        a = ac.read_list_ints()
        b = ac.read_list_ints()

        nums = [a[i] - b[i] for i in range(n)]
        ans = abs(nums[0])
        for i in range(1, n):
            x, y = nums[i - 1], nums[i]
            if x == 0:
                ans += abs(y)
            elif y == 0:
                continue
            else:
                if x * y < 0:
                    ans += abs(y)
                else:
                    if x > 0:
                        ans += ac.max(0, y - x)
                    else:
                        ans += ac.max(0, x - y)
        ac.st(ans)
        return

    @staticmethod
    def lg_p8816(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8816
        tag: classical|matrix_dp|implemention
        """
        n, k = ac.read_list_ints()
        nums = sorted([ac.read_list_ints() for _ in range(n)])
        dp = [list(range(1, k + 2)) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            x, y = nums[i]
            for j in range(i + 1, n):
                a, b = nums[j]
                if a >= x and b >= y:
                    dis = a - x + b - y - 1
                    for r in range(k + 1):
                        if r + dis <= k:
                            dp[i][r + dis] = ac.max(dp[i][r + dis], dp[j][r] + dis + 1)
                        else:
                            break
        ac.st(max(max(d) for d in dp))
        return

    @staticmethod
    def ac_4414(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/description/4417/
        tag: liner_dp
        """
        ac.read_int()
        nums = ac.read_list_ints()
        ans = -inf
        pre = [-inf, -inf]
        for num in nums:
            cur = pre[:]
            for i in range(2):
                j = (i + num) % 2
                cur[j] = ac.max(cur[j], pre[i] + num)
                j = num % 2
                cur[j] = ac.max(cur[j], num)
            pre = cur[:]
            ans = ac.max(ans, pre[1])
        ac.st(ans)
        return

    @staticmethod
    def lc_1824(obstacles: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/minimum-sideway-jumps/description/
        tag: liner_dp|rolling_update
        """
        n = len(obstacles)
        dp = [1, 0, 1]
        for i in range(n):
            x = obstacles[i]
            if x:
                dp[x - 1] = inf
            low = min(dp)
            for j in range(3):
                if j != x - 1:
                    dp[j] = dp[j] if dp[j] < low + 1 else low + 1
        return min(dp)

    @staticmethod
    def lc_978(arr: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/longest-turbulent-subarray/description/
        tag: liner_dp|rolling_update
        """
        n = len(arr)
        ans = dp0 = dp1 = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                dp1 = dp0 + 1
                dp0 = 1
            elif arr[i] < arr[i - 1]:
                dp0 = dp1 + 1
                dp1 = 1
            else:
                dp0 = dp1 = 1
            ans = ans if ans > dp0 else dp0
            ans = ans if ans > dp1 else dp1
        return ans

    @staticmethod
    def lc_1027(nums: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/longest-arithmetic-subsequence/
        tag: liner_dp
        """
        seen = set()
        count = dict()
        for num in nums:
            for pre in seen:
                d = num - pre
                count[(num, d)] = count.get((pre, d), 1) + 1
            seen.add(num)
        return max(count.values())

    @staticmethod
    def lc_1553(n: int) -> int:
        """
        url: https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/
        tag: brain_teaser|greedy|memory_search|liner_dp
        """

        @lru_cache(None)
        def dfs(num):
            if num <= 1:
                return num
            a = num % 2 + 1 + dfs(num // 2)
            b = num % 3 + 1 + dfs(num // 3)
            return a if a < b else b

        return dfs(n)

    @staticmethod
    def cf_1829h(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1829/problem/H
        tag: counter|linear_dp|classical|bit_operation|data_range
        """
        mod = 10 ** 9 + 7
        ceil = 2 * 10 ** 5
        power = [1] * (ceil + 1)
        for i in range(1, ceil + 1):
            power[i] = (power[i - 1] * 2) % mod

        for _ in range(ac.read_int()):
            n, k = ac.read_list_ints()
            cnt = [0] * 64
            for num in ac.read_list_ints():
                cnt[num] += 1

            pre = [0] * 64
            for num in range(64):
                if cnt[num]:
                    cur = pre[:]
                    for p in range(64):
                        cur[p & num] += pre[p] * (power[cnt[num]] - 1) % mod
                    cur[num] += (power[cnt[num]] - 1) % mod
                    pre = [x % mod for x in cur]
            ans = 0
            for p in range(64):
                if bin(p).count("1") == k:
                    ans += pre[p]
            ans %= mod
            ac.st(ans)
        return

    @staticmethod
    def cf_1154f(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1154/problem/F
        tag: linear_dp|reverse_thinking|brute_force|greedy|implemention|data_range
        """
        n, m, k = ac.read_list_ints()
        nums = ac.read_list_ints()
        nums.sort()
        nums = nums[:k]
        pre = ac.accumulate(nums)
        cost = [0] * (k + 1)
        for _ in range(m):
            x, y = ac.read_list_ints()
            if x <= k and cost[x] < y:
                cost[x] = y
        dp = [inf] * (k + 1)
        dp[k] = 0
        for i in range(k - 1, -1, -1):
            dp[i] = dp[i + 1] + nums[i]
            for j in range(i, k):
                x = j - i + 1
                y = cost[x]
                cur = dp[j + 1] + pre[j + 1] - pre[i] - (pre[i + y] - pre[i])
                if cur < dp[i]:
                    dp[i] = cur
        ac.st(dp[0])
        return

    @staticmethod
    def library_check_1(ac=FastIO()):
        """
        url: https://www.51nod.com/Challenge/Problem.html#problemId=1202
        tag: liner_dp|classical|different_subsequence
        """
        mod = 10 ** 9 + 7
        n = ac.read_int()
        dp = [0] * (n + 1)
        pre = dict()
        for i in range(n):
            num = ac.read_int()
            if num not in pre:
                dp[i + 1] = (2 * dp[i] + 1) % mod
            else:
                dp[i + 1] = (2 * dp[i] - dp[pre[num]]) % mod
            pre[num] = i
        ac.st(dp[-1])
        return

    @staticmethod
    def abc_285e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc285/tasks/abc285_e
        tag: linear_dp|brain_teaser|circular_array|classical
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        pre = ac.accumulate(nums)

        def cost(k):
            return pre[k // 2] + pre[(k + 1) // 2]

        dp = [-inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + cost(i - j - 1))
        ac.st(dp[-1])
        return

    @staticmethod
    def abc_275f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc275/tasks/abc275_f
        tag: matrix_dp|linear_dp|classical
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()

        dp = [[inf] * (m + 1) for _ in range(2)]
        dp[0][0] = 0
        for num in nums:
            ndp = [[inf] * (m + 1) for _ in range(2)]
            for pre in range(2):
                for s in range(m + 1):
                    if pre:
                        ndp[pre][s] = min(ndp[pre][s], dp[pre][s])
                        if num + s <= m:
                            ndp[0][num + s] = min(ndp[0][num + s], dp[pre][s])
                    else:
                        if num + s <= m:
                            ndp[pre][num + s] = min(ndp[pre][num + s], dp[pre][s])

                        ndp[1][s] = min(ndp[1][s], dp[pre][s] + 1)
            dp = ndp
        for x in range(1, m + 1):
            ans = min(dp[0][x], dp[1][x])
            ac.st(ans if ans < inf else -1)
        return

    @staticmethod
    def abc_248f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc248/tasks/abc248_f
        tag: connected_graph|linear_dp|classical
        """
        n, mod = ac.read_list_ints()

        dp = [[0] * n for _ in range(2)]
        dp[1][0] = 1
        for _ in range(n - 1):
            for rem in range(n - 1, -1, -1):
                for state in range(2):
                    res = 0
                    if not state:
                        if rem > 0:
                            res += dp[state][rem - 1]
                        res += dp[1][rem]
                    else:
                        res += dp[0][rem - 2] * 2
                        res += dp[1][rem - 1] * 3
                        res += dp[1][rem]
                    dp[state][rem] = res % mod
        ans = [(dp[0][x - 1] + dp[1][x]) % mod for x in range(1, n)]
        ac.lst(ans)
        return

    @staticmethod
    def abc_244e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc244/tasks/abc244_e
        tag: implemention|linear_dp
        """
        mod = 998244353
        n, m, k, s, t, x = ac.read_list_ints()
        s -= 1
        t -= 1
        x -= 1
        dp = [[0] * n, [0] * n]
        dp[0][s] = 1
        edges = [ac.read_list_ints_minus_one() for _ in range(m)]
        for _ in range(k):
            ndp = [[0] * n, [0] * n]
            for i, j in edges:
                for a, b in [(i, j), (j, i)]:
                    for w in range(2):
                        if b == x:
                            ndp[1 - w][b] += dp[w][a]
                        else:
                            ndp[w][b] += dp[w][a]
            dp = [[x % mod for x in ls] for ls in ndp]
        ans = dp[0][t]
        ac.st(ans)
        return

    @staticmethod
    def abc_243g(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc243/tasks/abc243_g
        tag: prefix_sum|preprocess|linear_dp|brain_teaser|high_precision|sqrt_sqrt_n|math
        """

        def sqrt(m):

            def check(s):
                return s * s <= m

            return BinarySearch().find_int_right(1, m, check)

        def sqrt_sqrt(m):

            def check(s):
                return s * s * s * s <= m

            return BinarySearch().find_int_right(1, m, check)

        x = 9 * 10 ** 18
        n = sqrt_sqrt(x) + 10
        dp = [0] * (n + 1)
        dp[1] = 1
        pre = ac.accumulate(dp)
        for i in range(2, n + 1):
            dp[i] = pre[sqrt(i) + 1] - pre[1]
            pre[i + 1] = pre[i] + dp[i]
        for _ in range(ac.read_int()):
            x = ac.read_int()
            sx = sqrt(x)
            fx = sqrt_sqrt(x)
            ans = sum(dp[i] * (sx - i * i + 1) for i in range(1, fx + 1))
            ac.st(ans)
        return

    @staticmethod
    def abc_350e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc350/tasks/abc350_e
        tag: linear_dp|implemention|prob_dp|expectation_dp|classical
        """

        n, a, x, y = ac.read_list_ints()

        @lru_cache(None)
        def dfs(num):
            if num == 0:
                return 0
            res = dfs(num // a) + x
            res = min(res, (sum(dfs(num // aa) for aa in range(2, 7)) + 6 * y) / 5)
            return res

        ac.st(dfs(n))
        return

    @staticmethod
    def abc_234g(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc234/tasks/abc234_g
        tag: monotonic_stack|linear_dp|prefix_sum|contribution_method|classical
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        dp = [0] * (n + 1)
        mx = [0] * (n + 1)
        mi = [0] * (n + 1)
        mod = 998244353
        dp[0] = 1
        mx_stack = []
        mi_stack = []
        for i in range(1, n + 1):
            while mx_stack and nums[mx_stack[-1] - 1] <= nums[i - 1]:
                mx_stack.pop()
            while mi_stack and nums[mi_stack[-1] - 1] >= nums[i - 1]:
                mi_stack.pop()

            if not mx_stack:
                mx[i] = dp[i - 1] * nums[i - 1] % mod
            else:
                x = mx_stack[-1]
                mx[i] = mx[x] + (dp[i - 1] - dp[x - 1]) * nums[i - 1]
                mx[i] %= mod

            if not mi_stack:
                mi[i] = dp[i - 1] * nums[i - 1] % mod
            else:
                x = mi_stack[-1]
                mi[i] = mi[x] + (dp[i - 1] - dp[x - 1]) * nums[i - 1]
                mi[i] %= mod

            dp[i] = (dp[i - 1] + mx[i] - mi[i]) % mod
            mx_stack.append(i)
            mi_stack.append(i)

        ac.st((dp[n] - dp[n - 1]) % mod)
        return

    @staticmethod
    def abc_234f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc234/tasks/abc234_f
        tag: brute_force|linear_dp|comb|math
        """
        mod = 998244353
        s = ac.read_str()
        cnt = Counter(s)
        n = len(s)
        cb = Combinatorics(n + 10, mod)
        dp = [0] * (n + 1)
        dp[0] = 1
        for w in cnt:
            ndp = dp[:]
            for x in range(n + 1):
                for y in range(1, cnt[w] + 1):
                    if x + y > n:
                        break
                    ndp[x + y] += dp[x] * cb.comb(x + y, y)
            dp = [x % mod for x in ndp]
        ac.st(sum(dp[1:]) % mod)
        return

    @staticmethod
    def cf_1969c(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1969/problem/C
        tag: linear_dp|data_range|implemention
        """
        for _ in range(ac.read_int()):
            n, k = ac.read_list_ints()
            nums = ac.read_list_ints()

            dp = deque([[inf] * (k + 1) for _ in range(20)])
            dp[-1][0] = 0
            for i in range(n):
                cur = [inf] * (k + 1)
                cnt = 0
                val = inf
                for x in range(k + 1):
                    cur[x] = dp[-1][x] + nums[i]
                for j in range(i, max(-1, i - 11), -1):
                    if nums[j] < val:
                        val = nums[j]
                        cnt = 1
                    elif nums[j] == val:
                        cnt += 1
                    tot = i - j + 1
                    for x in range(k + 1):
                        y = x + (tot - cnt)
                        if y > k:
                            break
                        cur[y] = min(cur[y], dp[-(i - j + 1)][x] + val * tot)
                dp.append(cur[:])
                dp.popleft()
            ac.st(min(dp[-1]))
        return

    @staticmethod
    def abc_224f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc224/tasks/abc224_f
        tag: linear_dp|contribution_method|math
        """
        mod = 998244353
        s = ac.read_str()
        n = len(s)
        dp = [0] * (n + 1)
        cnt = [0] * (n + 1)
        cnt[n] = 1
        cnt[n - 1] = 1
        post_sum = post = 0
        tot = 10
        for i in range(n - 1, -1, -1):
            cnt[i] = 2 * cnt[i + 1] if i < n - 1 else 1
            cnt[i] %= mod
            if i == n - 1:
                tot = 0
            else:
                tot = (tot + cnt[i + 2]) * 10 % mod
            post = post + int(s[i]) * tot + int(s[i]) * cnt[i + 1]
            post %= mod
            dp[i] = (post_sum + post) % mod
            post_sum = (post_sum + dp[i]) % mod
        ac.st(dp[0] % mod)
        return

    @staticmethod
    def cf_264c(ac=FastIO()):
        """
        url: https://codeforces.com/contest/264/problem/C
        tag: linear_dp|classical|maximum_second
        """
        n, q = ac.read_list_ints()
        v = ac.read_list_ints()
        c = ac.read_list_ints_minus_one()
        for _ in range(q):
            a, b = ac.read_list_ints()
            dp = [-inf] * n
            c1, ceil1 = 0, -inf
            c2, ceil2 = 0, -inf
            ans = 0
            for i, x in enumerate(c):
                cur = dp[x]
                if a * v[i] > 0:
                    cur += a * v[i]
                if c1 != x:
                    if ceil1 + b * v[i] > cur:
                        cur = ceil1 + b * v[i]
                else:
                    if ceil2 + b * v[i] > cur:
                        cur = ceil2 + b * v[i]
                if b * v[i] > cur:
                    cur = b * v[i]
                if c1 == x:
                    if ceil1 < cur:
                        ceil1 = cur
                elif c2 == x:
                    if ceil2 < cur:
                        ceil2 = cur
                else:
                    if cur >= ceil1:
                        c2, ceil2 = c1, ceil1
                        c1, ceil1 = x, cur
                    elif cur > ceil2:
                        c2, ceil2 = x, cur
                dp[x] = cur
                if cur > ans:
                    ans = cur
            ac.st(ans)
        return

    @staticmethod
    def cf_1984c2(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1984/problem/C2
        tag: linear_dp|implemention|greedy
        """

        mod = 998244353
        for _ in range(ac.read_int()):
            ac.read_int()
            nums = ac.read_list_ints()
            pre = defaultdict(int)
            pre[0] = 1
            for num in nums:
                cur = defaultdict(int)
                for p in pre:
                    cur[p + num] += pre[p]
                    cur[abs(p + num)] += pre[p]
                floor = min(cur)
                ceil = max(cur)
                pre = defaultdict(int)
                pre[floor] = cur[floor] % mod
                pre[ceil] = cur[ceil] % mod
            ac.st(pre[max(pre)])
        return