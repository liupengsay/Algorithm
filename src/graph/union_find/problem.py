"""

Algorithm：union_find|persistent_union_find|permutation_circle
Description：graph|reverse_thinking|permutation_circle|offline_query|merge_wise|root_wise

====================================LeetCode====================================
765（https://leetcode.cn/problems/couples-holding-hands/）union_find
1697（https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/）sort|offline_query|implemention
2503（https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/）sort|offline_query|implemention
2421（https://leetcode.cn/problems/number-of-good-paths/）sort|union_find|counter
2382（https://leetcode.cn/problems/maximum-segment-sum-after-removals/）reverse_order|union_find|implemention|reverse_thinking
2334（https://leetcode.cn/problems/subarray-with-elements-greater-than-varying-threshold/）sort|brute_force|union_find
2158（https://leetcode.cn/problems/amount-of-new-area-painted-each-day/）union_left
2157（https://leetcode.cn/problems/groups-of-strings/）alphabet|brute_force
2076（https://leetcode.cn/problems/process-restricted-friend-requests/）union_find|reverse_thinking
2459（https://leetcode.cn/problems/sort-array-by-moving-items-to-empty-space/）permutation_circle
2709（https://leetcode.cn/problems/greatest-common-divisor-traversal/）union_find|prime_factorization
2612（https://leetcode.cn/problems/minimum-reverse-operations/）union_find|find_range_merge_to_disjoint
1559（https://leetcode.cn/problems/detect-cycles-in-2d-grid/）union_find|circle_judge|classical
1970（https://leetcode.cn/problems/last-day-where-you-can-still-cross/）reverse_thinking|union_find
1998（https://leetcode.cn/problems/gcd-sort-of-an-array/）union_find|prime_factorization
2158（https://leetcode.cn/problems/amount-of-new-area-painted-each-day/）union_find_range|union_left|union_find_right_root
2471（https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/）discretization|permutation_circle
945（https://leetcode.cn/problems/minimum-increment-to-make-array-unique/description/）union_find_right_root|greedy
947（https://leetcode.cn/contest/weekly-contest-112/problems/most-stones-removed-with-same-row-or-column/）brain_teaser|union_find
547（https://leetcode.cn/problems/number-of-provinces/description/）union_find
684（https://leetcode.cn/problems/redundant-connection/description/）union_find
1562（https://leetcode.cn/problems/find-latest-group-of-size-m/description/）union_find|sorted_list
407（https://leetcode-cn.com/problems/trapping-rain-water-ii/）union_find|classical
1632（https://leetcode.cn/problems/rank-transform-of-a-matrix/）union_find|matrix_rank|row_column_union_find
100376（https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-ii/）build_graph|union_find|union_right
685（https://leetcode.cn/problems/redundant-connection-ii/）union_find|directed_graph|in_degree|circle_based_tree|classical

=====================================LuoGu======================================
P3367（https://www.luogu.com.cn/problem/P3367）connected_part|counter|union_find
P5836（https://www.luogu.com.cn/problem/P5836）union_find|several_union_find
P3144（https://www.luogu.com.cn/problem/P3144）reverse_order|union_find|connected_part|counter
P5836（https://www.luogu.com.cn/problem/P5836）union_find|several_union_find
P5877（https://www.luogu.com.cn/problem/P5877）union_find|implemention|counter
P6111（https://www.luogu.com.cn/problem/P6111）union_find|offline_query
P6121（https://www.luogu.com.cn/problem/P6121）reverse_order|union_find|size
P6153（https://www.luogu.com.cn/problem/P6153）union_find|greedy|classical
P1955（https://www.luogu.com.cn/problem/P1955）union_find
P1196（https://www.luogu.com.cn/problem/P1196）union_find_weighted
P1197（https://www.luogu.com.cn/problem/P1197）reverse_order|union_find|reverse_order|brute_force|part
P1522（https://www.luogu.com.cn/problem/P1522）connected_part|brute_force|high_precision|tree_diameter
P1621（https://www.luogu.com.cn/problem/P1621）euler_series|O(nlogn)|prime_factorization
P1892（https://www.luogu.com.cn/problem/P1892）union_find|bipartite_graph
P2189（https://www.luogu.com.cn/problem/P2189）union_find
P2307（https://www.luogu.com.cn/problem/P2307）union_find
P3420（https://www.luogu.com.cn/problem/P3420）union_find
P5429（https://www.luogu.com.cn/problem/P5429）union_find
P6004（https://www.luogu.com.cn/problem/P6004）union_find|permutation_circle|kruskal|mst|greedy|pointer
P6193（https://www.luogu.com.cn/problem/P6193）permutation_circle
P6706（https://www.luogu.com.cn/problem/P6706）directed_graph|union_find|reverse_order|find_range_merge_to_disjoint
P7991（https://www.luogu.com.cn/problem/P7991）union_find|shrink_point
P8230（https://www.luogu.com.cn/problem/P8230）layer|union_find|implemention
P8637（https://www.luogu.com.cn/problem/P8637）union_find|permutation_circle
P8686（https://www.luogu.com.cn/problem/P8686）union_find
P8785（https://www.luogu.com.cn/problem/P8785）union_find|counter
P8787（https://www.luogu.com.cn/problem/P8787）greedy|heapq|implemention|union_find
P8881（https://www.luogu.com.cn/problem/P8881）brain_teaser|union_find|circle_judge|part
P5930（https://www.luogu.com.cn/problem/P5930）union_find|classical
P2024（https://www.luogu.com.cn/problem/P2024）union_find_type|build_graph
P3402（https://www.luogu.com.cn/problem/P3402）
P2391（https://www.luogu.com.cn/problem/P2391）union_find_right|reverse_thinking
P1840（https://www.luogu.com.cn/problem/P1840）union_find_right

===================================CodeForces===================================
25D（https://codeforces.com/problemset/problem/25/D）union_find
1810E（https://codeforces.com/contest/1810/problem/E）union_find|heuristic_search|bfs|heapq
920E（https://codeforces.com/contest/920/problem/E）union_find
540C（https://codeforces.com/problemset/problem/540/C）union_find
1800E2（https://codeforces.com/problemset/problem/1800/E2）union_find
1691E（https://codeforces.com/contest/1691/problem/E）union_find_range
827A（https://codeforces.com/problemset/problem/827/A）union_find_right_root|implemention|greedy
1167C（https://codeforces.com/problemset/problem/1167/C）union_find
1411C（https://codeforces.com/contest/1411/problem/C）brain_teaser|classical|hard
1726D（https://codeforces.com/contest/1726/problem/D）union_find|brain_teaser|classical
915F（https://codeforces.com/contest/915/problem/F）union_find|contribution_method|counter
371D（https://codeforces.com/problemset/problem/371/D）union_find_right
292D（https://codeforces.com/problemset/problem/292/D）union_find_right|prefix_suffix
566D（https://codeforces.com/problemset/problem/566/D）union_find_range
1012B（https://codeforces.com/problemset/problem/1012/B）union_find|brain_teaser|classical
650C（https://codeforces.com/problemset/problem/650/C）union_find|matrix_rank|row_column_union_find
1253D（https://codeforces.com/problemset/problem/1253/D）union_find_right
1851G（https://codeforces.com/contest/1851/problem/G）union_find|offline_query|brain_teaser
1609D（https://codeforces.com/problemset/problem/1609/D）union_find|part|sorted_list
1850H（https://codeforces.com/contest/1850/problem/H）union_find_weighted_dis|classical|hard
766D（https://codeforces.com/problemset/problem/766/D）union_find_type|build_graph|bipartite_graph
1594D（https://codeforces.com/contest/1594/problem/D）union_find_type|build_graph|bipartite_graph|2-sat
1290C（https://codeforces.com/problemset/problem/1290/C）
1713E（https://codeforces.com/contest/1713/problem/E）
1788F（https://codeforces.com/problemset/problem/1788/F）
1807C（https://codeforces.com/contest/1807/problem/C）union_find_type
1213G（https://codeforces.com/contest/1213/problem/G）union_find|offline_query|classical
1619G（https://codeforces.com/contest/1619/problem/G）union_find|implemention
1618G（https://codeforces.com/contest/1618/problem/G）union_find_left|union_find_right|classical|offline_query
1941G（https://codeforces.com/contest/1941/problem/G）union_find|build_graph|bfs|brain_teaser|classical
1971G（https://codeforces.com/contest/1971/problem/G）union_find|bit_operation
1383A（https://codeforces.com/problemset/problem/1383/A）build_graph|greedy|implemention|union_find|brain_teaser|observation
1494D（https://codeforces.com/problemset/problem/1494/D）union_right|union_find|implemention|construction
1209D（https://codeforces.com/problemset/problem/1494/D）union_find|brain_teaser
776D（https://codeforces.com/problemset/problem/776/D）union_find|classical|2-sat
1278D（https://codeforces.com/problemset/problem/1278/D）union_find|range|binary_search|observation|partial_order|observation|bucket_sort
1994D（https://codeforces.com/problemset/problem/1994/D）reverse_order|pigeonhole_principle|union_find
2020D（https://codeforces.com/contest/2020/problem/D）union_find|union_right|classical
277A（https://codeforces.com/problemset/problem/277/A）union_find_general
1156D（https://codeforces.com/problemset/problem/1156/D）union_find|brute_force
2033E（https://codeforces.com/contest/2033/problem/E）union_find|permutation_circle|greedy
2020D（https://codeforces.com/contest/2020/problem/D）union_find|union_right
2021E2（https://codeforces.com/contest/2021/problem/E2）tree_dp|bag_dp|union_dp|brain_teaser|classical

====================================AtCoder=====================================
ARC065B（https://atcoder.jp/contests/abc049/tasks/arc065_b）union_find|several_union_find
ABC126E（https://atcoder.jp/contests/abc126/tasks/abc126_e）union_find|several_union_find
ABC131F（https://atcoder.jp/contests/abc131/tasks/abc131_f）brain_teaser|union_find|counter
ARC097B（https://atcoder.jp/contests/arc097/tasks/arc097_b）union_find|permutation_circle
ABC304E（https://atcoder.jp/contests/abc304/tasks/abc304_e）union_find|reverse_thinking
ABC237E（https://atcoder.jp/contests/abc238/tasks/abc238_e）union_find_range|prefix_sum|brain_teaser
ABC279F（https://atcoder.jp/contests/abc279/tasks/abc279_f）union_find_range|brain_teaser|build_graph|classical
ABC214D（https://atcoder.jp/contests/abc214/tasks/abc214_d）union_find|contribution_method|counter
ARC107C（https://www.luogu.com.cn/problem/AT_arc107_c）union_find|comb_perm
ABC328F（https://atcoder.jp/contests/abc328/tasks/abc328_f）union_find_weighted_dis|classical|hard
ABC314F（https://atcoder.jp/contests/abc314/tasks/abc314_f）union_find|bfs|build_graph|expectation|prob
ABC295G（https://atcoder.jp/contests/abc295/tasks/abc295_g）union_find|implemention|tree|union_min|classical
ABC293D（https://atcoder.jp/contests/abc293/tasks/abc293_d）union_find
ABC280F（https://atcoder.jp/contests/abc270/tasks/abc270_f）union_find|build_graph|brute_force|classical
ABC264E（https://atcoder.jp/contests/abc264/tasks/abc264_e）union_right|reverse_order|classical
ABC259D（https://atcoder.jp/contests/abc259/tasks/abc259_d）geometry|union_find|circle_location|classical
ABC350G（https://atcoder.jp/contests/abc350/tasks/abc350_g）implemention|union_find|data_range|heuristic_merge|brain_teaser|classical
ABC350D（https://atcoder.jp/contests/abc350/tasks/abc350_d）union_find|classical
ABC238E（https://atcoder.jp/contests/abc238/tasks/abc238_e）prefix_sum|union_find|classical
ABC229E（https://atcoder.jp/contests/abc229/tasks/abc229_e）reverse_order|union_find|classical
ABC228D（https://atcoder.jp/contests/abc228/tasks/abc228_d）union_find_range|classical|implemention
ABC351D（https://atcoder.jp/contests/abc351/tasks/abc351_d）union_find|bfs|classical
ABC226E（https://atcoder.jp/contests/abc226/tasks/abc226_e）circle_based_tree|union_find|classical
ABC218E（https://atcoder.jp/contests/abc218/tasks/abc218_e）union_find|mst
ABC214E（https://atcoder.jp/contests/abc214/tasks/abc214_e）union_find_right|dict|discretization|implemention|linked_list
ABC355F（https://atcoder.jp/contests/abc355/tasks/abc355_f）union_find|brain_teaser|implemention
ABC372E（https://atcoder.jp/contests/abc372/tasks/abc372_e）heuristic_merge|union_find
ABC183F（https://atcoder.jp/contests/abc183/tasks/abc183_f）heuristic_merge|classical
ABC378F（https://atcoder.jp/contests/abc378/tasks/abc378_f）union_find|brute_force|observation
ABC170F（https://atcoder.jp/contests/abc170/tasks/abc170_f）bfs|union_find|classical
ABC383E（https://atcoder.jp/contests/abc383/tasks/abc383_e）union_find|classical
ABC380E（https://atcoder.jp/contests/abc380/tasks/abc380_e）union_find_range|union_left|union_right|classical

=====================================AcWing=====================================
4309（https://www.acwing.com/problem/content/description/4309/）union_right
4869（https://www.acwing.com/problem/content/description/4869/）union_find|implemention|size
5148（https://www.acwing.com/problem/content/5148/）union_find|circle_judge

================================LibraryChecker================================
1（https://judge.yosupo.jp/problem/cycle_detection_undirected）union_find|circle_judge
2（https://ac.nowcoder.com/acm/contest/7780/C）union_find|circle_judge
3（https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B）union_find_max|union_find_min
4（https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C）union_find|heuristic_merge|classical|hard
5（https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D）union_find|reverse_thinking|classical
6（https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A）union_find_range
7（https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/B）union_find_range
8（https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C）union_find_range
9（https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/D）union_find_weighted_dis|classical|hard
10（https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/J）union_find_type|build_graph


1（https://www.codechef.com/problems/TFALL）union_find_left|union_find_right|brute_force
2786（https://yukicoder.me/problems/no/2786）heuristic_merge|union_find|classical

"""

import decimal
import math
from collections import defaultdict, Counter, deque
from heapq import heappop, heapify, heappush
from typing import List, Optional

from src.basis.tree_node.template import TreeNode
from src.graph.dijkstra.template import WeightedGraphForDijkstra
from src.graph.union_find.template import UnionFind, UnionFindWeighted, UnionFindSP, UnionFindGeneral
from src.math.comb_perm.template import Combinatorics
from src.math.number_theory.template import PrimeSieve
from src.math.prime_factor.template import PrimeFactor
from src.struct.segment_tree.template import RangeDivideRangeSum
from src.struct.sorted_list.template import SortedList
from src.util.fast_io import FastIO


class Solution:
    def __init__(self):
        return

    @staticmethod
    def cf_1810e_1(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1810/problem/E
        tag: cannot_be_union_find|heuristic_search|bfs|heapq|classical|hard
        """
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            nums = ac.read_list_ints()
            edge = [[] for _ in range(n)]
            for _ in range(m):
                u, v = ac.read_list_ints_minus_one()
                edge[u].append(v)
                edge[v].append(u)

            visit = [-1] * n
            ans = "NO"
            for i in range(n):
                if visit[i] == -1 and not nums[i]:
                    count = 0
                    visit[i] = i
                    stack = [(0, i)]
                    while stack:
                        d, x = heappop(stack)
                        if count < nums[x]:
                            break
                        count += 1
                        for j in edge[x]:
                            if visit[j] != i:
                                visit[j] = i
                                heappush(stack, (nums[j], j))
                    if count == n:
                        ans = "YES"
                        break
            ac.st(ans)

        return

    @staticmethod
    def cf_1810e_2(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1810/problem/E
        tag: cannot_be_union_find|heuristic_search|bfs|heapq|classical|hard|mst
        """
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            nums = ac.read_list_ints()
            nums = [num * n + i for i, num in enumerate(nums)]  # classical skills

            edge = [[] for _ in range(n)]
            for _ in range(m):
                u, v = ac.read_list_ints_minus_one()
                if nums[u] < nums[v]:
                    u, v = v, u
                edge[u].append(v)

            reach = [0] * n
            uf = UnionFind(n)
            nums.sort()
            for val in nums:
                num, i = val // n, val % n
                if not num:
                    reach[i] = 1
                for j in edge[i]:
                    if reach[uf.find(j)] and num <= uf.size(j):
                        reach[i] = 1
                    uf.union_left(i, j)
            ac.st("YES" if uf.part == 1 and reach[uf.find(0)] else "NO")
        return

    @staticmethod
    def ac_5148(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/5148/
        tag: union_find|circle_judge
        """
        m, n = ac.read_list_ints()
        grid = [ac.read_str() for _ in range(m)]
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                for x, y in [[i, j + 1], [i + 1, j]]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == grid[i][j]:
                        if not uf.union(i * n + j, x * n + y):
                            ac.yes()
                            return
        ac.no()
        return

    @staticmethod
    def cf_872a(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/827/A
        tag: union_find_right_root|implemention|greedy
        """
        n = ac.read_int()
        nums = [ac.read_list_strs() for _ in range(n)]
        length = max(int(ls[-1]) + len(ls[0]) - 1 for ls in nums)
        uf = UnionFind(length + 1)
        ans = ["a"] * length
        for ls in nums:
            st = ls[0]
            m = len(st)
            for x in ls[2:]:
                x = int(x) - 1
                start = x
                while x <= start + m - 1:
                    x = uf.find(x)
                    if x <= start + m - 1:
                        ans[x] = st[x - start]
                        uf.union_right(x, x + 1)
                    else:
                        break
        ac.st("".join(ans))
        return

    @staticmethod
    def cf_920e(ac=FastIO()):
        """
        url: https://codeforces.com/contest/920/problem/E
        tag: union_find
        """
        n, m = ac.read_list_ints()
        edge = set()
        for _ in range(m):
            u, v = ac.read_list_ints_minus_one()
            edge.add((u, v))

        ans = []
        not_visit = set(range(n))
        while not_visit:
            i = next(iter(not_visit))
            not_visit.discard(i)
            stack = [i]
            cnt = 1
            while stack:
                u = stack.pop()
                visit = []
                for v in not_visit:
                    if (u, v) in edge or (v, u) in edge:
                        continue
                    cnt += 1
                    stack.append(v)
                    visit.append(v)
                for v in visit:
                    not_visit.discard(v)
            ans.append(cnt)
        ans.sort()
        ac.st(len(ans))
        ac.lst(ans)
        return

    @staticmethod
    def lc_1697(n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        url: https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/
        tag: sort|offline_query|implemention|classical
        """
        m = len(queries)
        ind = list(range(m))
        ind.sort(key=lambda x: queries[x][2])

        edge_list.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        i = 0
        k = len(edge_list)
        ans = []
        for j in ind:
            p, q, limit = queries[j]
            while i < k and edge_list[i][2] < limit:
                uf.union(edge_list[i][0], edge_list[i][1])
                i += 1
            ans.append([j, uf.is_connected(p, q)])

        ans.sort(key=lambda x: x[0])
        return [an[1] for an in ans]

    @staticmethod
    def lc_2503(grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        url: https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/
        tag: sort|offline_query|implemention
        """
        dct = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    x, y = grid[i][j], grid[i + 1][j]
                    dct.append([i * n + j, i * n + n + j, x if x > y else y])
                if j + 1 < n:
                    x, y = grid[i][j], grid[i][j + 1]
                    dct.append([i * n + j, i * n + 1 + j, x if x > y else y])
        dct.sort(key=lambda d: d[2])
        uf = UnionFind(m * n)
        k = len(queries)
        ind = list(range(k))
        ind.sort(key=lambda d: queries[d])

        ans = [0] * k
        j = 0
        length = len(dct)
        for i in ind:
            cur = queries[i]
            while j < length and dct[j][2] < cur:
                uf.union(dct[j][0], dct[j][1])
                j += 1
            if cur > grid[0][0]:
                ans[i] = uf.size(0)
        return ans

    @staticmethod
    def lc_2421(vals: List[int], edges: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/problems/number-of-good-paths/
        tag: sort|union_find|counter|classical|discretization
        """
        n = len(vals)
        index = defaultdict(list)
        for i in range(n):
            index[vals[i]].append(i)
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        uf = UnionFind(n)
        i = 0
        m = len(edges)
        ans = 0
        for val in sorted(index):
            while i < m and vals[edges[i][0]] <= val and vals[edges[i][1]] <= val:
                uf.union(edges[i][0], edges[i][1])
                i += 1
            cnt = Counter(uf.find(x) for x in index[val])
            for w in cnt.values():
                ans += w * (w - 1) // 2 + w
        return ans

    @staticmethod
    def library_check_1(ac=FastIO()):
        """
        url: https://judge.yosupo.jp/problem/cycle_detection_undirected
        tag: union_find|circle_judge
        """
        n, m = ac.read_list_ints()
        edges = [ac.read_list_ints() for _ in range(m)]
        uf = UnionFind(n)
        dct = [[] for _ in range(n)]
        for i in range(m):
            u, v = edges[i]
            if not uf.union(u, v):
                stack = [(u, -1)]
                parent = [(-1, -1) for _ in range(n)]
                while stack:
                    x, fa = stack.pop()
                    for y, ind in dct[x]:
                        if y != fa:
                            parent[y] = (x, ind)
                            stack.append((y, x))
                nodes = [v]
                edges = []
                while nodes[-1] != u:
                    edges.append(parent[nodes[-1]][1])
                    nodes.append(parent[nodes[-1]][0])
                edges.append(i)
                ac.st(len(nodes))
                ac.lst(nodes)
                ac.lst(edges)
                break
            dct[u].append((v, i))
            dct[v].append((u, i))
        else:
            ac.st(-1)
        return

    @staticmethod
    def lg_p1196(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1196
        tag: union_find_weighted|classical|hard
        """
        uf = UnionFindWeighted(3 * 10 ** 4)
        for _ in range(ac.read_int()):
            op, i, j = ac.read_list_strs()
            i = int(i) - 1
            j = int(j) - 1
            if op == "M":
                uf.union_right(i, j)
            else:
                if uf.is_connected(i, j):
                    ac.st(abs(uf.dis[i] - uf.dis[j]) - 1)
                else:
                    ac.st(-1)
        return

    @staticmethod
    def lg_p1197(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1197
        tag: reverse_order|union_find|reverse_order|brute_force|part
        """
        n, m = ac.read_list_ints()
        dct = [[] for _ in range(n)]
        for _ in range(m):
            i, j = ac.read_list_ints()
            dct[i].append(j)
            dct[j].append(i)
        k = ac.read_int()
        rem = [ac.read_int() for _ in range(k)]
        out = set(rem)
        uf = UnionFind(n)
        for i in range(n):
            if i not in out:
                for j in dct[i]:
                    if j not in out:
                        uf.union(i, j)
        ans = []
        for i in range(k - 1, -1, -1):
            ans.append(uf.part - i - 1)
            out.discard(rem[i])
            for j in dct[rem[i]]:
                if j not in out:
                    uf.union(rem[i], j)
        ans.append(uf.part)
        ans.reverse()
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def lg_p1522(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1522
        tag: connected_part|brute_force|high_precision|tree_diameter|classical|hard
        """

        def dis(x1, y1, x2, y2):
            return math.sqrt(decimal.Decimal(((x1 - x2) ** 2 + (y1 - y2) ** 2)))

        n = ac.read_int()
        nums = [[w for w in ac.read_list_ints()] for _ in range(n)]
        grid = [ac.read_str() for _ in range(n)]
        graph = WeightedGraphForDijkstra(n)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if grid[i][j] == "1":
                    uf.union(i, j)
                    d = dis(nums[i][0], nums[i][1], nums[j][0], nums[j][1])
                    graph.add_undirected_edge(i, j, d)

        dist = []
        for i in range(n):
            dist.append(graph.dijkstra_for_shortest_path_float(i))

        part = uf.get_root_part()
        fast = [math.inf] * n
        group = dict()
        for p in part:
            for i in part[p]:
                fast[i] = max(dist[i][j] for j in part[p])
            group[p] = max(fast[i] for i in part[p])

        ans = math.inf
        for i in range(n):
            for j in range(n):
                if not uf.is_connected(i, j):
                    cur = dis(nums[i][0], nums[i][1], nums[j][0], nums[j][1]) + fast[i] + fast[j]
                    cur = max(cur, group[uf.find(i)])
                    cur = max(cur, group[uf.find(j)])
                    ans = min(ans, cur)
        ac.st("%.6f" % ans)
        return

    @staticmethod
    def lg_p1621(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1621
        tag: euler_series|O(nlogn)|prime_factorization|classical
        """
        a, b, p = ac.read_list_ints()
        nums = list(range(a, b + 1))
        ind = {num: num - a for num in nums}
        primes = [x for x in PrimeSieve().eratosthenes_sieve(b) if x >= p]

        uf = UnionFind(b - a + 1)
        for x in primes:
            lst = []
            y = x
            while y <= b:
                if y in ind:
                    lst.append(ind[y])
                y += x
            m = len(lst)
            for j in range(m - 1):
                uf.union(lst[j], lst[j + 1])
        ac.st(uf.part)
        return

    @staticmethod
    def lg_p1892(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1892
        tag: union_find|bipartite_graph
        """
        n = ac.read_int()
        m = ac.read_int()
        uf = UnionFind(n)
        dct = dict()
        for _ in range(m):
            lst = ac.read_list_strs()
            a, b = int(lst[1]), int(lst[2])
            a -= 1
            b -= 1
            if lst[0] == "E":
                if a in dct:
                    uf.union(dct[a], b)
                if b in dct:
                    uf.union(dct[b], a)
                dct[a] = b
                dct[b] = a
            else:
                uf.union(a, b)
        ac.st(uf.part)
        return

    @staticmethod
    def lg_p1955(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1955
        tag: union_find|discretization
        """
        t = ac.read_int()
        for _ in range(t):
            n = ac.read_int()
            ind = dict()
            uf = UnionFind(n * 2)
            res = []
            for _ in range(n):
                lst = ac.read_list_ints()
                while not lst:
                    lst = ac.read_list_ints()
                i, j, e = lst
                if i not in ind:
                    ind[i] = len(ind)
                if j not in ind:
                    ind[j] = len(ind)
                if e == 1:
                    uf.union(ind[i], ind[j])
                else:
                    res.append((ind[i], ind[j]))
            if any(uf.is_connected(i, j) for i, j in res):
                ac.no()
            else:
                ac.yes()
        return

    @staticmethod
    def lg_p2189(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2189
        tag: union_find|classical|preprocess|hard
        """
        n, m, k, q = ac.read_list_ints()
        dct = [[] for _ in range(n)]
        for _ in range(m):
            i, j = ac.read_list_ints_minus_one()
            dct[i].append(j)
            dct[j].append(i)

        for _ in range(q):
            order = ac.read_list_ints_minus_one()
            uf = UnionFind(n)
            visit = [0] * n
            for i in order:
                visit[i] = 1

            ans = True
            pre = order[0]
            for i in range(n):
                if not visit[i]:
                    for j in dct[i]:
                        if not visit[j]:
                            uf.union(i, j)

            for i in order:
                visit[i] = 0
                for j in dct[i]:
                    if not visit[j]:
                        uf.union(i, j)
                if not uf.is_connected(i, pre):
                    ans = False
                    break
                pre = i
            ac.st("Yes" if ans else "No")
        return

    @staticmethod
    def lg_p2307(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2307
        tag: union_find
        """
        while True:
            ans = []
            while True:
                lst = ac.read_list_ints()
                if not lst:
                    break
                ans.extend(lst)
            if ans == [-1, -1]:
                break
            ans = ans[:-2]
            nodes = list(set(ans))
            ind = {num: i for i, num in enumerate(nodes)}
            m = len(ind)
            uf = UnionFind(m)
            res = True
            for i in range(0, len(ans), 2):
                a, b = ind[ans[i]], ind[ans[i + 1]]
                if not uf.union(a, b):
                    res = False
                    break
            ac.st(1 if res and uf.part == 1 else 0)
        return

    @staticmethod
    def lg_p3420(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3420
        tag: union_find
        """
        n = ac.read_int()
        uf = UnionFind(n)
        for i in range(n):
            j = ac.read_int()
            uf.union(i, j - 1)
        ac.st(uf.part)
        return

    @staticmethod
    def lg_p6004(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6004
        tag: union_find|permutation_circle|kruskal|mst|greedy|pointer
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints_minus_one()
        edges = [ac.read_list_ints() for _ in range(m)]
        edges.sort(key=lambda it: -it[2])
        uf = UnionFind(n)
        ind = 0
        ans = -1
        for i, j, w in edges:
            while ind < n and uf.is_connected(ind, nums[ind]):
                ind += 1
            if ind == n:
                ac.st(ans)
                return
            uf.union(i - 1, j - 1)
            ans = w
        ac.st(ans)
        return

    @staticmethod
    def lg_p6193(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6193
        tag: permutation_circle|discretization|brain_teaser|classical|hard
        """
        n = ac.read_int()
        nums = [ac.read_int() for _ in range(n)]
        lst = sorted(nums)
        ind = {num: i for i, num in enumerate(lst)}
        uf = UnionFind(n)
        x = lst[0]
        for i in range(n):
            uf.union(i, ind[nums[i]])
        part = uf.get_root_part()
        ans = 0
        for p in part:
            y = min(lst[i] for i in part[p])
            s = sum(lst[i] for i in part[p])
            m = len(part[p])
            if m == 1:
                continue
            cost1 = s + (m - 2) * y
            cost2 = s - y + x + (m - 2) * x + (x + y) * 2
            ans += min(cost1, cost2)
        ac.st(ans)
        return

    @staticmethod
    def lc_2709(nums: List[int]) -> bool:
        """
        url: https://leetcode.cn/problems/greatest-common-divisor-traversal/
        tag: union_find|prime_factorization
        """
        pf = PrimeFactor(10 ** 5)
        n = len(nums)
        uf = UnionFind(n)
        pre = dict()
        for i in range(n):
            for num, _ in pf.prime_factor[nums[i]]:
                if num in pre:
                    uf.union(i, pre[num])
                else:
                    pre[num] = i
        return uf.part == 1

    @staticmethod
    def lg_p6706(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6706
        tag: directed_graph|union_find|reverse_order|find_range_merge_to_disjoint|classical|hard
        """
        n = ac.read_int()  # MLE
        edge = ac.read_list_ints()
        q = ac.read_int()
        query = []
        for _ in range(q):
            op, x = ac.read_list_ints()
            if op == 2:
                edge[x - 1] = -edge[x - 1]
            query.append(op * (n + 1) + x)
        uf = UnionFind(n + 1)
        for i in range(1, n + 1):
            if edge[i - 1] > 0:
                j = uf.find(edge[i - 1])
                if j == i:
                    uf.union_left(0, i)
                    uf.union_left(0, j)
                else:
                    uf.union_right(i, j)

        ans = []
        for i in range(q - 1, -1, -1):
            op, x = query[i] // (n + 1), query[i] % (n + 1)
            if op == 1:
                y = uf.find(x)
                if y == 0:
                    res = "CIKLUS"
                else:
                    res = y
                ans.append(res)
            else:
                j = uf.find(-edge[x - 1])
                if j == x:
                    uf.union_left(0, x)
                    uf.union_left(0, j)
                else:
                    uf.union_right(x, j)
        for i in range(len(ans) - 1, -1, -1):
            ac.st(ans[i])
        return

    @staticmethod
    def lg_p7991(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P7991
        tag: union_find|shrink_point
        """
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            uf = UnionFind(n)
            for _ in range(m):
                i, j = ac.read_list_ints_minus_one()
                uf.union(i, j)
            if uf.is_connected(0, n - 1):
                ac.st(0)
                continue

            dis_0 = [n] * n
            dis_1 = [n] * n

            pre_0 = pre_1 = -1
            for i in range(n):
                if uf.is_connected(0, i):
                    pre_0 = i
                if uf.is_connected(n - 1, i):
                    pre_1 = i
                if pre_0 != -1:
                    dis_0[uf.find(i)] = min(dis_0[uf.find(i)], i - pre_0)
                if pre_1 != -1:
                    dis_1[uf.find(i)] = min(dis_1[uf.find(i)], i - pre_1)

            pre_0 = pre_1 = -1
            for i in range(n - 1, -1, -1):
                if uf.is_connected(0, i):
                    pre_0 = i
                if uf.is_connected(n - 1, i):
                    pre_1 = i
                if pre_0 != -1:
                    dis_0[uf.find(i)] = min(dis_0[uf.find(i)], pre_0 - i)
                if pre_1 != -1:
                    dis_1[uf.find(i)] = min(dis_1[uf.find(i)], pre_1 - i)
            ans = min(dis_0[i] * dis_0[i] + dis_1[i] * dis_1[i] for i in range(n))
            ac.st(ans)
        return

    @staticmethod
    def lc_2612(n: int, p: int, banned: List[int], k: int) -> List[int]:
        """
        url: https://leetcode.cn/problems/minimum-reverse-operations/
        tag: union_find|find_range_merge_to_disjoint|classical|hard|odd_even|bfs|brain_teaser
        """
        ans = [-1] * n
        uf = UnionFind(n + 2)
        for i in banned:
            uf.union_right(i, i + 2)
        stack = deque([p])
        ans[p] = 0
        while stack:
            i = stack.popleft()
            low = max(0, k - 1 - i, i - k + 1)
            high = min(2 * n - k - 1 - i, n - 1, i + k - 1)
            j = uf.find(low)
            while j <= high:
                if ans[j] == -1:
                    ans[j] = ans[i] + 1
                    stack.append(j)
                    uf.union_right(j, j + 2)
                j = uf.find(j + 2)
        return ans

    @staticmethod
    def lg_p8230(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8230
        tag: layer|union_find|implemention|mst|brain_teaser
        """
        k, m, n = ac.read_list_ints()
        ans = 1
        start = [0, 0]
        uf = UnionFind(m * n)
        for _ in range(k):

            lst = []
            end = [-1, -1]
            for i in range(m * n):
                uf.root_or_size[i] = -1
            pre = [-9] * n
            for i in range(m):
                cur = ac.read_list_ints()
                for j in range(n):
                    w = cur[j]
                    if w != -9:
                        lst.append(w * m * n + i * n + j)
                        x = i - 1
                        if 0 <= x < m and pre[j] != -9:
                            uf.union(i * n + j, x * n + j)

                        y = j - 1
                        if 0 <= y < n and cur[y] != -9:
                            uf.union(i * n + j, i * n + y)

                    if w == -1:
                        end = [i, j]
                pre = cur[:]
            lst.sort()

            for num in lst:
                val, i, j = num // m // n, (num % (m * n)) // n, (num % (m * n)) % n
                if val > ans:
                    break
                if uf.is_connected(start[0] * n + start[1], i * n + j):
                    if ans >= val:
                        if val > 0:
                            ans += val
            start = end[:]
        ac.st(ans)
        return

    @staticmethod
    def lg_p8686(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8686
        tag: union_find|classical
        """
        ac.read_int()
        nums = ac.read_list_ints()
        dct = dict()
        ans = []
        for num in nums:
            pre = num
            while pre in dct:
                pre = dct[pre]

            x = num
            while x in dct:
                dct[x], x = pre + 1, dct[x]

            dct[pre] = pre + 1
            ans.append(pre)
        ac.lst(ans)
        return

    @staticmethod
    def lg_p8787_1(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8787
        tag: greedy|heapq|implemention|union_find|classical|hard

        """
        n = ac.read_int()
        nums = ac.read_list_ints()
        stack = [(-nums[i], -i) for i in range(n)]
        heapify(stack)
        uf = UnionFind(n)
        for i in range(n):
            if i and nums[i] == nums[i - 1]:
                uf.union_left(i - 1, i)
        ans = 0
        while stack:
            val, i = heappop(stack)
            val, i = -val, -i
            if val == 1:
                break
            if i != uf.find(i):
                continue
            if i and nums[uf.find(i - 1)] == val:
                uf.union_left(i - 1, i)
                continue
            ans += 1
            val = int(((val // 2) + 1) ** 0.5)
            nums[i] = val
            heappush(stack, (-val, -i))
        ac.st(ans)
        return

    @staticmethod
    def lg_p8787_2(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8787
        tag: greedy|heapq|implemention|union_find|classical|hard

        """
        ac.read_int()
        nums = ac.read_list_ints()
        pre = set()
        ans = 0
        for num in nums:
            cur = set()
            while num > 1:
                if num not in pre:
                    ans += 1
                cur.add(num)
                num = int(((num // 2) + 1) ** 0.5)
            pre = cur
        ac.st(ans)
        return

    @staticmethod
    def lg_p8881(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8881
        tag: brain_teaser|union_find|circle_judge|part|classical
        """
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            uf = UnionFind(n)
            edge = []
            for _ in range(m):
                i, j = ac.read_list_ints_minus_one()
                uf.union(i, j)
                edge.append((i, j))
            cnt = 0
            for i, j in edge:
                if uf.is_connected(0, i):
                    cnt += 1
            ac.st("1.000" if uf.size(0) == cnt + 1 else "0.000")
        return

    @staticmethod
    def lc_945_1(nums: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/minimum-increment-to-make-array-unique/description/
        tag: union_find_right_root|greedy
        """
        nums.sort()
        ans = 0
        uf = UnionFind(max(nums) + len(nums) + 2)
        for num in nums:
            x = uf.find(num)
            ans += x - num
            uf.union_right(x, x + 1)
        return ans

    @staticmethod
    def lc_945_2(nums: List[int]) -> int:
        """
        url: https://leetcode.cn/problems/minimum-increment-to-make-array-unique/description/
        tag: union_find_right_root|greedy
        """
        nums.sort()
        ans = 0
        pre = -1
        for num in nums:
            if num > pre:
                pre = num
            else:
                ans += pre + 1 - num
                pre += 1
        return ans

    @staticmethod
    def lc_1559(grid: List[List[str]]) -> bool:
        """
        url: https://leetcode.cn/problems/detect-cycles-in-2d-grid/
        tag: union_find|circle_judge|classical
        """
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if i + 1 < m and grid[i + 1][j] == grid[i][j]:
                    if not uf.union(i * n + j, i * n + n + j):
                        return True
                if j + 1 < n and grid[i][j + 1] == grid[i][j]:
                    if not uf.union(i * n + j, i * n + j + 1):
                        return True
        return False

    @staticmethod
    def lc_2158(paint: List[List[int]]) -> List[int]:
        """
        url: https://leetcode.cn/problems/amount-of-new-area-painted-each-day/
        tag: union_find_range|union_left|union_find_right_root
        """
        m = max(ls[1] for ls in paint) + 10
        uf = UnionFind(m)
        ans = []
        for a, b in paint:
            cnt = 0
            a = uf.find(a)
            while a < b:
                cnt += 1
                uf.union_right(a, a + 1)
                a = uf.find(a + 1)
            ans.append(cnt)
        return ans

    @staticmethod
    def abc_065b(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc049/tasks/arc065_b
        tag: union_find|several_union_find
        """
        n, k, ll = ac.read_list_ints()
        ufa = UnionFind(n)
        for _ in range(k):
            p, q = ac.read_list_ints_minus_one()
            ufa.union(p, q)

        ufb = UnionFind(n)
        for _ in range(ll):
            p, q = ac.read_list_ints_minus_one()
            ufb.union(p, q)
        pre = defaultdict(int)
        for i in range(n):
            pre[(ufa.find(i), ufb.find(i))] += 1
        ans = [pre[(ufa.find(i), ufb.find(i))] for i in range(n)]
        ac.lst(ans)
        return

    @staticmethod
    def abc_131f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc131/tasks/abc131_f
        tag: brain_teaser|union_find|counter|hard|classical
        """
        n = ac.read_int()
        m = 10 ** 5
        uf = UnionFind(2 * m)
        for _ in range(n):
            x, y = ac.read_list_ints_minus_one()
            y += m
            uf.union(x, y)
        group = uf.get_root_part()
        ans = 0
        for g in group:
            x = sum(xx < m for xx in group[g])
            y = sum(xx >= m for xx in group[g])
            ans += x * y
        ac.st(ans - n)
        return

    @staticmethod
    def ac_4309(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/description/4309/
        tag: union_right|greedy
        """
        n = ac.read_int()
        a = ac.read_list_ints()
        uf = UnionFind(n * 2 + 2)
        a.sort()
        ans = 0
        for num in a:
            x = uf.find(num)
            ans += x - num
            uf.union_right(x, x + 1)
        ac.st(ans)
        return

    @staticmethod
    def ac_4869(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/description/4869/
        tag: union_find|implemention|size|classical
        """
        n, d = ac.read_list_ints()
        uf = UnionFind(n)
        lst = SortedList([1] * n)
        pre = ans = 1
        for i in range(d):
            x, y = ac.read_list_ints_minus_one()
            if uf.is_connected(x, y):
                pre += 1
                if len(lst) - pre >= 0:
                    ans += lst[len(lst) - pre]
            else:
                for w in [x, y]:
                    i = lst.bisect_left(uf.size(w))
                    if i >= len(lst) - pre:
                        ans -= lst.pop(i)
                        if len(lst) - pre >= 0:
                            ans += lst[len(lst) - pre]
                    else:
                        lst.pop(i)

                uf.union(x, y)
                lst.add(uf.size(x))
                i = lst.bisect_right(uf.size(x))
                if i >= len(lst) - pre:
                    ans += uf.size(x)
                    if len(lst) - pre - 1 >= 0:
                        ans -= lst[len(lst) - pre - 1]
            ac.st(ans - 1)
        return

    @staticmethod
    def lc_2471(root: Optional[TreeNode]) -> int:
        """
        url: https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
        tag: discretization|permutation_circle|classical
        """

        def check():
            nonlocal ans
            ind = {num: i for i, num in enumerate(cur)}
            lst = sorted(cur)
            m = len(lst)
            uf = UnionFind(m)
            for i in range(m):
                uf.union(ind[lst[i]], ind[cur[i]])
            group = uf.get_root_size()
            for p in group:
                ans += group[p] - 1
            return

        ans = 0
        stack = [root] if root else []
        while stack:
            nex = []
            cur = [node.val for node in stack]
            check()
            for node in stack:
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            stack = nex[:]
        return ans

    @staticmethod
    def cf_1411c(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1411/problem/C
        tag: brain_teaser|classical|hard
        """
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            uf = UnionFind(n)
            ans = 0
            for _ in range(m):
                x, y = ac.read_list_ints_minus_one()
                if x == y:
                    continue
                if uf.union(x, y):
                    ans += 1
                else:
                    ans += 2
            ac.st(ans)
        return

    @staticmethod
    def abc_304e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc304/tasks/abc304_e
        tag: union_find|reverse_thinking
        """
        n, m = ac.read_list_ints()
        uf = UnionFind(n)
        for _ in range(m):
            x, y = ac.read_list_ints_minus_one()
            uf.union(x, y)
        bad = set()
        for _ in range(ac.read_int()):
            x, y = ac.read_list_ints_minus_one()
            a, b = uf.find(x), uf.find(y)
            bad.add((a, b) if a < b else (b, a))
        for _ in range(ac.read_int()):
            x, y = ac.read_list_ints_minus_one()
            a, b = uf.find(x), uf.find(y)
            if a > b:
                a, b = b, a
            ac.st("Yes" if (a, b) not in bad else "No")
        return

    @staticmethod
    def abc_238e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc238/tasks/abc238_e
        tag: union_find_range|prefix_sum|brain_teaser
        """
        n, q = ac.read_list_ints()
        uf = UnionFind(n + 1)
        for _ in range(q):
            ll, rr = ac.read_list_ints_minus_one()
            uf.union_right(ll, rr + 1)  # pre[rr+1] - pre[ll]
        ac.st("Yes" if uf.is_connected(0, n) else "No")  # pre[n] - pre[0]
        return

    @staticmethod
    def abc_279f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc279/tasks/abc279_f
        tag: union_find_range|brain_teaser|build_graph|classical
        """
        n, q = ac.read_list_ints()
        uf = UnionFind(n + q + q)
        ball_ind = n
        box_ind = n + q
        box = list(range(n))
        dct = list(range(n + q + q))
        for i in range(q):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y = [w - 1 for w in lst[1:]]
                uf.union_right(box[y], box[x])
                box[y] = box_ind
                dct[box_ind] = y
                box_ind += 1
            elif lst[0] == 2:
                x = lst[1] - 1
                uf.union_right(ball_ind, box[x])
                ball_ind += 1
            else:
                x = lst[1] - 1
                ac.st(dct[uf.find(x)] + 1)
        return

    @staticmethod
    def cf_1726d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1726/problem/D
        tag: union_find|brain_teaser|classical
        """
        uf = UnionFind(2 * 10 ** 6)
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            edges = [ac.read_list_ints_minus_one() for _ in range(m)]
            for i in range(n):
                uf.root_or_size[i] = -1
            uf.part = n

            color = [1] * m
            blue = []
            for i in range(m):
                x, y = edges[i]
                if not uf.union(x, y):
                    color[i] = 0
                    blue.append(i)
                    if len(blue) == 3:
                        break
            points = set()
            for i in blue:
                x, y = edges[i]
                points.add(x)
                points.add(y)
            if len(blue) == 3 and len(set(points)) == 3:
                ind = blue[0]
                for i in range(n):
                    uf.root_or_size[i] = -1
                uf.part = n
                color[ind] = 1
                uf.union(edges[ind][0], edges[ind][1])
                for i in range(m):
                    if i not in blue:
                        x, y = edges[i]
                        if not uf.union(x, y):
                            color[i] = 0
                            break
            ac.st("".join(str(x) for x in color))
        return

    @staticmethod
    def cf_915f(ac=FastIO()):
        """
        url: https://codeforces.com/contest/915/problem/F
        tag: union_find|contribution_method|counter
        """
        n = ac.read_int()
        nums = [x * n + i for i, x in enumerate(ac.read_list_ints())]
        dct = [[] for _ in range(n)]
        rev = [[] for _ in range(n)]
        for _ in range(n - 1):
            i, j = ac.read_list_ints_minus_one()
            if nums[i] > nums[j]:
                dct[i].append(j)
                rev[j].append(i)
            else:
                dct[j].append(i)
                rev[i].append(j)
        nums.sort()

        uf = UnionFind(n)
        ans = 0
        for x in nums:
            val, a = x // n, x % n
            for b in dct[a]:
                left = uf.size(a)
                right = uf.size(b)
                ans += val * left * right
                uf.union(a, b)

        uf = UnionFind(n)
        for i in range(n - 1, -1, -1):
            x = nums[i]
            val, a = x // n, x % n
            for b in rev[a]:
                left = uf.size(a)
                right = uf.size(b)
                ans -= val * left * right
                uf.union(a, b)
        ac.st(ans)
        return

    @staticmethod
    def abc_214d(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc214/tasks/abc214_d
        tag: union_find|contribution_method|counter
        """
        n = ac.read_int()
        edges = [ac.read_list_ints() for _ in range(n - 1)]
        edges.sort(key=lambda it: it[2])
        ans = 0
        uf = UnionFind(n)
        for a, b, w in edges:
            left = uf.size(a - 1)
            right = uf.size(b - 1)
            ans += w * left * right
            uf.union(a - 1, b - 1)
        ac.st(ans)
        return

    @staticmethod
    def cf_371d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/371/D
        tag: union_find_right
        """
        n = ac.read_int()
        a = ac.read_list_ints()
        uf = UnionFind(n + 1)
        water = [0] * (n + 1)
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                u, x = lst[1:]
                u -= 1
                root = u
                while root < n and x:
                    root = uf.find(root)
                    if root == n:
                        break
                    c = min(a[root] - water[root], x)
                    x -= c
                    water[root] += c
                    if water[root] == a[root]:
                        uf.union_right(root, root + 1)
                        root = uf.find(root)
            else:
                u = lst[1]
                u -= 1
                ac.st(water[u])
        return

    @staticmethod
    def lg_p5930(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P5930
        tag: union_find|classical
        """

        m, n = ac.read_list_ints()
        grid = []
        for i in range(m):
            lst = ac.read_list_ints()
            grid.extend([lst[j] * m * n + i * n + j for j in range(n)])
        uf = UnionFindSP(m * n + 1)
        ans = 0
        for val in sorted(grid):
            h, i, j = val // m // n, (val - (val // m // n) * m * n) // n, val % n
            uf.size[i * n + j] = 1
            uf.height[i * n + j] = h
            if i in [0, m - 1] or j in [0, n - 1]:
                ans += uf.union_right(i * n + j, m * n, h)

            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and uf.size[x * n + y] > 0:
                    ans += uf.union_right(i * n + j, x * n + y, h)
        ac.st(ans)
        return

    @staticmethod
    def lc_407(grid: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/problems/trapping-rain-water-ii/
        tag: union_find|classical
        """
        m, n = len(grid), len(grid[0])
        lst = [grid[i][j] * m * n + i * n + j for j in range(n) for i in range(m)]
        lst.sort()
        uf = UnionFindSP(m * n + 1)
        ans = 0
        for val in lst:
            h, i, j = val // m // n, (val - (val // m // n) * m * n) // n, val % n
            uf.size[i * n + j] = 1
            uf.height[i * n + j] = h
            if i in [0, m - 1] or j in [0, n - 1]:
                ans += uf.union_right(i * n + j, m * n, h)

            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and uf.size[x * n + y] > 0:
                    ans += uf.union_right(i * n + j, x * n + y, h)
        return ans

    @staticmethod
    def cf_292d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/292/D
        tag: union_find_right|prefix_suffix
        """
        n, m = ac.read_list_ints()  # TLE
        pre = [0 for _ in range(m + 1)]
        lst = []
        uf = UnionFind(n)
        lst.append(uf.root_or_size[:])
        parts = [n]
        ind = 0
        edges = [ac.read_list_ints_minus_one() for _ in range(m)]
        for i, (x, y) in enumerate(edges):
            if uf.union(x, y):
                ind = len(lst)
                lst.append(uf.root_or_size[:])
                parts.append(uf.part)
            pre[i + 1] = ind
        q = ac.read_int()
        ans = [0] * q
        queries = [[] for _ in range(m)]
        for i in range(q):
            ll, rr = ac.read_list_ints_minus_one()
            queries[rr].append((ll, i))
        uf = UnionFind(n)
        cur_uf = UnionFind(n)
        for rr in range(m - 1, -1, -1):
            for ll, i in queries[rr]:
                cur_uf.root_or_size[:] = lst[pre[ll]][:]
                cur_uf.part = parts[pre[ll]]
                for j in range(n):
                    cur_uf.union(j, uf.find(j))
                ans[i] = cur_uf.part
            x, y = edges[rr]
            uf.union(x, y)
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def library_check_2(ac=FastIO()):
        """
        url: https://ac.nowcoder.com/acm/contest/7780/C
        tag: union_find|circle_judge
        """
        n, m, k = ac.read_list_ints()
        uf = UnionFind(n)
        edges = [ac.read_list_ints_minus_one() for _ in range(m)]
        ans = 0
        for i, j in edges:
            if i >= k and j >= k:
                uf.union(i, j)
        for i, j in edges:
            if i < k or j < k:
                if not uf.union(i, j):
                    ans += 1
        ac.st(ans)
        return

    @staticmethod
    def cf_566d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/566/D
        tag: union_find_range
        """
        n, q = ac.read_list_ints()
        uf = UnionFind(n)
        uf_range = UnionFind(n)
        for _ in range(q):
            op, x, y = ac.read_list_ints_minus_one()
            if op == 0:
                uf.union(x, y)
            elif op == 1:
                while x < y:
                    uf.union(x, x + 1)
                    uf_range.union_right(x, x + 1)
                    x = uf_range.find(x)
            else:
                ac.st("YES" if uf.is_connected(x, y) else "NO")
        return

    @staticmethod
    def cf_1012b(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1012/B
        tag: union_find|brain_teaser|classical
        """
        n, m, q = ac.read_list_ints()
        uf = UnionFind(n + m)
        for _ in range(q):
            x, y = ac.read_list_ints_minus_one()
            uf.union(x, y + n)
        ac.st(uf.part - 1)
        return

    @staticmethod
    def cf_650c(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/650/C
        tag: union_find|matrix_rank|row_column_union_find
        """
        m, n = ac.read_list_ints()
        matrix = [ac.read_list_ints() for _ in range(m)]
        uf = UnionFind(m + n)

        groups = defaultdict(list)
        for i in range(m):
            for j in range(n):
                groups[matrix[i][j]].append((i, j))

        rank_r, rank_c = [0] * m, [0] * n
        for val in sorted(groups):
            for r, c in groups[val]:
                uf.union(r, c + m)

            roots = defaultdict(list)
            for r, c in groups[val]:
                roots[uf.find(r)].append((r, c))

            for lst in roots.values():
                rank = max(rank_r[r] if rank_r[r] >= rank_c[c] else rank_c[c] for r, c in lst) + 1
                for r, c in lst:
                    matrix[r][c] = rank
                    rank_r[r] = rank_c[c] = rank
                    uf.root_or_size[r] = -1
                    uf.root_or_size[c + m] = -1
        for ma in matrix:
            ac.lst(ma)
        return

    @staticmethod
    def lc_1632(matrix: List[List[int]]) -> List[List[int]]:
        """
        url: https://leetcode.cn/problems/rank-transform-of-a-matrix/
        tag: union_find|matrix_rank|row_column_union_find
        """
        m, n = len(matrix), len(matrix[0])
        uf = UnionFind(m + n)

        groups = defaultdict(list)
        for i in range(m):
            for j in range(n):
                groups[matrix[i][j]].append((i, j))

        rank_r, rank_c = [0] * m, [0] * n
        for val in sorted(groups):
            for r, c in groups[val]:
                uf.union(r, c + m)

            roots = defaultdict(list)
            for r, c in groups[val]:
                roots[uf.find(r)].append((r, c))

            for lst in roots.values():
                rank = max(rank_r[r] if rank_r[r] >= rank_c[c] else rank_c[c] for r, c in lst) + 1
                for r, c in lst:
                    matrix[r][c] = rank
                    rank_r[r] = rank_c[c] = rank
                    uf.root_or_size[r] = -1
                    uf.root_or_size[c + m] = -1
        return matrix

    @staticmethod
    def cf_1253d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1253/D
        tag: union_find_right
        """
        n, m = ac.read_list_ints()
        uf = UnionFind(n)
        for _ in range(m):
            x, y = ac.read_list_ints_minus_one()
            a, b = uf.find(x), uf.find(y)
            if a > b:
                a, b = b, a
            uf.union_right(a, b)
        ans = 0
        for x in range(n - 1):
            if not (x == uf.find(x) or uf.is_connected(x, x + 1)):
                ans += 1
                a, b = uf.find(x), uf.find(x + 1)
                if a > b:
                    a, b = b, a
                uf.union_right(a, b)
        ac.st(ans)
        return

    @staticmethod
    def library_check_3(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B
        tag: union_find_max|union_find_min
        """
        n, m = ac.read_list_ints()
        uf1 = UnionFind(n)
        uf2 = UnionFind(n)
        for _ in range(m):
            lst = ac.read_list_strs()
            if lst[0] == "union":
                x, y = [int(w) - 1 for w in lst[1:]]
                uf1.union_max(x, y)
                uf2.union_min(x, y)
            else:
                x = int(lst[1]) - 1
                ans = [uf2.find(x) + 1, uf1.find(x) + 1, uf1.size(x)]
                ac.lst(ans)
        return

    @staticmethod
    def library_checker_4(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C
        tag: union_find|heuristic_merge|classical|hard
        """
        n, m = ac.read_list_ints()
        uf = UnionFind(n)
        node = [0] * n
        root = [0] * n
        group = [[i] for i in range(n)]
        for _ in range(m):
            lst = ac.read_list_strs()
            if lst[0] == "add":
                x, v = [int(w) for w in lst[1:]]
                root[uf.find(x - 1)] += v

            elif lst[0] == "join":
                x, y = [int(w) - 1 for w in lst[1:]]
                x, y = uf.find(x), uf.find(y)
                if x == y:
                    continue
                if uf.size(x) > uf.size(y):
                    x, y = y, x
                gap = root[y] - root[x]
                while group[x]:  # important!
                    i = group[x].pop()
                    group[y].append(i)
                    node[i] -= gap
                uf.union_right(x, y)
            else:
                x = int(lst[1]) - 1
                ac.st(node[x] + root[uf.find(x)])
        return

    @staticmethod
    def library_check_5(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D
        tag: union_find|reverse_thinking|classical
        """
        n, m, q = ac.read_list_ints()
        uf = UnionFind(n)
        for _ in range(m):
            ac.read_list_ints()
        ans = []
        queries = [ac.read_list_strs() for _ in range(q)]
        for i in range(q - 1, -1, -1):
            lst = queries[i]
            x, y = [int(w) - 1 for w in lst[1:]]
            if lst[0] == "ask":
                ans.append("YES" if uf.is_connected(x, y) else "NO")
            else:
                uf.union(x, y)
        ac.st("\n".join(ans[::-1]))
        return

    @staticmethod
    def library_check_6(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A
        tag: union_find_range
        """
        n, m = ac.read_list_ints()
        uf = UnionFind(n + 2)
        for _ in range(m):
            op, x = ac.read_list_strs()
            x = int(x)
            if op == "?":
                ans = uf.find(x)
                ac.st(ans if ans < n + 1 else -1)
            else:
                uf.union_right(x, x + 1)
        return

    @staticmethod
    def library_check_7(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/B
        tag: union_find_range
        """
        n = ac.read_int()
        uf = UnionFind(n + 2)
        nums = ac.read_list_ints()
        ans = [-1] * n
        for i in range(n):
            x = uf.find(nums[i])
            if x == n + 1:
                x = uf.find(1)
            ans[i] = x
            uf.union_right(x, x + 1)
        ac.lst(ans)
        return

    @staticmethod
    def library_check_8(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C
        tag: union_find_range
        """
        n, q = ac.read_list_ints()
        uf = UnionFind(n)
        uf_range = UnionFind(n)
        for _ in range(q):
            op, x, y = ac.read_list_ints_minus_one()
            if op == 0:
                uf.union(x, y)
            elif op == 1:
                while x < y:
                    uf.union(x, x + 1)
                    uf_range.union_right(x, x + 1)
                    x = uf_range.find(x)
            else:
                ac.st("YES" if uf.is_connected(x, y) else "NO")
        return

    @staticmethod
    def cf_1609d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1609/D
        tag: union_find|part|sorted_list
        """
        n, q = ac.read_list_ints()
        uf = UnionFind(n)
        lst = SortedList([1] * n)
        cnt = 0
        for _ in range(q):
            i, j = ac.read_list_ints_minus_one()
            if uf.is_connected(i, j):
                cnt += 1
            else:
                lst.discard(uf.size(i))
                lst.discard(uf.size(j))
                uf.union(i, j)
                lst.add(uf.size(i))
            n = len(lst)
            ans = 0
            for i in range(n - 1, n - cnt - 2, -1):
                if i < 0:
                    break
                ans += lst[i]
            ac.st(ans - 1)
        return

    @staticmethod
    def arc_107c(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/AT_arc107_c
        tag: union_find|comb_perm
        """
        n, k = ac.read_list_ints()
        mod = 998244353
        cb = Combinatorics(n, mod)
        grid = [ac.read_list_ints() for _ in range(n)]

        ans = 1
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if all(grid[i][x] + grid[j][x] <= k for x in range(n)):
                    uf.union(i, j)
        for va in uf.get_root_size().values():
            ans *= cb.factorial(va)
            ans %= mod

        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if all(grid[x][i] + grid[x][j] <= k for x in range(n)):
                    uf.union(i, j)
        for va in uf.get_root_size().values():
            ans *= cb.factorial(va)
            ans %= mod
        ac.st(ans)
        return

    @staticmethod
    def cf_1850h(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1850/problem/H
        tag: union_find_weighted_dis|classical|hard
        """
        uf = UnionFindWeighted(2 * 10 ** 5)
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            for i in range(n):
                uf.root_or_size[i] = -1
                uf.dis[i] = 0
            ans = "YES"
            for _ in range(m):
                u, v, d = ac.read_list_ints_minus_one()
                d += 1
                if ans == "YES" and uf.union(u, v, d):
                    ans = "NO"
            ac.st(ans)
        return

    @staticmethod
    def abc_328f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc328/tasks/abc328_f
        tag: union_find_weighted_dis|classical|hard
        """
        n, q = ac.read_list_ints()
        uf = UnionFindWeighted(n)
        ans = []
        for i in range(q):
            u, v, d = ac.read_list_ints_minus_one()
            d += 1
            if not uf.union(u, v, d):
                ans.append(i + 1)
        ac.lst(ans)
        return

    @staticmethod
    def library_check_9(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/D
        tag: union_find_weighted_dis|classical|hard
        """
        n, m = ac.read_list_ints()
        uf = UnionFindWeighted(n)
        for _ in range(m):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                a, b = [w - 1 for w in lst[1:]]
                uf.union_right_weight(a, b, 1)
            else:
                c = lst[1] - 1
                uf.find(c)
                ac.st(uf.dis[c])
        return

    @staticmethod
    def cf_766d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/766/D
        tag: union_find_type|build_graph|bipartite_graph
        """
        n, m, q = ac.read_list_ints()
        uf = UnionFind(n * 2)
        words = ac.read_list_strs()
        ind = {w: i for i, w in enumerate(words)}
        for _ in range(m):
            lst = ac.read_list_strs()
            if lst[0] == "1":
                i, j = ind[lst[1]], ind[lst[2]]
                if uf.is_connected(i, j + n):
                    ac.no()
                else:
                    ac.yes()
                    uf.union(i, j)
                    uf.union(i + n, j + n)
            else:
                i, j = ind[lst[1]], ind[lst[2]]
                if uf.is_connected(i, j):
                    ac.no()
                else:
                    ac.yes()
                    uf.union(i, j + n)
                    uf.union(i + n, j)
        for _ in range(q):
            i, j = [ind[w] for w in ac.read_list_strs()]
            if uf.is_connected(i, j):
                ac.st(1)
            elif uf.is_connected(i, j + n):
                ac.st(2)
            else:
                ac.st(3)
        return

    @staticmethod
    def cf_1594d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1594/problem/D
        tag: union_find_type|build_graph|bipartite_graph|2-sat
        """

        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            uf = UnionFind(n * 2)
            for _ in range(m):
                i, j, s = ac.read_list_strs()
                i = int(i) - 1
                j = int(j) - 1
                if s == "crewmate":
                    uf.union(i, j)
                    uf.union(i + n, j + n)
                else:
                    uf.union(i, j + n)
                    uf.union(i + n, j)

            visit = [0] * 2 * n
            ans = 0
            group = uf.get_root_part()
            for i in range(n):
                if uf.is_connected(i, i + n):
                    ac.st(-1)
                    break
                if visit[uf.find(i)] or visit[uf.find(i + n)]:
                    continue
                cur = max(sum(x < n for x in group[uf.find(i)]), sum(x < n for x in group[uf.find(i + n)]))
                ans += cur
                visit[uf.find(i)] = visit[uf.find(i + n)] = 1
            else:
                ac.st(ans)
        return

    @staticmethod
    def lg_p2024(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2024
        tag: union_find_type|build_graph
        """

        n, k = ac.read_list_ints()
        ans = 0
        uf = UnionFind(n * 3)
        for _ in range(k):
            op, x, y = ac.read_list_ints_minus_one()
            if x >= n or y >= n:
                ans += 1
            elif op == 0:
                if uf.is_connected(x, y + n) or uf.is_connected(x, y + 2 * n):
                    ans += 1
                else:
                    uf.union(x, y)
                    uf.union(x + n, y + n)
                    uf.union(x + 2 * n, y + 2 * n)
            else:
                if uf.is_connected(x, y) or uf.is_connected(x + 2 * n, y):
                    ans += 1
                else:
                    uf.union(x, y + 2 * n)
                    uf.union(x + n, y)
                    uf.union(x + 2 * n, y + n)
        ac.st(ans)
        return

    @staticmethod
    def library_check_10(ac=FastIO()):
        """
        url: https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/J
        tag: union_find_type|build_graph
        """

        n, k = ac.read_list_ints()
        uf = UnionFind(n * 2)
        for i in range(k):
            x, y = ac.read_list_ints_minus_one()
            if uf.is_connected(x, y):
                ac.st(i + 1)
                break
            uf.union(x, y + n)
            uf.union(x + n, y)
        else:
            ac.st(-1)
        return

    @staticmethod
    def lg_p2391(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2391
        tag: union_find_right|reverse_thinking
        """
        n, m, p, q = [ac.read_int() for _ in range(4)]
        ans = [0] * n
        uf = UnionFind(n + 1)
        for i in range(m, 0, -1):
            x = (i * p + q) % n
            y = (i * q + p) % n
            if x > y:
                x, y = y, x
            x = uf.find(x)
            while x <= y:
                ans[x] = i
                uf.union_right(x, x + 1)
                x = uf.find(x + 1)
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def cf_920f_1(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/920/F
        tag: segment_tree|range_divide|range_sum|classical
        """
        n, m = ac.read_list_ints()
        tree = RangeDivideRangeSum(n, 10 ** 6)
        tree.build(ac.read_list_ints())
        for i in range(m):
            op, ll, rr = ac.read_list_ints_minus_one()
            if op == 0:
                tree.range_divide(ll, rr)
            else:
                ans = tree.range_sum(ll, rr)
                ac.st(ans)
        return

    @staticmethod
    def cf_1618g(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1618/problem/G
        tag: union_find_left|union_find_right|classical|offline_query
        """
        n, m, q = ac.read_list_ints()
        ans = [-1] * q
        nums = ac.read_list_ints() + ac.read_list_ints()
        ind = list(range(n + m))
        ind.sort(key=lambda it: nums[it])
        pre = ac.accumulate([nums[i] for i in ind])
        cnt = ac.accumulate([int(i < n) for i in ind])
        edges = [(nums[ind[i + 1]] - nums[ind[i]], i) for i in range(n + m - 1)]
        edges.sort()

        queries = ac.read_list_ints()
        index = list(range(q))
        index.sort(key=lambda it: queries[it])
        uf1 = UnionFind(n + m)
        uf2 = UnionFind(n + m)
        tot = sum(nums[:n])
        j = 0
        for i in index:
            k = queries[i]
            while j < n + m - 1 and edges[j][0] <= k:
                x = edges[j][1]
                if not uf1.is_connected(x, x + 1):
                    l1, r1 = uf1.find(x), uf2.find(x)
                    l2, r2 = uf1.find(x + 1), uf2.find(x + 1)
                    pre_c1 = cnt[r1 + 1] - cnt[l1]
                    pre_c2 = cnt[r2 + 1] - cnt[l2]
                    tot -= pre[r1 + 1] - pre[r1 + 1 - pre_c1]
                    tot -= pre[r2 + 1] - pre[r2 + 1 - pre_c2]
                    tot += pre[r2 + 1] - pre[r2 + 1 - pre_c1 - pre_c2]
                    uf1.union_left(x, x + 1)
                    uf2.union_right(x, x + 1)

                j += 1
            ans[i] = tot
        ac.st("\n".join(str(x) for x in ans))
        return

    @staticmethod
    def abc_314f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc314/tasks/abc314_f
        tag: union_find|bfs|build_graph|expectation|prob
        """
        n = ac.read_int()

        uf = UnionFindGeneral(2 * n - 1)
        uf.size = [1] * n + [0] * (n - 1)
        dct = [[] for _ in range(2 * n - 1)]
        mod = 998244353
        node = [0] * (2 * n - 1)
        for i in range(n - 1):
            p, q = ac.read_list_ints_minus_one()
            ll, rr = uf.size[uf.find(p)], uf.size[uf.find(q)]
            pq = pow(ll + rr, -1, mod)
            root_p, root_q = uf.find(p), uf.find(q)
            uf.union_right(root_p, i + n)
            uf.union_right(root_q, i + n)
            dct[i + n].extend([root_p, root_q])
            node[root_p] += ll * pq % mod
            node[root_q] += rr * pq % mod
        stack = [2 * n - 2]
        while stack:
            i = stack.pop()
            for j in dct[i]:
                node[j] += node[i]
                stack.append(j)
                node[j] %= mod
        ac.lst(node[:n])
        return

    @staticmethod
    def cf_1941g(ac=FastIO()):
        """
        url: https://codeforces.com/contest/1941/problem/G
        tag: union_find|build_graph|bfs|brain_teaser|classical
        """
        ac.get_random_seed()
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            color = dict()

            for _ in range(m):
                u, v, c = ac.read_list_ints_minus_one()
                if c ^ ac.random_seed not in color:
                    color[c ^ ac.random_seed] = []
                color[c ^ ac.random_seed].append((u, v))
            dct = [[] for _ in range(n + m)]
            uf = UnionFind(n)
            idx = n
            group = [set() for _ in range(n)]
            for c in color:
                for i, j in color[c]:
                    uf.union(i, j)
                roots = set()
                for i, j in color[c]:
                    group[uf.find(i)].add(j)
                    group[uf.find(i)].add(i)
                    roots.add(uf.find(i))
                for r in roots:
                    for i in group[r]:
                        dct[idx].append(i)
                        dct[i].append(idx)
                    idx += 1
                for i, j in color[c]:
                    uf.root_or_size[i] = -1
                    uf.root_or_size[j] = -1
                for r in roots:
                    group[r] = set()
            b, e = ac.read_list_ints_minus_one()
            dis = [math.inf] * (n + m)
            dis[b] = 0
            stack = [b]
            while stack:
                nex = []
                for i in stack:
                    for j in dct[i]:
                        if dis[j] == math.inf:
                            nex.append(j)
                            dis[j] = dis[i] + 1
                stack = nex[:]
            ac.st(dis[e] // 2)
        return

    @staticmethod
    def abc_295g(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc295/tasks/abc295_g
        tag: union_find|implemention|tree|union_min|classical
        """
        n = ac.read_int()
        to = [0] + ac.read_list_ints_minus_one()
        uf = UnionFind(n)
        parent = [0] * n
        for i in range(1, n):
            parent[i] = to[i]
        for _ in range(ac.read_int()):
            lst = ac.read_list_ints()
            if lst[0] == 1:
                x, y = lst[1:]
                x -= 1
                y -= 1
                while not uf.is_connected(x, y):
                    uf.union_min(x, parent[x])
                    x = uf.find(x)
            else:
                x = lst[1] - 1
                ac.st(uf.find(x) + 1)
        return

    @staticmethod
    def abc_264e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc264/tasks/abc264_e
        tag: union_right|reverse_order|classical
        """
        n, m, e = ac.read_list_ints()
        edges = [ac.read_list_ints_minus_one() for _ in range(e)]
        queries = [ac.read_int() - 1 for _ in range(ac.read_int())]
        uf = UnionFindGeneral(n + m + 1)
        uf.size = [1] * n + [0] * (m + 1)
        for i in range(n, n + m):
            uf.union_right(i, n + m)
        rem = set(queries)
        for i in range(e):
            if i not in rem:
                u, v = edges[i]
                uf.union_right(u, v)
        ans = [uf.size[uf.find(n + m)]]
        for i in queries[::-1]:
            u, v = edges[i]
            uf.union_right(u, v)
            ans.append(uf.size[uf.find(n + m)])
        ans.pop()
        ans.reverse()
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def abc_259d(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc259/tasks/abc259_d
        tag: geometry|union_find|circle_location|classical
        """
        n = ac.read_int()
        sx, sy, tx, ty = ac.read_list_ints()
        nums = [ac.read_list_ints() for _ in range(n)]
        uf = UnionFind(n + 2)
        for i in range(n):
            x1, y1, r1 = nums[i]
            for j in range(i + 1, n):
                x2, y2, r2 = nums[j]
                dis = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                if dis > (r1 + r2) ** 2:
                    continue
                if dis < (r1 - r2) ** 2:
                    continue
                uf.union(i, j)
            if (x1 - sx) * (x1 - sx) + (y1 - sy) * (y1 - sy) == r1 * r1:
                uf.union(i, n)
            if (x1 - tx) * (x1 - tx) + (y1 - ty) * (y1 - ty) == r1 * r1:
                uf.union(i, n + 1)
            if uf.is_connected(n, n + 1):
                ac.yes()
                return
        ac.no()
        return

    @staticmethod
    def abc_350g(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc350/tasks/abc350_g
        tag: implemention|union_find|data_range|heuristic_merge|brain_teaser|classical
        """
        n, q = ac.read_list_ints()
        uf = UnionFind(n)
        mod = 998244353
        dct = [set() for _ in range(n)]
        pre = dict()
        ans = 0
        for _ in range(q):
            a, b, c = ac.read_list_ints()
            op, u, v = 1 + ((a * (1 + ans)) % mod) % 2, 1 + ((b * (1 + ans)) % mod) % n, 1 + ((c * (1 + ans)) % mod) % n
            u -= 1
            v -= 1
            op -= 1
            if u > v:
                u, v = v, u
            if op == 0:
                dct[u].add(v)
                dct[v].add(u)
                uf.union(u, v)
            else:
                ans = 0
                if uf.is_connected(u, v):
                    if (u, v) in pre:
                        ans = pre[(u, v)]
                    else:
                        if len(dct[u]) < len(dct[v]):
                            for w in dct[u]:
                                if w in dct[v]:
                                    ans = w + 1
                                    break
                        else:
                            for w in dct[v]:
                                if w in dct[u]:
                                    ans = w + 1
                                    break
                        pre[(u, v)] = ans
                ac.st(ans)
        return

    @staticmethod
    def abc_350d(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc350/tasks/abc350_d
        tag: union_find|classical
        """

        n, m = ac.read_list_ints()
        uf = UnionFind(n)
        edges = []
        for _ in range(m):
            i, j = ac.read_list_ints_minus_one()
            uf.union(i, j)
            edges.append((i, j))
        group = defaultdict(int)
        for i, j in edges:
            group[uf.find(i)] += 1
        size = uf.get_root_size()
        ans = 0
        for g in size:
            ans += size[g] * (size[g] - 1) // 2 - group[g]
        ac.st(ans)
        return

    @staticmethod
    def abc_228d(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc228/tasks/abc228_d
        tag: union_find_range|classical|implemention
        """
        q = ac.read_int()
        n = 2 ** 20
        uf = UnionFind(n)
        nums = [-1] * n
        for _ in range(q):
            t, x = ac.read_list_ints()
            if t == 1:
                i = uf.find(x % n)
                if nums[i] != -1:
                    i = uf.find(0)
                nums[i] = x
                if i + 1 < n:
                    uf.union_right(i, i + 1)
            else:
                ac.st(nums[x % n])
        return

    @staticmethod
    def abc_351d(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc351/tasks/abc351_d
        tag: union_find|bfs|classical
        """
        m, n = ac.read_list_ints()
        grid = [ac.read_str() for _ in range(m)]
        uf = UnionFind(m * n)
        safe = [[1] * n for _ in range(m)]
        ind = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ".":
                    if any(0 <= i + a < m and 0 <= j + b < n and grid[i + a][j + b] == "#" for a, b in ind):
                        safe[i][j] = 0
                    ans = 1
                else:
                    safe[i][j] = 0
        for i in range(m):
            for j in range(n):
                if safe[i][j]:
                    for a, b in ind:
                        if 0 <= i + a < m and 0 <= j + b < n and safe[i + a][j + b]:
                            uf.union(i * n + j, (i + a) * n + j + b)

        group = uf.get_root_part()
        for g in group:
            lst = group[g]
            x = lst[0]
            if safe[x // n][x % n] == 0:
                continue
            cur = len(lst)
            flag = set()
            for x in lst:
                i, j = x // n, x % n
                for a, b in ind:
                    if 0 <= i + a < m and 0 <= j + b < n and grid[i + a][j + b] == "." and not safe[i + a][j + b]:
                        flag.add((i + a, j + b))
            ans = max(ans, cur + len(flag))
        ac.st(ans)
        return

    @staticmethod
    def abc_226e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc226/tasks/abc226_e
        tag: circle_based_tree|union_find|classical
        """
        n, m = ac.read_list_ints()
        uf = UnionFind(n)
        mod = 998244353
        edges = []
        for _ in range(m):
            i, j = ac.read_list_ints_minus_one()
            uf.union(i, j)
            edges.append((i, j))
        group = uf.get_root_part()
        degree = defaultdict(int)
        for i, j in edges:
            degree[uf.find(i)] += 1
        ans = 0
        for g in group:
            if len(group[g]) != degree[g]:
                ac.st(0)
                return
            ans += 1
        ac.st(pow(2, ans, mod))
        return

    @staticmethod
    def abc_214e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc214/tasks/abc214_e
        tag: union_find_right|dict|discretization|implemention|linked_list
        """
        for _ in range(ac.read_int()):
            n = ac.read_int()
            nums = [ac.read_list_ints() for _ in range(n)]
            nums.sort(key=lambda it: it[1])
            post = dict()
            for a, b in nums:
                x = a
                lst = []
                while x in post:
                    lst.append(x)
                    x = post[x]
                if x > b:
                    ac.no()
                    break
                for y in lst:
                    post[y] = x + 1
                post[x] = x + 1
            else:
                ac.yes()
        return

    @staticmethod
    def abc_355f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc355/tasks/abc355_f
        tag: union_find|brain_teaser|implemention
        """
        n, q = ac.read_list_ints()
        edges = [[] for _ in range(11)]
        for _ in range(n - 1):
            a, b, c = ac.read_list_ints()
            a -= 1
            b -= 1
            edges[c].append((a, b))
        ufs = [UnionFind(n) for _ in range(11)]
        ans = 0
        for x in range(1, 11):
            ufs[x].root_or_size[:] = ufs[x - 1].root_or_size[:]
            for a, b in edges[x]:
                ufs[x].union(a, b)
                ans += x
        for _ in range(q):
            u, v, w = ac.read_list_ints()
            u -= 1
            v -= 1
            for x in range(w + 1):
                if ufs[x].is_connected(u, v):
                    ac.st(ans)
                    break
            else:
                for y in range(w + 1, 11):
                    if ufs[y].is_connected(u, v):
                        ans -= y
                        ans += w
                        for yy in range(w, 11):
                            ufs[yy].union(u, v)
                        break
                ac.st(ans)
        return

    @staticmethod
    def cc_1(ac=FastIO()):
        """
        url: https://www.codechef.com/problems/TFALL
        tag: union_find_left|union_find_right|brute_force
        """
        for _ in range(ac.read_int()):
            n = ac.read_int()
            x = ac.read_list_ints()
            ufr = UnionFind(n)
            p = ac.read_list_ints()
            ufl = UnionFind(n)
            for i in range(1, n):
                if x[i] - x[i - 1] <= p[i]:
                    ufl.union_left(i - 1, i)

            for i in range(n - 2, -1, -1):
                if x[i + 1] - x[i] <= p[i]:
                    ufr.union_right(i, i + 1)
            if ufl.is_connected(0, n - 1) or ufr.is_connected(0, n - 1):
                ac.st("YES")
            else:
                for i in range(n - 1):
                    if ufl.is_connected(0, i) and ufr.is_connected(i + 1, n - 1):
                        ac.st("YES")
                        break
                    if ufr.is_connected(0, i) and ufl.is_connected(i + 1, n - 1):
                        ac.st("YES")
                        break
                    if ufr.is_connected(0, i) and ufr.is_connected(i + 1, n - 1):
                        ac.st("YES")
                        break
                    if ufl.is_connected(0, i) and ufl.is_connected(i + 1, n - 1):
                        ac.st("YES")
                        break
                else:
                    ac.st("NO")
        return

    @staticmethod
    def yuki_2786(ac=FastIO()):
        """
        url: https://yukicoder.me/problems/no/2786
        tag: heuristic_merge|union_find|classical
        """
        m, n = ac.read_list_ints()
        grid = [ac.read_list_ints() for _ in range(m)]
        q = ac.read_int()
        ans = [-1] * q
        dct = [[] for _ in range(m * n)]
        for i in range(q):
            x1, y1, x2, y2 = ac.read_list_ints_minus_one()
            dct[x1 * n + y1].append((i, x2 * n + y2))
            dct[x2 * n + y2].append((i, x1 * n + y1))
        ind = list(range(m * n))
        ind.sort(key=lambda it: grid[it // n][it % n])
        uf = UnionFind(m * n)
        for num in ind:
            x, y = num // n, num % n
            for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= a < m and 0 <= b < n and grid[a][b] <= grid[x][y] and not uf.is_connected(num, a * n + b):
                    root1, root2 = uf.find(num), uf.find(a * n + b)
                    if len(dct[root1]) < len(dct[root2]):
                        lst = []
                        for i, xx in dct[root1]:
                            if uf.is_connected(xx, root2):
                                ans[i] = grid[x][y]
                            else:
                                lst.append((i, xx))
                        dct[root2].extend(lst)
                        uf.union_left(root2, root1)
                    else:
                        lst = []
                        for i, xx in dct[root2]:
                            if uf.is_connected(xx, root1):
                                ans[i] = grid[x][y]
                            else:
                                lst.append((i, xx))
                        dct[root1].extend(lst)
                        uf.union_left(root1, root2)
        for a in ans:
            ac.st(a)
        return

    @staticmethod
    def cf_1383a(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1383/A
        tag: build_graph|greedy|implemention|union_find|brain_teaser|observation
        """
        for _ in range(ac.read_int()):
            n = ac.read_int()
            s = ac.read_str()
            t = ac.read_str()
            if all(s[i] <= t[i] for i in range(n)):
                uf = UnionFind(26)
                dct = defaultdict(set)
                for i in range(n):
                    if s[i] < t[i]:
                        dct[t[i]].add(s[i])
                ans = 0
                for w in dct:
                    for y in dct[w]:
                        if uf.union(ord(w) - ord("a"), ord(y) - ord("a")):
                            ans += 1
                ac.st(ans)
            else:
                ac.st(-1)
        return

    @staticmethod
    def cf_1494d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1494/D
        tag: union_right|union_find|implemention|construction
        """
        n = ac.read_int()
        dct = [[] for _ in range(5001)]
        for i in range(n):
            lst = ac.read_list_ints()
            for j in range(n):
                dct[lst[j]].append((i, j))
        uf = UnionFind(n * n)
        parent = [-1] * n * n
        salary = [-1] * n * n
        ind = n
        for d in range(1, 5001):
            for i, j in dct[d]:
                pi, pj = uf.find(i), uf.find(j)
                if pi == pj:
                    salary[pi] = d
                    continue
                if salary[pi] == d:
                    uf.union_right(pj, pi)
                    parent[pj] = pi
                    continue
                if salary[pj] == d:
                    uf.union_right(pi, pj)
                    parent[pi] = pj
                    continue
                parent[pi] = ind
                parent[pj] = ind
                uf.union_right(pi, ind)
                uf.union_right(pj, ind)
                salary[ind] = d
                ind += 1
        ac.st(ind)
        ac.lst(salary[:ind])
        ac.st(ind)
        for i in range(ind - 1):
            ac.lst([i + 1, parent[i] + 1])
        return

    @staticmethod
    def lc_100376(n: int, queries: List[List[int]]) -> List[int]:
        """
        url: https://leetcode.cn/problems/shortest-distance-after-road-addition-queries-ii/
        tag: build_graph|union_find|union_right
        """
        uf = UnionFind(n - 1)
        ans = []
        for x, y in queries:
            while uf.find(x) < y - 1:
                uf.union_right(x, uf.find(x + 1))
                x = uf.find(x + 1)
            ans.append(uf.part)
        return ans

    @staticmethod
    def cf_776d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/776/D
        tag: union_find|classical|2-sat
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        uf = UnionFind(m + m)
        key = [[] for _ in range(n)]
        for i in range(m):
            lst = ac.read_list_ints_minus_one()
            for x in lst[1:]:
                key[x].append(i)
        for x in range(n):
            a, b = key[x][0], key[x][1]
            if nums[x]:
                uf.union(a, b)
                uf.union(a + m, b + m)
            else:
                uf.union(a + m, b)
                uf.union(a, b + m)
        for i in range(m):
            if uf.is_connected(i, m + i):
                ac.no()
                break
        else:
            ac.yes()
        return

    @staticmethod
    def cf_1278d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1278/D
        tag: union_find|range|binary_search|observation|partial_order|observation|bucket_sort
        """
        n = ac.read_int()
        uf = UnionFind(n)
        line = defaultdict(list)
        m = 2 * n + 2
        for i in range(n):
            ll, rr = ac.read_list_ints()
            line[ll].append(rr * m + i)
        pre = SortedList()

        for ll in sorted(line):
            x = pre.bisect_right(ll * m)
            for val in line[ll]:
                rr, i = val // m, val % m
                j = x
                while j < len(pre) and pre[j] // m < rr:
                    k = pre[j] % m
                    if not uf.union(i, k):
                        ac.no()
                        return
                    j += 1
            for val in line[ll]:
                pre.add(val)
        if uf.part == 1:
            ac.yes()
        else:
            ac.no()
        return

    @staticmethod
    def cf_1994d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1994/D
        tag: reverse_order|pigeonhole_principle|union_find
        """
        for _ in range(ac.read_int()):
            n = ac.read_int()
            nums = ac.read_list_ints()
            uf = UnionFind(n)
            ac.yes()
            ans = []
            for x in range(n - 1, 0, -1):
                cur = [-1] * x
                for i in range(n):
                    j = nums[i] % x
                    if cur[j] != -1 and uf.union(cur[j], i):
                        ans.append([cur[j] + 1, i + 1])
                        break
                    cur[j] = i
            ans.reverse()
            for ls in ans:
                ac.lst(ls)
        return

    @staticmethod
    def abc_372e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc372/tasks/abc372_e
        tag: heuristic_merge|union_find
        """
        n, q = ac.read_list_ints()
        nodes = [[i] for i in range(n)]
        uf = UnionFind(n)
        for _ in range(q):
            op, a, b = ac.read_list_ints_minus_one()
            if op == 0:
                root1, root2 = uf.find(a), uf.find(b)
                if root1 == root2:
                    continue
                uf.union_right(root1, root2)
                lst1 = nodes[root1]
                lst2 = nodes[root2]
                m1, m2 = len(lst1), len(lst2)
                i1, i2 = 0, 0
                lst = []
                while i1 < m1 and i2 < m2:
                    if lst1[i1] < lst2[i2]:
                        lst.append(lst1[i1])
                        i1 += 1
                    else:
                        lst.append(lst2[i2])
                        i2 += 1
                lst.extend(lst1[i1:])
                lst.extend(lst2[i2:])
                nodes[root1] = None
                nodes[root2] = lst[-10:]
            else:
                root1 = uf.find(a)
                b += 1
                if len(nodes[root1]) < b:
                    ac.st(-1)
                else:
                    ac.st(nodes[root1][-b] + 1)
        return

    @staticmethod
    def lc_685(edges: List[List[int]]) -> List[int]:
        """
        url: https://leetcode.cn/problems/redundant-connection-ii/
        tag: union_find|directed_graph|in_degree|circle_based_tree|classical
        """
        n = len(edges)
        degree = [0] * (n + 1)
        for i, j in edges:
            degree[j] += 1
        uf = UnionFind(n + 1)
        if max(degree) == 1:
            for i, j in edges:
                if not uf.union(i, j):
                    return [i, j]
        lst = []
        for i, j in edges:
            if degree[j] == 2:
                lst.append([i, j])
            else:
                uf.union(i, j)
        for ls in lst:
            if uf.is_connected(ls[0], ls[1]):
                return ls
            uf.union(ls[0], ls[1])
        return [-1, -1]

    @staticmethod
    def abc_183f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc183/tasks/abc183_f
        tag: heuristic_merge|classical
        """
        n, q = ac.read_list_ints()
        c = ac.read_list_ints_minus_one()
        uf = UnionFind(n)
        sub = [{c[i]: 1} for i in range(n)]
        for _ in range(q):
            op, x, y = ac.read_list_ints_minus_one()
            if op == 0:
                root_x, root_y = uf.find(x), uf.find(y)
                if root_x == root_y:
                    continue
                if uf.size(root_x) > uf.size(root_y):
                    root_x, root_y = root_y, root_x
                uf.union_right(root_x, root_y)
                for w, v in sub[root_x].items():
                    sub[root_y][w] = sub[root_y].get(w, 0) + v
                sub[root_x] = dict()
            else:
                ans = sub[uf.find(x)].get(y, 0)
                ac.st(ans)
        return

    @staticmethod
    def abc_378f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc378/tasks/abc378_f
        tag: union_find|brute_force|observation
        """
        n = ac.read_int()
        dct = [[] for i in range(n)]
        degree = [0] * n
        edges = []
        for _ in range(n - 1):
            i, j = ac.read_list_ints_minus_one()
            dct[i].append(j)
            dct[j].append(i)
            degree[i] += 1
            degree[j] += 1
            edges.append((i, j))
        uf = UnionFind(n)
        for i, j in edges:
            if degree[i] == degree[j] == 3:
                uf.union(i, j)
        ans = 0
        group = uf.get_root_part()
        for g in group:
            lst = group[g]
            if all(degree[x] == 3 for x in lst):
                cur = set()
                for x in lst:
                    for y in dct[x]:
                        if degree[y] == 2:
                            cur.add(y)
                tow = len(cur)
                ans += tow * (tow - 1) // 2
        ac.st(ans)
        return

    @staticmethod
    def abc_380e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc380/tasks/abc380_e
        tag: union_find_range|union_left|union_right|classical
        """
        n, q = ac.read_list_ints()
        uf_left = UnionFind(n)
        color = list(range(n))
        uf_right = UnionFind(n)
        cnt = [1] * n
        for _ in range(q):
            lst = ac.read_list_ints_minus_one()
            if lst[0] == 0:
                x, c = lst[1], lst[2]
                root_left = uf_left.find(x)
                root_right = uf_right.find(x)
                cnt[color[root_left]] -= uf_left.size(x)
                color[root_left] = color[root_right] = c
                cnt[c] += uf_left.size(x)
                while root_right + 1 < n and color[uf_right.find(root_right + 1)] == c:
                    uf_right.union_right(root_right, root_right + 1)
                    uf_left.union_left(root_left, root_right + 1)
                    root_right = uf_right.find(root_right)
                while root_left and color[uf_left.find(root_left - 1)] == c:
                    uf_left.union_left(root_left - 1, root_left)
                    uf_right.union_right(root_left - 1, root_right)
                    root_left = uf_left.find(root_left)
            else:
                c = lst[1]
                ac.st(cnt[c])
        return

    @staticmethod
    def abc_170f(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc170/tasks/abc170_f
        tag: bfs|union_find|classical
        """
        m, n, k = ac.read_list_ints()
        x1, y1, x2, y2 = ac.read_list_ints_minus_one()
        grid = [ac.read_str() for _ in range(m)]
        inf = 10 ** 9
        visit = [inf] * n * m
        visit[x1 * n + y1] = 0
        stack = [x1 * n + y1]
        uf_up = [UnionFind(m) for _ in range(n)]
        uf_down = [UnionFind(m) for _ in range(n)]
        uf_left = [UnionFind(n) for _ in range(m)]
        uf_right = [UnionFind(n) for _ in range(m)]
        while stack and visit[x2 * n + y2] == inf:
            nex = []
            for val in stack:
                d = visit[val]
                x, y = val // n, val % n
                i, j = x, y

                while uf_up[y].find(i) and grid[uf_up[y].find(i) - 1][y] == "." and uf_up[y].find(i) - 1 >= x - k:
                    uf_up[y].union_right(i, uf_up[y].find(i) - 1)
                    i, j = uf_up[y].find(i), y
                    if visit[i * n + j] > d + 1:
                        visit[i * n + j] = d + 1
                        nex.append(i * n + j)

                i, j = x, y
                while uf_down[y].find(i) + 1 < m and grid[uf_down[y].find(i) + 1][y] == "." and uf_down[y].find(
                        i) + 1 <= x + k:
                    uf_down[y].union_right(i, uf_down[y].find(i) + 1)
                    i, j = uf_down[y].find(i), y
                    if visit[i * n + j] > d + 1:
                        visit[i * n + j] = d + 1
                        nex.append(i * n + j)

                i, j = x, y
                while uf_left[x].find(j) and grid[x][uf_left[x].find(j) - 1] == "." and uf_left[x].find(j) - 1 >= y - k:
                    uf_left[x].union_right(j, uf_left[x].find(j) - 1)
                    i, j = x, uf_left[x].find(j)
                    if visit[i * n + j] > d + 1:
                        visit[i * n + j] = d + 1
                        nex.append(i * n + j)

                i, j = x, y
                while uf_right[x].find(j) + 1 < n and grid[x][uf_right[x].find(j) + 1] == "." and uf_right[x].find(
                        j) + 1 <= y + k:
                    uf_right[x].union_right(j, uf_right[x].find(j) + 1)
                    i, j = x, uf_right[x].find(j)
                    if visit[i * n + j] > d + 1:
                        visit[i * n + j] = d + 1
                        nex.append(i * n + j)
            stack = nex
        ans = visit[x2 * n + y2]
        ac.st(ans if ans < inf else -1)
        return

    @staticmethod
    def abc_383e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc383/tasks/abc383_e
        tag: union_find|classical
        """
        n, m, k = ac.read_list_ints()
        uu = []
        vv = []
        ww = []
        for _ in range(m):
            u, v, w = ac.read_list_ints_minus_one()
            w += 1
            uu.append(u)
            vv.append(v)
            ww.append(w)
        ww = [ww[i] * m + i for i in range(m)]
        ww.sort()
        a = ac.read_list_ints_minus_one()
        b = ac.read_list_ints_minus_one()
        uf = UnionFind(n)

        root = [0] * n
        for x in a:
            root[x] += 1
        uf.size1 = root[:]

        root = [0] * n
        for x in b:
            root[x] += 1
        uf.size2 = root[:]

        ans = 0
        for val in ww:
            w, i = val // m, val % m
            u, v = uu[i], vv[i]
            if not uf.is_connected(u, v):
                u, v = uf.find(u), uf.find(v)
                c = min(uf.size1[u], uf.size2[v])
                ans += c * w
                uf.size1[u] -= c
                uf.size2[v] -= c
                c = min(uf.size1[v], uf.size2[u])
                ans += c * w
                uf.size1[v] -= c
                uf.size2[u] -= c
                uf.union_right(u, v)
                uf.size1[v] = uf.size1[u] + uf.size1[v]
                uf.size2[v] = uf.size2[u] + uf.size2[v]
                uf.size1[u] = uf.size2[u] = 0
        ac.st(ans)
        return

    @staticmethod
    def cf_2020d(ac=FastIO()):
        """
        url: https://codeforces.com/contest/2020/problem/D
        tag: union_find|union_right
        """
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            dct = [[] for _ in range(11)]
            for _ in range(m):
                a, d, k = ac.read_list_ints()
                dct[d].append((a, k))
            uf = UnionFind(n + 1)
            for d in range(1, 11):
                cur_uf = UnionFind(n + 1)
                for a, k in dct[d]:
                    node = a
                    while node + d <= a + k * d:
                        cur_uf.union_right(node, node + d)
                        node = cur_uf.find(node + d)
                for i in range(n):
                    uf.union(i, cur_uf.find(i))
            ac.st(uf.part - 1)
        return

    @staticmethod
    def cf_2021e2(ac=FastIO()):
        """
        url: https://codeforces.com/contest/2021/problem/E2
        tag: tree_dp|bag_dp|union_dp|brain_teaser|classical
        """
        for _ in range(ac.read_int()):
            n, m, p = ac.read_list_ints()
            s = ac.read_list_ints_minus_one()
            inf = 10 ** 15
            edges = []
            for _ in range(m):
                u, v, w = ac.read_list_ints_minus_one()
                edges.append((w + 1, u, v))
            edges.sort()
            size = [0] * (n + 1)
            sub = [inf] * (n + 1) * (n + 1)
            for x in s:
                size[x] = 1
                sub[x * (n + 1) + 1] = 0
            for i in range(n):
                sub[i * (n + 1)] = 0
            uf = UnionFindGeneral(n)
            uf.size = size[:]
            for w, i, j in edges:
                i = uf.find(i)
                j = uf.find(j)
                if i != j:
                    cur = [inf] * (uf.size[i] + uf.size[j] + 1)
                    for x in range(uf.size[i] + 1):
                        for y in range(uf.size[j] + 1):
                            if x and y:
                                cur[x + y] = min(cur[x + y], sub[i * (n + 1) + x] + sub[j * (n + 1) + y])
                            elif x:
                                cur[x + y] = min(cur[x + y],
                                                 sub[i * (n + 1) + x] + sub[j * (n + 1) + y] + w * uf.size[j])
                            elif y:
                                cur[x + y] = min(cur[x + y],
                                                 sub[i * (n + 1) + x] + sub[j * (n + 1) + y] + w * uf.size[i])
                            else:
                                cur[x + y] = 0
                    uf.union(i, j)
                    j = uf.find(j)
                    for x in range(uf.size[j] + 1):
                        sub[j * (n + 1) + x] = cur[x]

                    if uf.size[j] == p:
                        for x in range(uf.size[j] + 1, n + 1):
                            sub[j * (n + 1) + x] = 0
                        ac.lst([sub[j * (n + 1) + x] for x in range(1, n + 1)])
                        break
        return
