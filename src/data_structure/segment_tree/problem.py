"""
Algorithm：segment_tree|bisect_left
Description：range_sum|range_min|range_add|range_change|range_max|dynamic_segment_tree|defaultdict

====================================LeetCode====================================
218（https://leetcode.cn/problems/the-skyline-problem/solution/by-liupengsay-isfo/）segment_tree|RangeChangeRangeMax
2286（https://leetcode.cn/problems/booking-concert-tickets-in-groups/）segment_tree|RangeAddRangeSumMaxMin
2407（https://leetcode.cn/problems/longest-increasing-subsequence-ii/）segment_tree|RangeAddRangeMax|linear_dp
2158（https://leetcode.cn/problems/amount-of-new-area-painted-each-day/）segment_tree|RangeAddRangeSum
2589（https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/）segment_tree|greedy|bisect_left
732（https://leetcode.cn/problems/my-calendar-iii/）dynamic_segment_tree
1851（https://leetcode.cn/problems/minimum-interval-to-include-each-query/）segment_tree|RangeChangeRangeMin|offline_query|monotonic_queue
2213（https://leetcode.cn/problems/longest-substring-of-one-repeating-character/）segment_tree|sub_consequence|range_query|range_merge
2276（https://leetcode.cn/problems/count-integers-in-intervals/）dynamic_segment_tree|union_find_range|SortedList
1340（https://leetcode.cn/problems/jump-game-v/）segment_tree|linear_dp
2940（https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/）segment_tree|bisect_left
2569（https://leetcode.cn/problems/handling-sum-queries-after-update/）segment_tree|range_reverse|bit_set
3003（https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations）segment_tree|bisect_left|range_or|point_set

=====================================LuoGu======================================
P2846（https://www.luogu.com.cn/problem/P2846）segment_tree|range_reverse|range_sum
P2572（https://www.luogu.com.cn/problem/P2572）segment_tree|range_reverse|range_sum
P2574（https://www.luogu.com.cn/problem/P2574）segment_tree|range_change|range_sum|range_cover
P3130（https://www.luogu.com.cn/problem/P3130）RangeAddRangeSumMaxMin
P3870（https://www.luogu.com.cn/problem/P3870）segment_tree|range_reverse|range_sum
P5057（https://www.luogu.com.cn/problem/P5057）segment_tree|range_reverse|range_sum
P3372（https://www.luogu.com.cn/problem/P3372）RangeAddRangeSumMaxMin
P2880（https://www.luogu.com.cn/problem/P2880）RangeAddRangeSumMaxMin
P1904（https://www.luogu.com.cn/problem/P1904）segment_tree|RangeAscendRangeMax
P1438（https://www.luogu.com.cn/problem/P1438）diff_array|RangeAddRangeSumMaxMin|segment_tree
P1253（https://www.luogu.com.cn/problem/P1253）range_add|range_change|segment_tree|range_sum
P3373（https://www.luogu.com.cn/problem/P3373）range_add|range_mul|segment_tree|range_sum|RangeAffineRangeSum
P4513（https://www.luogu.com.cn/problem/P4513）segment_tree|range_change|range_merge|sub_consequence
P1471（https://www.luogu.com.cn/problem/P1471）math|segment_tree|RangeAddRangeSum
P6492（https://www.luogu.com.cn/problem/P6492）segment_tree|range_change|range_merge|sub_consequence
P4145（https://www.luogu.com.cn/problem/P4145）math|segment_tree|RangeAddRangeSum
P1558（https://www.luogu.com.cn/problem/P1558）segment_tree|RangeSetRangeOr
P3740（https://www.luogu.com.cn/problem/P3740）discretization|segment_tree|RangeChangeRangeSum
P4588（https://www.luogu.com.cn/problem/P4588）segment_tree|RangeChangeRangeMul
P6627（https://www.luogu.com.cn/problem/P6627）segment_tree|range_xor
P8081（https://www.luogu.com.cn/problem/P8081）diff_array|counter|action_scop|segment_tree|RangeSetRangeOr
P8812（https://www.luogu.com.cn/problem/P8812）segment_tree|RangeDescendRangeMin
P8856（https://www.luogu.com.cn/problem/solution/P8856）segment_tree|RangeAddRangeSumMaxMin

===================================CodeForces===================================
482B（https://codeforces.com/problemset/problem/482/B）segment_tree|RangeOrRangeAnd
380C（https://codeforces.com/problemset/problem/380/C）segment_tree|range_merge|sub_consequence|bracket
52C（https://codeforces.com/problemset/problem/52/C）segment_tree|circular_array|RangeChangeRangeMin
438D（https://codeforces.com/problemset/problem/438/D）segment_tree|range_sum|mod|RangeChangeRangeSumMaxMin
558E（https://codeforces.com/contest/558/problem/E）alphabet|segment_tree|sorting
343D（https://codeforces.com/problemset/problem/343/D）dfs_order|segment_tree
242E（https://codeforces.com/problemset/problem/242/E）segment_tree|RangeReverseRangeBitCount
987C（https://codeforces.com/problemset/problem/987/C）brute_force|segment_tree|prefix_suffix
1216F（https://codeforces.com/contest/1216/problem/F）segment_tree|dp|monotonic_queue
1665E（https://codeforces.com/contest/1665/problem/E）segment_tree
1478E（https://codeforces.com/contest/1478/problem/E）RangeSetRangeSumMinMax|backward_thinking|implemention
1679E（https://codeforces.com/contest/1679/problem/B）RangeSetRangeSumMinMax|range_change|range_sum

====================================AtCoder=====================================
ABC332F（https://atcoder.jp/contests/abc332/tasks/abc332_f）RangeAffineRangeSum
ABC287G（https://atcoder.jp/contests/abc287/tasks/abc287_g）segment_tree|range_sum|dynamic|offline

=====================================AcWing=====================================
3805（https://www.acwing.com/problem/content/3808/）RangeAddRangeMin

=====================================LibraryChecker=====================================
1（https://judge.yosupo.jp/problem/range_affine_point_get）RangeAffineRangeSum
2（https://judge.yosupo.jp/problem/range_affine_range_sum）RangeAffineRangeSum
3（https://judge.yosupo.jp/problem/point_set_range_composite）PointSetRangeComposite
4（https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/A）PointSetRangeSum
5（https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/B）segment_tree|point_set|range_min
6（https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/C）segment_tree|point_set|range_min_count
7（https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/A）segment_tree|point_set|range_max_sub_sum
8（https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/B）segment_tree|point_set|range_sum_bisect_left
9（https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/C）segment_tree|point_set|range_max_bisect_left
10（https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/D）segment_tree|point_set|range_max_bisect_left_with_ind
11（https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/A）segment_tree|point_set|range_sum|inversion
12（https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/B）segment_tree|point_set|range_sum|inversion|bisect_left
13（https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/C）segment_tree|point_set|range_sum|range_include
14（https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/D）segment_tree|point_set|range_sum|range_include|reverse_thinking|include_exclude
15（https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/E）segment_tree|range_add|point_get
16（https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/A）segment_tree|point_set|range_sum
17（https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/B）segment_tree|matrix_build|range_mul
18（https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/C）segment_tree|point_set|range_inverse
19（https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/D）segment_tree|point_set|range_or
20（https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A）segment_tree|range_add|point_get
21（https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A）segment_tree|range_ascend|point_get
22（https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A）segment_tree|range_set|point_get
23（https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/E）segment_tree|bisect_left|brute_force|classical|range_min|point_set
24（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/A）segment_tree|range_add|range_min
25（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/B）segment_tree|range_affine|range_sum
26（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/C）segment_tree|range_or|range_and
27（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/D）segment_tree|range_add|range_sum
28（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/E）segment_tree|range_set|range_min
29（https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/F）segment_tree|range_set|range_sum
30（https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/A）segment_tree|range_set|range_max_non_emp_con_sub_sum
31（https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/B）segment_tree|range_reverse|range_bit_count_bisect_left
32（https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/C）segment_tree|range_add|range_max|bisect_left
33（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/A）segment_tree|range_change_add|range_sum
34（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/B）segment_tree|diff_array|range_add|point_get|range_sum
35（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/C）segment_tree|range_set|range_seg_count_length
36（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/D）segment_tree|range_add|range_weighted_sum
37（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/E）segment_tree|range_chmin_chmax|point_get
38（https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/F）segment_tree_dynamic|range_set|range_sum_bisect_left


"""
from collections import defaultdict
from typing import List

from src.data_structure.segment_tree.template import RangeAscendRangeMax, RangeDescendRangeMin, \
    RangeAddRangeSumMinMax, RangeRevereRangeBitCount, RangeSetRangeOr, \
    RangeAddRangeAvgDev, \
    RangeSetRangeSumMinMaxDynamic, PointSetRangeLongestSubSame, \
    RangeOrRangeAnd, RangeSetRangeSumMinMax, RangeKthSmallest, RangeSetRangeMaxNonEmpConSubSum, \
    RangeAffineRangeSum, PointSetRangeComposite, RangeLongestRegularBrackets, \
    RangeXorUpdateRangeXorQuery, PointSetRangeLongestAlter, \
    RangeSqrtRangeSum, RangeSetReverseRangeSumLongestConSub, PointSetRangeOr, PointSetRangeSum, PointSetRangeMin, \
    PointSetRangeMinCount, PointSetRangeMaxSubSum, PointSetRangeMax, RangeAddPointGet, MatrixBuildRangeMul, \
    PointSetRangeInversion, RangeSetPointGet, RangeAscendPointGet, RangeSetAddRangeSumMinMax, \
    RangeSetRangeSegCountLength, RangeAddRangeWeightedSum, RangeChminChmaxPointGet, RangeSetPreSumMaxDynamicDct, \
    PointAddRangeSum1Sum2
from src.data_structure.sorted_list.template import SortedList
from src.utils.fast_io import FastIO
from src.utils.fast_io import inf


class Solution:
    def __int__(self):
        return

    @staticmethod
    def lc_2213(s: str, word: str, indices: List[int]) -> List[int]:
        """
        url: https://leetcode.cn/problems/longest-substring-of-one-repeating-character/
        tag: segment_tree|sub_consequence|range_query|range_merge
        """
        n = len(s)
        tree = PointSetRangeLongestSubSame(n, [ord(w) - ord("a") for w in s])
        ans = []
        for i, w in zip(indices, word):
            ans.append(tree.point_set_rang_longest_sub_same(i, ord(w) - ord("a")))
        return ans

    @staticmethod
    def library_1(ac=FastIO()):
        """
        url: https://judge.yosupo.jp/problem/range_affine_point_get
        tag: RangeAffineRangeSum
        """
        n, q = ac.read_list_ints()
        nums = ac.read_list_ints()
        mod = 998244353
        tree = RangeAffineRangeSum(n, mod)
        tree.build(nums)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 0:
                ll, rr, b, c = lst[1:]
                tree.range_affine(ll, rr - 1, (b << 32) | c)
            else:
                i = lst[1]
                ac.st(tree.range_sum(i, i))
        return

    @staticmethod
    def library_check_2(ac=FastIO()):
        """
        url: https://judge.yosupo.jp/problem/range_affine_range_sum
        tag: RangeAffineRangeSum
        """
        n, q = ac.read_list_ints()
        nums = ac.read_list_ints()
        mod = 998244353
        tree = RangeAffineRangeSum(n, mod)
        tree.build(nums)
        ans = []
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 0:
                ll, rr, b, c = lst[1:]
                tree.range_affine(ll, rr - 1, (b << 32) | c)
            else:
                ll, rr = lst[1:]
                ans.append(str(tree.range_sum(ll, rr - 1)))
        print("\n".join(ans))
        return

    @staticmethod
    def library_3(ac=FastIO()):
        n, q = ac.read_list_ints()
        nums = [ac.read_list_ints() for _ in range(n)]
        m = 32
        mod = 998244353
        tree = PointSetRangeComposite(n, mod, m)
        tree.build([(c << m) | d for c, d in nums])
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 0:
                p, c, d = lst[1:]
                tree.point_set(p, p, (c << m) | d)
            else:
                ll, rr, x = lst[1:]
                val = tree.range_composite(ll, rr - 1)
                mul, add = val >> m, val & tree.mask
                ac.st((mul * x + add) % mod)
        return

    @staticmethod
    def lc_2569(nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """
        url: https://leetcode.cn/problems/handling-sum-queries-after-update/
        tag: segment_tree|range_reverse|bit_set
        """
        n = len(nums1)
        tree = RangeRevereRangeBitCount(n)
        tree.build(nums1)
        ans = []
        s = sum(nums2)
        for op, x, y in queries:
            if op == 1:
                tree.range_reverse(x, y)
            elif op == 2:
                s += tree.range_bit_count(0, n - 1) * x
            else:
                ans.append(s)
        return ans

    @staticmethod
    def lg_p1904(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1904
        tag: segment_tree|RangeAscendRangeMax
        """
        high = 10 ** 4
        segment = RangeAscendRangeMax(high)
        segment.build([0] * high)
        nums = set()
        while True:
            s = ac.read_str()
            if not s:
                break
            x, h, y = [int(w) for w in s.split() if w]
            nums.add(x)
            nums.add(y)
            segment.range_ascend(x, y - 1, h)
        nums = sorted(list(nums))
        n = len(nums)
        height = [segment.range_max(num, num) for num in nums]
        ans = []
        pre = -1
        for i in range(n):
            if height[i] != pre:
                ans.extend([nums[i], height[i]])
                pre = height[i]
        ac.lst(ans)
        return

    @staticmethod
    def cf_242e(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/242/E
        tag: segment_tree|RangeReverseRangeBitCount
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        tree = [RangeRevereRangeBitCount(n) for _ in range(22)]
        for j in range(22):
            lst = [1 if nums[i] & (1 << j) else 0 for i in range(n)]
            tree[j].build(lst)
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr = lst[1:]
                ll -= 1
                rr -= 1
                ans = sum((1 << j) * tree[j].range_bit_count(ll, rr) for j in range(22))
                ac.st(ans)
            else:
                ll, rr, xx = lst[1:]
                ll -= 1
                rr -= 1
                for j in range(22):
                    if (1 << j) & xx:
                        tree[j].range_reverse(ll, rr)
        return

    @staticmethod
    def cf_1216f(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1216/problem/F
        tag: segment_tree|dp|monotonic_queue
        """
        n, k = ac.read_list_ints()
        s = ac.read_str()
        tree = RangeDescendRangeMin(n)
        for i in range(n):
            if s[i] == "1":
                left = ac.max(0, i - k)
                right = ac.min(n - 1, i + k)
                pre = tree.range_min(left - 1, i - 1) if left else 0
                cur = pre + i + 1
                tree.range_descend(i, right, cur)
            else:
                pre = tree.range_min(i - 1, i - 1) if i else 0
                cur = pre + i + 1
                tree.range_descend(i, i, cur)
        ac.st(tree.range_min(n - 1, n - 1))
        return

    @staticmethod
    def cf_1478e(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1478/problem/E
        tag: RangeSetRangeSumMinMax|backward_thinking|implemention
        """
        for _ in range(ac.read_int()):
            def check():
                n, q = ac.read_list_ints()
                s = [int(w) for w in ac.read_str()]
                t = [int(w) for w in ac.read_str()]
                queries = [ac.read_list_ints_minus_one() for _ in range(q)]
                queries.reverse()
                tree = RangeSetRangeSumMinMax(n)
                tree.build(t)
                for ll, rr in queries:
                    cur_sum = tree.range_sum(ll, rr)
                    if cur_sum < rr - ll + 1 - cur_sum:
                        tree.range_set(ll, rr, 0)
                    elif cur_sum > rr - ll + 1 - cur_sum:
                        tree.range_set(ll, rr, 1)
                    else:
                        ac.st("NO")
                        return
                if tree.get() == s:
                    ac.st("YES")
                else:
                    ac.st("NO")
                return

            check()
        return

    @staticmethod
    def cf_1665e(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1665/problem/E
        tag: segment_tree|classical
        """
        for _ in range(ac.read_int()):
            n = ac.read_int()
            nums = ac.read_list_ints()
            tree = RangeKthSmallest(n, 31)
            tree.build(nums)
            for _ in range(ac.read_int()):
                ll, rr = ac.read_list_ints_minus_one()
                lst = tree.range_kth_smallest(ll, rr)
                ans = inf
                m = len(lst)
                for i in range(m):
                    x = lst[i]
                    if x > ans:
                        break
                    for j in range(i + 1, m):
                        y = lst[j]
                        if x > ans:
                            break
                        ans = ac.min(ans, x | y)
                ac.st(ans)
        return

    @staticmethod
    def lc_218(buildings: List[List[int]]) -> List[List[int]]:
        """
        url: https://leetcode.cn/problems/the-skyline-problem/
        tag: segment_tree|RangeChangeRangeMax
        """
        pos = set()
        for left, right, _ in buildings:
            pos.add(left)
            pos.add(right)
        lst = sorted(list(pos))
        n = len(lst)
        dct = {x: i for i, x in enumerate(lst)}

        segment = RangeAscendRangeMax(n)
        segment.build([0] * n)
        for left, right, height in buildings:
            segment.range_ascend(dct[left], dct[right] - 1, height)

        pre = -1
        ans = []
        for pos in lst:
            h = segment.range_max(dct[pos], dct[pos])
            if h != pre:
                ans.append([pos, h])
                pre = h
        return ans

    @staticmethod
    def cf_380c(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/380/C
        tag: segment_tree|range_merge|sub_consequence|bracket
        """
        s = ac.read_str()
        n = len(s)
        tree = RangeLongestRegularBrackets(n)
        tree.build(s)
        for _ in range(ac.read_int()):
            x, y = ac.read_list_ints_minus_one()
            ac.st(tree.range_longest_regular_brackets(x, y))
        return

    @staticmethod
    def lg_p3372(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3372
        tag: RangeAddRangeSumMaxMin
        """
        n, m = ac.read_list_ints()
        segment = RangeAddRangeSumMinMax(n)
        segment.build(ac.read_list_ints())

        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y, k = lst[1:]
                segment.range_add(x - 1, y - 1, k)
            else:
                x, y = lst[1:]
                ac.st(segment.range_sum(x - 1, y - 1))
        return

    @staticmethod
    def lg_p3870(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3870
        tag: segment_tree|range_reverse|range_sum
        """
        n, m = ac.read_list_ints()
        segment = RangeRevereRangeBitCount(n)

        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 0:
                x, y = lst[1:]
                segment.range_reverse(x - 1, y - 1)
            else:
                x, y = lst[1:]
                ac.st(segment.range_bit_count(x - 1, y - 1))
        return

    @staticmethod
    def lg_p1438(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1438
        tag: diff_array|RangeAddRangeSumMaxMin|segment_tree
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        segment = RangeAddRangeSumMinMax(n)

        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y, k, d = lst[1:]
                if x == y:
                    segment.range_add(x - 1, x - 1, k)
                    if y <= n - 1:
                        segment.range_add(y, y, -k)
                else:
                    segment.range_add(x - 1, x - 1, k)
                    segment.range_add(x, y - 1, d)
                    cnt = y - x
                    if y <= n - 1:
                        segment.range_add(y, y, -cnt * d - k)
            else:
                x = lst[1]
                ac.st(segment.range_sum(0, x - 1) + nums[x - 1])
        return

    @staticmethod
    def lg_p1253(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1253
        tag: range_add|range_change|segment_tree|range_sum
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        tree = RangeSetAddRangeSumMinMax(n, 1 << 32)
        tree.build(nums)
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y, k = lst[1:]
                tree.range_set_add(x - 1, y - 1, (k, 0))
                for i in range(x - 1, y):
                    nums[i] = k
            elif lst[0] == 2:
                x, y, k = lst[1:]
                tree.range_set_add(x - 1, y - 1, (-tree.inf, k))
                for i in range(x - 1, y):
                    nums[i] += k
            else:
                x, y = lst[1:]
                ac.st(tree.range_max(x - 1, y - 1))
        return

    @staticmethod
    def lg_p3373(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3373
        tag: range_add|range_mul|segment_tree|range_sum|RangeAffineRangeSum
        """
        n, q, mod = ac.read_list_ints()
        tree = RangeAffineRangeSum(n, mod)
        nums = ac.read_list_ints()
        tree.build(nums)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y, k = lst[1:]
                tree.range_affine(x - 1, y - 1, k << 32)
            elif lst[0] == 2:
                x, y, k = lst[1:]
                tree.range_affine(x - 1, y - 1, (1 << 32) | k)
            else:
                x, y = lst[1:]
                ans = tree.range_sum(x - 1, y - 1)
                ac.st(ans)
        return

    @staticmethod
    def lg_p4513(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4513
        tag: segment_tree|range_change|range_merge|sub_consequence
        """
        n, m = ac.read_list_ints()
        segment = RangeSetRangeMaxNonEmpConSubSum(n, 1000)
        segment.build([ac.read_int() for _ in range(n)])
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                a, b = lst[1:]
                a, b = ac.min(a, b), ac.max(a, b)
                ans = segment.range_max_non_emp_con_sub_sum(a - 1, b - 1)
                ac.st(ans)
            else:
                a, s = lst[1:]
                segment.point_set(a - 1, s)
        return

    @staticmethod
    def lg_p1471(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1471
        tag: math|segment_tree|RangeAddRangeSum
        """
        n, m = ac.read_list_ints()
        tree = RangeAddRangeAvgDev(n)
        tree.build(ac.read_list_floats())
        for _ in range(m):
            lst = ac.read_list_floats()
            if lst[0] == 1:
                x, y, k = lst[1:]
                x = int(x)
                y = int(y)
                tree.range_add(x - 1, y - 1, k)
            elif lst[0] == 2:
                x, y = lst[1:]
                x = int(x)
                y = int(y)
                ans = tree.range_avg_dev(x - 1, y - 1)[0]
                ac.st("%.4f" % ans)
            else:
                x, y = lst[1:]
                x = int(x)
                y = int(y)
                ans = tree.range_avg_dev(x - 1, y - 1)[1]
                ac.st("%.4f" % ans)
        return

    @staticmethod
    def lg_p6627(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6627
        tag: segment_tree|range_xor|discretization
        """
        n = ac.read_int()
        nums = [ac.read_list_ints() for _ in range(n)]
        nodes = {0, -10 ** 9 - 1, 10 ** 9 + 1}
        for lst in nums:
            for va in lst[1:-1]:
                nodes.add(va)
                nodes.add(va - 1)
                nodes.add(va + 1)
        nodes = sorted(list(nodes))
        n = len(nodes)
        ind = {num: i for i, num in enumerate(nodes)}
        tree = RangeXorUpdateRangeXorQuery(n)
        arr = [0] * n
        for lst in nums:
            if lst[0] == 1:
                a, b, w = lst[1:]
                if a > b:
                    a, b = b, a
                tree.range_xor_update(ind[a], ind[b], w)
            elif lst[0] == 2:
                a, w = lst[1:]
                arr[ind[a]] ^= w
            else:
                a, w = lst[1:]
                tree.range_xor_update(0, n - 1, w)
                arr[ind[a]] ^= w
        ans = inf
        res = -inf
        nums = tree.get()
        for i in range(n):
            val = arr[i] ^ nums[i]
            if val > res or (
                    val == res and (abs(ans) > abs(nodes[i]) or (abs(ans) == abs(nodes[i]) and nodes[i] > ans))):
                res = val
                ans = nodes[i]
        ac.lst([res, ans])
        return

    @staticmethod
    def lg_p6492(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6492
        tag: segment_tree|range_change|range_merge|sub_consequence
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeLongestAlter(n)
        for _ in range(q):
            i = ac.read_int() - 1
            ac.st(tree.point_set_range_longest_alter(i, i))
        return

    @staticmethod
    def lg_p4145(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4145
        tag: math|segment_tree|RangeAddRangeSum
        """
        n = ac.read_int()
        tree = RangeSqrtRangeSum(n)
        tree.build(ac.read_list_ints())
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            a, b = [int(w) - 1 for w in lst[1:]]
            if a > b:
                a, b = b, a
            if lst[0] == 0:
                tree.range_sqrt(a, b)
            else:
                ac.st(tree.range_sum(a, b))
        return

    @staticmethod
    def lc_2940(heights: List[int], queries: List[List[int]]) -> List[int]:
        """
        url: https://leetcode.cn/problems/find-building-where-alice-and-bob-can-meet/
        tag: segment_tree_binary_search|static_range
        """
        n = len(heights)
        tree = RangeAscendRangeMax(n)
        tree.build(heights)
        ans = []
        for ll, rr in queries:
            if ll > rr:
                ll, rr = rr, ll
            if heights[ll] < heights[rr]:
                ans.append(rr)
                continue
            if ll == rr:
                ans.append(ll)
                continue
            if rr == n - 1:
                ans.append(-1)
                continue
            h = heights[ll] if heights[ll] > heights[rr] else heights[rr]
            left = tree.range_max_bisect_left(rr + 1, n - 1, h + 1)
            ans.append(left)
        return ans

    @staticmethod
    def lg_p2574(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2574
        tag: segment_tree|range_reverse|range_sum
        """
        n, m = ac.read_list_ints()
        tree = RangeRevereRangeBitCount(n)
        tree.build([int(w) for w in ac.read_str()])

        for _ in range(m):
            op, left, right = ac.read_list_ints()
            if not op:
                tree.range_reverse(left - 1, right - 1)
            else:
                ac.st(tree.range_bit_count(left - 1, right - 1))
        return

    @staticmethod
    def lg_2572(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2572
        tag: segment_tree|range_reverse|range_sum
        """
        n, m = ac.read_list_ints()
        tree = RangeSetReverseRangeSumLongestConSub(n)
        tree.build(ac.read_list_ints())
        ans = []
        for _ in range(m):
            lst = ac.read_list_ints()
            left, right = lst[1:]
            if left > right:
                left, right = right, left
            if lst[0] <= 2:
                tree.range_change_reverse(left, right, lst[0])
            elif lst[0] == 3:
                ans.append(str(tree.range_sum(left, right)))
            else:
                ans.append(str(tree.range_longest_con_sub(left, right)))
        ac.st("\n".join(ans))
        return

    @staticmethod
    def lg_p1558(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1558
        tag: segment_tree|RangeSetRangeOr
        """
        n, t, q = ac.read_list_ints()
        tree = RangeSetRangeOr(n)
        tree.range_set(0, n - 1, 1)
        for _ in range(q):
            lst = ac.read_list_strs()
            if lst[0] == "C":
                a, b, c = [int(w) for w in lst[1:]]
                if a > b:
                    a, b = b, a
                tree.range_set(a - 1, b - 1, 1 << (c - 1))
            else:
                a, b = [int(w) for w in lst[1:]]
                if a > b:
                    a, b = b, a
                ac.st(bin(tree.range_or(a - 1, b - 1)).count("1"))
        return

    @staticmethod
    def lg_p3740(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3740
        tag: discretization|segment_tree|RangeChangeRangeSum
        """
        n, m = ac.read_list_ints()
        nums = []
        while len(nums) < m * 2:
            nums.extend(ac.read_list_ints())
        nums = [nums[2 * i:2 * i + 2] for i in range(m)]
        nodes = set()
        nodes.add(1)
        nodes.add(n)
        for a, b in nums:
            nodes.add(a)
            nodes.add(b)
            nodes.add(b + 1)
        nodes = list(sorted(nodes))
        ind = {num: i for i, num in enumerate(nodes)}

        n = len(nodes)
        tree = RangeSetRangeSumMinMax(n)
        tree.build([0] * n)
        for i in range(m):
            a, b = nums[i]
            tree.range_set(ind[a], ind[b], i + 1)

        ans = tree.get()
        ac.st(len(set(c for c in ans if c)))
        return

    @staticmethod
    def lg_p4588(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4588
        tag: segment_tree|PointSetRangeComposite
        """
        for _ in range(ac.read_int()):
            n, mod = ac.read_list_ints()
            m = 32
            tree = PointSetRangeComposite(n, mod, m)
            tree.build([1 << m for _ in range(n)])
            for i in range(n):
                op, x = ac.read_list_ints()
                if op == 1:
                    tree.point_set(i, i, x << m)
                else:
                    tree.point_set(x - 1, x - 1, 1 << m)
                val = tree.range_composite(0, n - 1)
                ac.st((val >> m) % mod)
        return

    @staticmethod
    def lg_p8081(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8081
        tag: diff_array|counter|action_scop|segment_tree|RangeSetRangeOr
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        tree = RangeSetRangeSumMinMax(n)
        pre = 0
        ceil = 0
        for i in range(n):
            if nums[i] < 0:
                pre += 1
            else:
                if pre:
                    ceil = max(ceil, pre)
                    low, high = i - 3 * pre, i - pre - 1
                    if high >= 0:
                        tree.range_set(ac.max(0, low), high, 1)
                pre = 0
        if pre:
            ceil = max(ceil, pre)
            low, high = n - 3 * pre, n - pre - 1
            if high >= 0:
                tree.range_set(ac.max(0, low), high, 1)

        ans = tree.range_sum(0, n - 1)
        pre = 0
        res = 0
        for i in range(n):
            if nums[i] < 0:
                pre += 1
            else:
                if pre == ceil:
                    low, high = i - 4 * pre, i - 3 * pre - 1
                    low = ac.max(low, 0)
                    if low <= high:
                        res = ac.max(res, high - low + 1 - tree.range_sum(low, high))
                pre = 0
        if pre == ceil:
            low, high = n - 4 * pre, n - 3 * pre - 1
            low = ac.max(low, 0)
            if low <= high:
                res = ac.max(res, high - low + 1 - tree.range_sum(low, high))
        ac.st(ans + res)
        return

    @staticmethod
    def lg_p8812(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8812
        tag: segment_tree|RangeDescendRangeMin|discretization
        """
        n, m = ac.read_list_ints()
        goods = [[] for _ in range(n)]
        for _ in range(m):
            s, t, p, c = ac.read_list_ints()
            for _ in range(c):
                a, b = ac.read_list_ints()
                a -= 1
                goods[a].append([1, 10 ** 9 + 1, b])
                b = b * p // 100
                goods[a].append([s, t, b])

        for i in range(n):
            nodes = {0, 10 ** 9 + 1}
            for s, t, _ in goods[i]:
                nodes.add(s - 1)
                nodes.add(s)
                nodes.add(t)
                nodes.add(t + 1)
            nodes = sorted(list(nodes))
            ind = {node: i for i, node in enumerate(nodes)}
            k = len(ind)
            tree = RangeDescendRangeMin(k)
            for s, t, b in goods[i]:
                tree.range_descend(ind[s], ind[t], b)
            res = []
            for x in range(k):
                val = tree.range_min(x, x)
                if val == inf:
                    continue
                if not res or res[-1][2] != val:
                    res.append([nodes[x], nodes[x], val])
                else:
                    res[-1][1] = nodes[x]

            goods[i] = [r[:] for r in res]

        nodes = {0, 10 ** 9 + 1}
        for i in range(n):
            for s, t, _ in goods[i]:
                nodes.add(s)
                nodes.add(t)
        nodes = sorted(list(nodes))
        ind = {node: i for i, node in enumerate(nodes)}
        k = len(ind)
        diff = [0] * k
        for i in range(n):
            for s, t, b in goods[i]:
                diff[ind[s]] += b
                if ind[t] + 1 < k:
                    diff[ind[t] + 1] -= b
        diff = ac.accumulate(diff)[2:]
        ac.st(min(diff))
        return

    @staticmethod
    def cf_482b(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/482/B
        tag: segment_tree|RangeOrRangeAnd
        """
        n, m = ac.read_list_ints()
        tree = RangeOrRangeAnd(n)
        nums = [ac.read_list_ints_minus_one() for _ in range(m)]
        for a, b, c in nums:
            if c != -1:
                tree.range_or(a, b, c + 1)
        if all(tree.range_and(a, b) == c + 1 for a, b, c in nums):
            ac.st("YES")
            ac.lst(tree.get())
        else:
            ac.st("NO")
        return

    @staticmethod
    def cf_987c(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/987/C
        tag: brute_force|segment_tree|prefix_suffix
        """
        n = ac.read_int()
        s = ac.read_list_ints()
        c = ac.read_list_ints()
        ind = {num: i for i, num in enumerate(sorted(list(set(s + c + [0] + [10 ** 9 + 1]))))}
        m = len(ind)
        post = [inf] * n
        tree = RangeDescendRangeMin(m)
        for i in range(n - 1, -1, -1):
            tree.range_descend(ind[s[i]], ind[s[i]], c[i])
            post[i] = tree.range_min(ind[s[i]] + 1, m - 1)

        ans = inf
        tree = RangeDescendRangeMin(m)
        for i in range(n):
            if 1 <= i <= n - 2:
                cur = c[i] + tree.range_min(0, ind[s[i]] - 1) + post[i]
                ans = ac.min(ans, cur)
            tree.range_descend(ind[s[i]], ind[s[i]], c[i])
        ac.st(ans if ans < inf else -1)
        return

    @staticmethod
    def lc_1851(intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        url: https://leetcode.cn/problems/minimum-interval-to-include-each-query/
        tag: segment_tree|RangeChangeRangeMin|offline_query|monotonic_queue
        """
        port = []
        for inter in intervals:
            port.extend(inter)
        port.extend(queries)
        lst = sorted(list(set(port)))

        ind = {num: i for i, num in enumerate(lst)}
        ceil = len(lst)
        tree = RangeDescendRangeMin(ceil)
        for a, b in intervals:
            tree.range_descend(ind[a], ind[b], b - a + 1)
        ans = [tree.range_min(ind[num], ind[num]) for num in queries]
        return [x if x != inf else -1 for x in ans]

    @staticmethod
    def lc_1340(nums: List[int], d: int) -> int:
        """
        url: https://leetcode.cn/problems/jump-game-v/
        tag: segment_tree|linear_dp
        """
        n = len(nums)
        post = [n - 1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                post[stack.pop()] = i - 1
            stack.append(i)

        pre = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                pre[stack.pop()] = i + 1
            stack.append(i)

        dct = defaultdict(list)
        for i, num in enumerate(nums):
            dct[num].append(i)
        tree = RangeAscendRangeMax(n)
        tree.build([0] * n)
        for num in sorted(dct):
            cur = []
            for i in dct[num]:
                left, right = pre[i], post[i]
                if left < i - d:
                    left = i - d
                if right > i + d:
                    right = i + d
                x = tree.range_max(left, right)
                cur.append([x + 1, i])

            for x, i in cur:
                tree.range_ascend(i, i, x)
        return tree.range_max(0, n - 1)

    @staticmethod
    def abc_332f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc332/tasks/abc332_f
        tag: RangeAffineRangeSum
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        mod = 998244353
        tree = RangeAffineRangeSum(n, mod)
        tree.build(nums)
        for _ in range(m):
            ll, rr, xx = ac.read_list_ints()
            length = rr - ll + 1
            mul = ((length - 1) * pow(length, -1, mod)) % mod
            add = (xx * pow(length, -1, mod)) % mod
            tree.range_affine(ll - 1, rr - 1, (mul << 32) | add)
        ac.lst(tree.get())
        return

    @staticmethod
    def ac_3805(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/3808/
        tag: RangeAddRangeMin
        """
        n = ac.read_int()
        tree = RangeAddRangeSumMinMax(n)
        tree.build(ac.read_list_ints())
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if len(lst) == 2:
                ll, r = lst
                if ll <= r:
                    ac.st(tree.range_min(ll, r))
                else:
                    ans1 = tree.range_min(ll, n - 1)
                    ans2 = tree.range_min(0, r)
                    ac.st(ac.min(ans1, ans2))
            else:
                ll, r, d = lst
                if ll <= r:
                    tree.range_add(ll, r, d)
                else:
                    tree.range_add(ll, n - 1, d)
                    tree.range_add(0, r, d)
        return

    @staticmethod
    def ac_5037_1(ac=FastIO()):

        n = ac.read_int()
        nums = ac.read_list_ints()
        tree = [RangeRevereRangeBitCount(n) for _ in range(22)]
        for j in range(22):
            lst = [1 if nums[i] & (1 << j) else 0 for i in range(n)]
            tree[j].build(lst)
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr = lst[1:]
                ll -= 1
                rr -= 1
                ans = sum((1 << j) * tree[j].range_bit_count(ll, rr) for j in range(22))
                ac.st(ans)
            else:
                ll, rr, xx = lst[1:]
                ll -= 1
                rr -= 1
                for j in range(22):
                    if (1 << j) & xx:
                        tree[j].range_reverse(ll, rr)

        return

    @staticmethod
    def lc_2276_1():
        """
        url: https://leetcode.cn/problems/count-integers-in-intervals/
        tag: dynamic_segment_tree|union_find_range|SortedList
        """

        class CountIntervals:
            def __init__(self):
                self.n = 10 ** 9 + 7
                self.segment_tree = RangeSetRangeSumMinMaxDynamic(self.n)

            def add(self, left: int, right: int) -> None:
                self.segment_tree.range_set(left, right, 1)

            def count(self) -> int:
                return self.segment_tree.cover[1]

        return CountIntervals

    @staticmethod
    def lc_2276_2():
        """
        url: https://leetcode.cn/problems/count-integers-in-intervals/
        tag: dynamic_segment_tree|union_find_range|SortedList
        """

        class CountIntervals:

            def __init__(self):
                self.lst = SortedList()
                self.cover = 0

            def add(self, left: int, right: int) -> None:
                x = self.lst.bisect_left((left, left))
                if x - 1 >= 0 and self.lst[x - 1][1] >= left:
                    x -= 1

                while 0 <= x < len(self.lst) and not (self.lst[x][0] > right or self.lst[x][1] < left):
                    a, b = self.lst.pop(x)
                    left = left if left < a else a
                    right = right if right > b else b
                    self.cover -= b - a + 1
                self.cover += right - left + 1
                self.lst.add((left, right))

            def count(self) -> int:
                return self.cover

        return CountIntervals

    @staticmethod
    def lc_2286():
        """
        url: https://leetcode.cn/problems/booking-concert-tickets-in-groups/
        tag: segment_tree|RangeAddRangeSumMaxMin
        """

        class BookMyShow:

            def __init__(self, n: int, m: int):
                self.n = n
                self.m = m
                self.tree = RangeAddRangeSumMinMax(n)
                self.cnt = [0] * n
                self.null = SortedList(list(range(n)))

            def gather(self, k: int, max_row: int) -> List[int]:
                max_row += 1
                low = self.tree.range_min(0, max_row - 1)
                if self.m - low < k:
                    return []

                y = self.tree.range_min_bisect_left(self.m - k)
                self.cnt[y] += k
                self.tree.range_add(y, y, k)
                if self.cnt[y] == self.m:
                    self.null.discard(y)
                return [y, self.cnt[y] - k]

            def scatter(self, k: int, max_row: int) -> bool:
                max_row += 1
                s = self.tree.range_sum(0, max_row - 1)
                if self.m * max_row - s < k:
                    return False
                while k:
                    x = self.null[0]
                    rest = k if k < self.m - self.cnt[x] else self.m - self.cnt[x]
                    k -= rest
                    self.cnt[x] += rest
                    self.tree.range_add(x, x, rest)
                    if self.cnt[x] == self.m:
                        self.null.pop(0)
                return True

        return BookMyShow

    @staticmethod
    def lc_3003(s: str, k: int) -> int:
        """
        url: https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations
        tag: segment_tree|bisect_left|range_or|point_set
        """
        n = len(s)
        s = [ord(w) - ord("a") for w in s]
        tree = PointSetRangeOr(n)
        tree.build([1 << w for w in s])

        pre_ind = [-1] * n
        pre_cnt = [0] * n
        ind = [-1]
        pre = set()
        for i in range(n):
            pre_ind[i] = ind[-1]
            pre_cnt[i] = len(ind) - 1
            if s[i] not in pre and len(pre) == k:
                ind.append(i - 1)
                pre = set()
            pre.add(s[i])
        ind.append(n - 1)

        post_cnt = [0] * (n + 1)
        post = dict()
        j = n - 1
        for i in range(n - 1, -1, -1):
            post[s[i]] = post.get(s[i], 0) + 1
            while len(post) > k:
                post[s[j]] -= 1
                if not post[s[j]]:
                    post.pop(s[j])
                j -= 1
            post_cnt[i] = post_cnt[j + 1] + 1

        ans = post_cnt[0]
        for i in range(n):
            xx = s[i]
            for j in range(26):
                if j == xx or (i + 1 < n and s[i + 1] == j) or (i and s[i - 1] == j):
                    continue
                tree.point_set(i, 1 << j)
                cur_ind = pre_ind[i] + 1
                cur = pre_cnt[i]
                while cur_ind <= i:
                    jj = tree.range_or_bisect_right(cur_ind, n - 1, k)
                    cur += 1
                    cur_ind = jj + 1
                cur += post_cnt[cur_ind]
                if cur > ans:
                    ans = cur
            tree.point_set(i, 1 << xx)
        return ans

    @staticmethod
    def library_check_4(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/A
        tag: segment_tree|point_set|range_sum
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeSum(n)
        tree.build(ac.read_list_ints())
        for _ in range(q):
            op, x, y = ac.read_list_ints()
            if op == 1:
                tree.point_set(x, y)
            else:
                ans = tree.range_sum(x, y - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_5(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/B
        tag: segment_tree|point_set|range_min
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMin(n, inf)
        tree.build(ac.read_list_ints())
        for _ in range(q):
            op, x, y = ac.read_list_ints()
            if op == 1:
                tree.point_set(x, y)
            else:
                ans = tree.range_min(x, y - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_6(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/1/practice/contest/273169/problem/C
        tag: segment_tree|point_set|range_min_count
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMinCount(n, 0)
        nums = ac.read_list_ints()
        tree.build(nums)
        ac.get_random_seed()
        for _ in range(q):
            op, x, y = ac.read_list_ints()
            if op == 1:
                tree.point_set(x, y)
            else:
                ans = tree.range_min_count(x, y - 1)
                ac.lst(ans)
        return

    @staticmethod
    def library_check_7(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/A
        tag: segment_tree|point_set|range_max_sub_sum
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMaxSubSum(n, 0)
        nums = ac.read_list_ints()
        tree.build(nums)
        ans = tree.cover[1]
        ac.st(ac.max(ans, 0))
        for _ in range(q):
            x, y = ac.read_list_ints()
            ans = tree.point_set_range_max_sub_sum(x, y)
            ac.st(ac.max(ans, 0))
        return

    @staticmethod
    def library_check_8(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/B
        tag: segment_tree|point_set|range_sum_bisect_left
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeSum(n, 0)
        nums = ac.read_list_ints()
        tree.build(nums)
        for _ in range(q):
            x, y = ac.read_list_ints()
            if x == 1:
                nums[y] = 1 - nums[y]
                tree.point_set(y, nums[y])
            else:
                ans = tree.range_sum_bisect_left(y + 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_9(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/C
        tag: segment_tree|point_set|range_max_bisect_left
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMax(n, 0)
        tree.build(ac.read_list_ints())

        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                i, v = lst[1:]
                tree.point_set(i, v)
            else:
                x = lst[1]
                ans = tree.range_max_bisect_left(0, n - 1, x) if tree.cover[1] >= x else -1
                ac.st(ans)
        return

    @staticmethod
    def library_check_10(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/2/practice/contest/273278/problem/D
        tag: segment_tree|point_set|range_max_bisect_left
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMax(n)
        tree.build(ac.read_list_ints())
        for _ in range(q):
            op, x, y = ac.read_list_ints()
            if op == 1:
                tree.point_set(x, y)
            else:
                ans = tree.range_max_bisect_left(y, n - 1, x)
                ac.st(ans)
        return

    @staticmethod
    def library_check_11(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/A
        tag: segment_tree|point_set|range_sum|inversion
        """
        n = ac.read_int()
        tree = PointSetRangeSum(n, 0)
        nums = ac.read_list_ints_minus_one()
        ans = [0] * n
        for j in range(n):
            i = nums[j]
            ans[j] = tree.range_sum(i, n - 1)
            tree.point_set(i, 1)
        ac.lst(ans)
        return

    @staticmethod
    def library_check_12(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/B
        tag: segment_tree|point_set|range_sum|inversion|bisect_left
        """
        n = ac.read_int()
        tree = PointSetRangeSum(n, 0)
        tree.build([1] * n)
        nums = ac.read_list_ints()
        ans = [0] * n
        for j in range(n - 1, -1, -1):
            i = nums[j]
            ans[j] = tree.range_sum_bisect_left(tree.cover[1] - i) + 1
            tree.point_set(ans[j] - 1, 0)
        ac.lst(ans)
        return

    @staticmethod
    def library_check_13(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/C
        tag: segment_tree|point_set|range_sum|range_include
        """
        n = ac.read_int()
        nums = ac.read_list_ints_minus_one()
        tree = PointSetRangeSum(2 * n, 0)
        ans = [0] * n
        pre = [-1] * n
        for j in range(2 * n):
            i = nums[j]
            if pre[i] == -1:
                pre[i] = j
                continue
            ans[i] = tree.range_sum(pre[i], j)
            tree.point_set(pre[i], 1)
        ac.lst(ans)
        return

    @staticmethod
    def library_check_14(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/D
        tag: segment_tree|point_set|range_sum|range_include|reverse_thinking|include_exclude
        """
        n = ac.read_int()
        nums = ac.read_list_ints_minus_one()
        tree = PointSetRangeSum(2 * n, 0)
        ans = [0] * n
        pre = [-1] * n
        for j in range(2 * n):
            i = nums[j]
            if pre[i] == -1:
                pre[i] = j
                continue
            ans[i] = (j - pre[i] - 1) - 2 * tree.range_sum(pre[i], j)
            tree.point_set(pre[i], 1)
        ac.lst(ans)
        return

    @staticmethod
    def library_check_15(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/E
        tag: segment_tree|range_add|point_get
        """
        """
        url: https://codeforces.com/edu/course/2/lesson/4/3/practice/contest/274545/problem/E
        tag: segment_tree|range_add|point_get
        """
        n, q = ac.read_list_ints()
        tree = RangeAddPointGet(n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, vv = lst[1:]
                tree.range_add(ll, rr - 1, vv)
            else:
                ans = tree.point_get(lst[1])
                ac.st(ans)
        return

    @staticmethod
    def library_check_16(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/A
        tag: segment_tree|point_set|range_sum
        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        odd = PointSetRangeSum(n)
        lst = [nums[i] if i % 2 else 0 for i in range(n)]
        odd.build(lst)

        even = PointSetRangeSum(n)
        lst = [nums[i] if i % 2 == 0 else 0 for i in range(n)]
        even.build(lst)

        for _ in range(ac.read_int()):
            op, x, y = ac.read_list_ints()
            if op == 0:
                if (x - 1) % 2:
                    odd.point_set(x - 1, y)
                else:
                    even.point_set(x - 1, y)
            else:
                odd_sum = odd.range_sum(x - 1, y - 1)
                even_sum = even.range_sum(x - 1, y - 1)
                ans = odd_sum - even_sum if (x - 1) % 2 else even_sum - odd_sum
                ac.st(ans)
        return

    @staticmethod
    def library_check_17(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/B
        tag: segment_tree|matrix_build|range_mul
        """
        r, n, m = ac.read_list_ints()
        nums = []
        for _ in range(n):
            for _ in range(2):
                nums.extend(ac.read_list_ints())
            ac.read_str()

        tree = MatrixBuildRangeMul(n, 0, r)
        tree.matrix_build(nums)

        for _ in range(m):
            ll, rr = ac.read_list_ints_minus_one()
            ans = tree.range_mul(ll, rr)
            ac.lst((ans[0], ans[1]))
            ac.lst((ans[2], ans[3]))
            ac.st("")
        return

    @staticmethod
    def library_check_18(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/C
        tag: segment_tree|point_set|range_inverse
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeInversion(n, 40)
        tree.build(ac.read_list_ints_minus_one())

        for _ in range(q):
            op, x, y = ac.read_list_ints_minus_one()
            if op == 0:
                ans = tree.range_inverse(x, y)
                ac.st(ans)
            else:
                tree.point_set(x, y)
        return

    @staticmethod
    def library_check_19(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/D
        tag: segment_tree|point_set|range_or
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeOr(n)
        tree.build([1 << x for x in ac.read_list_ints_minus_one()])

        for _ in range(q):
            op, x, y = ac.read_list_ints_minus_one()
            if op == 0:
                ans = tree.range_or(x, y)
                ac.st(bin(ans).count("1"))
            else:
                tree.point_set(x, x, 1 << y)
        return

    @staticmethod
    def library_check_20(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A
        tag: segment_tree|range_add|point_get
        """
        n, q = ac.read_list_ints()
        tree = RangeAddPointGet(n)

        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_add(ll, rr - 1, v)
            else:
                ans = tree.point_get(lst[1])
                ac.st(ans)
        return

    @staticmethod
    def library_check_21(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A
        tag: segment_tree|range_ascend|point_get
        """
        n, q = ac.read_list_ints()
        tree = RangeAscendPointGet(n)

        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_ascend(ll, rr - 1, v)
            else:
                ans = tree.point_get(lst[1])
                ac.st(ans)
        return

    @staticmethod
    def library_check_22(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/1/practice/contest/279634/problem/A
        tag: segment_tree|range_set|point_get
        """
        n, q = ac.read_list_ints()
        tree = RangeSetPointGet(n)
        tree.build([0] * n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_set(ll, rr - 1, v)
            else:
                ans = tree.point_get(lst[1])
                ac.st(ans)
        return

    @staticmethod
    def library_check_23(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/4/4/practice/contest/274684/problem/E
        tag: segment_tree|bisect_left|brute_force|classical|range_min|point_set
        """
        n, q = ac.read_list_ints()
        tree = PointSetRangeMin(n, inf)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                i, h = lst[1:]
                tree.point_set(i, h)
            else:
                ll, rr, p = lst[1:]
                ans = 0
                while ll <= rr - 1:
                    x = tree.range_min_bisect_left(ll, rr - 1, p)
                    if x == -1:
                        break
                    ll = x
                    tree.point_set(ll, inf)
                    ans += 1
                ac.st(ans)
        return

    @staticmethod
    def library_check_24(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/A
        tag: segment_tree|range_add|range_min
        """
        n, q = ac.read_list_ints()
        tree = RangeAddRangeSumMinMax(n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_add(ll, rr - 1, v)
            else:
                ll, rr = lst[1:]
                ans = tree.range_min(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_25(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/B
        tag: segment_tree|range_affine|range_sum
        """
        n, q = ac.read_list_ints()
        mod = 10 ** 9 + 7
        tree = RangeAffineRangeSum(n, mod)
        tree.build([1] * n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, b = lst[1:]
                tree.range_affine(ll, rr - 1, (b << 32))
            else:
                ll, rr = lst[1:]
                ans = tree.range_sum(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_26(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/C
        tag: segment_tree|range_or|range_and
        """
        n, q = ac.read_list_ints()
        tree = RangeOrRangeAnd(n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, b = lst[1:]
                tree.range_or(ll, rr - 1, b)
            else:
                ll, rr = lst[1:]
                ans = tree.range_and(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_27(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/D
        tag: segment_tree|range_add|range_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeAddRangeSumMinMax(n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, b = lst[1:]
                tree.range_add(ll, rr - 1, b)
            else:
                ll, rr = lst[1:]
                ans = tree.range_sum(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_28(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/E
        tag: segment_tree|range_set|range_min
        """
        n, q = ac.read_list_ints()
        tree = RangeSetRangeSumMinMax(n)
        tree.build([0] * n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, b = lst[1:]
                tree.range_set(ll, rr - 1, b)
            else:
                ll, rr = lst[1:]
                ans = tree.range_min(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_29(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/2/practice/contest/279653/problem/F
        tag: segment_tree|range_set|range_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeSetRangeSumMinMax(n)
        tree.build([0] * n)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, b = lst[1:]
                tree.range_set(ll, rr - 1, b)
            else:
                ll, rr = lst[1:]
                ans = tree.range_sum(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_30(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/A
        tag: segment_tree|range_set|range_max_non_emp_con_sub_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeSetRangeMaxNonEmpConSubSum(n)
        tree.build([0] * n)
        for _ in range(q):
            ll, rr, v = ac.read_list_ints()
            tree.range_set(ll, rr - 1, v)
            ans = ac.max(tree.cover[1], 0)
            ac.st(ans)
        return

    @staticmethod
    def library_check_31(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/B
        tag: segment_tree|range_reverse|range_bit_count_bisect_left
        """
        n, m = ac.read_list_ints()
        tree = RangeRevereRangeBitCount(n)
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr = lst[1:]
                tree.range_reverse(ll, rr - 1)
            else:
                ans = tree.range_bit_count_bisect_left(lst[1] + 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_32(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/3/practice/contest/280799/problem/C
        tag: segment_tree|range_add|range_max|bisect_left
        """
        n, m = ac.read_list_ints()
        tree = RangeAddRangeSumMinMax(n)
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_add(ll, rr - 1, v)
            else:
                x, ll = lst[1:]
                ans = tree.range_max_bisect_left(ll, n - 1, x)
                ac.st(ans)
        return

    @staticmethod
    def library_check_33(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/A
        tag: segment_tree|range_change_add|range_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeSetAddRangeSumMinMax(n, 1)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, v = lst[1:]
                tree.range_set_add(ll, rr - 1, (v, 0))
            elif lst[0] == 2:
                ll, rr, v = lst[1:]
                tree.range_set_add(ll, rr - 1, (-tree.initial, v))
            else:
                ll, rr = lst[1:]
                ans = tree.range_sum(ll, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_34(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/B
        tag: segment_tree|diff_array|range_add|point_get|range_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeAddPointGet(n)
        diff = RangeAddRangeSumMinMax(n + 1)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, a, d = lst[1:]
                tree.range_add(ll - 1, rr - 1, a)
                if ll <= rr - 1:
                    diff.range_add(ll, rr - 1, d)
                    diff.range_add(rr, rr, -d * (rr - ll))
            else:
                ans = diff.range_sum(0, lst[1] - 1) + tree.point_get(lst[1] - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_35(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/C
        tag: segment_tree|range_set|range_seg_count_length
        """
        q = ac.read_int()
        n = 10 ** 6 + 10
        tree = RangeSetRangeSegCountLength(n)
        base = 5 * 10 ** 5
        for _ in range(q):
            lst = ac.read_list_strs()
            ll, d = [int(w) for w in lst[1:]]
            ll += base
            rr = ll + d - 1
            if lst[0] == "W":
                tree.range_set(ll, rr, 0)
            else:
                tree.range_set(ll, rr, 1)
            ac.lst([tree.cover[1], tree.sum[1]])
        return

    @staticmethod
    def library_check_36(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/D
        tag: segment_tree|range_add|range_weighted_sum
        """
        n, q = ac.read_list_ints()
        tree = RangeAddRangeWeightedSum(n)
        tree.build(ac.read_list_ints())
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, d = lst[1:]
                tree.range_add(ll - 1, rr - 1, d)
            else:
                ll, rr = lst[1:]
                ans = tree.range_weighted_sum(ll - 1, rr - 1)
                ac.st(ans)
        return

    @staticmethod
    def library_check_37(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/E
        tag: segment_tree|range_chmin_chmax|point_get
        """
        n, q = ac.read_list_ints()
        tree = RangeChminChmaxPointGet(n, 0, 10 ** 5)
        for _ in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                ll, rr, hh = lst[1:]
                tree.range_chmin_chmax(ll, rr, hh, tree.high_initial)
            else:
                ll, rr, hh = lst[1:]
                tree.range_chmin_chmax(ll, rr, tree.low_initial, hh)
        ans = tree.get()
        ac.st("\n".join(str(x) for x in ans))
        return

    @staticmethod
    def library_check_38(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/5/4/practice/contest/280801/problem/F
        tag: segment_tree_dynamic|range_set|range_sum_bisect_left
        """
        n = ac.read_int()
        tree = RangeSetPreSumMaxDynamicDct(n, 10 ** 5, -1 << 32)
        while True:
            lst = ac.read_list_strs()
            if lst[0] == "I":
                ll, rr, hh = [int(w) for w in lst[1:]]
                tree.range_set(ll - 1, rr - 1, hh)
            elif lst[0] == "Q":
                hh = int(lst[1])
                ans = tree.range_pre_sum_max_bisect_left(hh)
                ac.st(ans)
            else:
                break
        return

    @staticmethod
    def abc_287g(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc287/tasks/abc287_g
        tag: segment_tree|range_sum|dynamic|offline
        """
        n = ac.read_int()
        nums = [ac.read_list_ints() for _ in range(n)]
        q = ac.read_int()
        queries = [ac.read_list_ints() for _ in range(q)]
        nodes = set()
        for a, _ in nums:
            nodes.add(a)
        for lst in queries:
            if lst[0] == 1:
                nodes.add(lst[2])
        nodes = sorted(nodes)
        ind = {num: i for i, num in enumerate(nodes)}
        n = len(nodes)
        tree = PointAddRangeSum1Sum2(n)
        for a, b in nums:
            tree.point_add(ind[a], (b, a * b))
        for lst in queries:
            if lst[0] == 1:
                x, y = lst[1:]
                x -= 1
                a, b = nums[x]
                tree.point_add(ind[a], (-b, -b * a))
                nums[x][0] = y
                a, b = nums[x]
                tree.point_add(ind[a], (b, b * a))
            elif lst[0] == 2:
                x, y = lst[1:]
                x -= 1
                a, b = nums[x]
                tree.point_add(ind[a], (-b, -b * a))
                nums[x][1] = y
                a, b = nums[x]
                tree.point_add(ind[a], (b, b * a))
            else:
                x = lst[1]
                tot = tree.cover1[1]
                if tot < x:
                    ac.st(-1)
                else:
                    rest, c, i = tree.range_sum2_bisect_left(tot - x)
                    rest += c * nodes[i]
                    ac.st(tree.cover2[1] - rest)
        return
