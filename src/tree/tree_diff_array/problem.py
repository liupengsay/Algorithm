"""

Algorithm：lca|multiplication_method|tree_chain_split|tree_centroid|offline_lca|tree_diff_array
Description：tree_diff_array_edge|tree_diff_array_point

====================================LeetCode====================================
2646（https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/）offline_lca|tree_diff_array|counter|tree_dp

=====================================LuoGu======================================
P3128（https://www.luogu.com.cn/problem/P3128）offline_lca|tree_diff_array
P3258（https://www.luogu.com.cn/problem/P3258）offline_lca|tree_diff_array|tree_dp
P6869（https://www.luogu.com.cn/problem/P6869）offline_lca|tree_diff_array_edge|tree_diff_array_point

===================================CodeForces===================================
191C（https://codeforces.com/problemset/problem/191/C）tree_diff_array|tree_lca|implemention

====================================AtCoder=====================================
ABC309E（https://atcoder.jp/contests/abc309/tasks/abc309_e）tree_diff_array|dfs_order

=====================================AcWing=====================================


"""
from typing import List

from src.tree.tree_diff_array.template import TreeDiffArray
from src.tree.tree_dp.template import WeightedTree
from src.tree.tree_lca.template import OfflineLCA, UnionFindGetLCA
from src.util.fast_io import FastIO


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lc_2646(n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        """
        url: https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/
        tag: offline_lca|tree_diff_array|counter|tree_dp|classical
        """
        dct = [[] for _ in range(n)]
        for i, j in edges:
            dct[i].append(j)
            dct[j].append(i)

        res = OfflineLCA().bfs_iteration(dct, trips)

        m = len(trips)
        queries = [trips[i] + [res[i]] for i in range(m)]
        cnt = TreeDiffArray().bfs_iteration(dct, queries)

        stack = [0]
        sub = [[] for _ in range(n)]
        parent = [-1] * n
        while stack:
            i = stack.pop()
            if i >= 0:
                stack.append(~i)
                for j in dct[i]:
                    if j != parent[i]:
                        parent[j] = i
                        stack.append(j)
            else:
                i = ~i
                res = [cnt[i] * price[i], cnt[i] * price[i] // 2]
                for j in dct[i]:
                    if j != parent[i]:
                        a, b = sub[j]
                        res[0] += a if a < b else b
                        res[1] += a
                sub[i] = res

        return min(sub[0])

    @staticmethod
    def lg_p3128(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3128
        tag: offline_lca|tree_diff_array
        """
        n, k = ac.read_list_ints()
        dct = [[] for _ in range(n)]
        for _ in range(n - 1):
            i, j = ac.read_list_ints_minus_one()
            dct[i].append(j)
            dct[j].append(i)
        queries = [ac.read_list_ints_minus_one() for _ in range(k)]
        res = OfflineLCA().bfs_iteration(dct, queries)
        queries = [queries[i] + [res[i]] for i in range(k)]
        cnt = TreeDiffArray().bfs_iteration(dct, queries)
        ac.st(max(cnt))
        return

    @staticmethod
    def lg_p6869(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P6869
        tag: offline_lca|tree_diff_array_edge|tree_diff_array_point
        """
        n = ac.read_int()
        dct = [[] for _ in range(n)]
        cost = [dict() for _ in range(n)]
        for _ in range(n - 1):
            a, b, c1, c2 = ac.read_list_ints()
            a -= 1
            b -= 1
            cost[a][b] = cost[b][a] = [c1, c2]
            dct[a].append(b)
            dct[b].append(a)

        query = [[i, i + 1] for i in range(n - 1)]
        res = OfflineLCA().bfs_iteration(dct, query)
        for i in range(n - 1):
            query[i].append(res[i])
        diff = TreeDiffArray().bfs_iteration_edge(dct, query, 0)

        ans = 0
        stack = [0]
        parent = [-1] * n
        while stack:
            i = stack.pop()
            for j in dct[i]:
                if j != parent[i]:
                    stack.append(j)
                    parent[j] = i
                    cnt = diff[j]
                    c1, c2 = cost[i][j]
                    ans += min(cnt * c1, c2)
        ac.st(ans)
        return

    @staticmethod
    def lg_p3258(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3258
        tag: offline_lca|tree_diff_array|tree_dp
        """
        n = ac.read_int()
        nums = ac.read_list_ints_minus_one()
        root = nums[0]
        dct = [[] for _ in range(n)]
        for _ in range(n - 1):
            i, j = ac.read_list_ints_minus_one()
            dct[i].append(j)
            dct[j].append(i)

        stack = [root]
        parent = [-1] * n
        parent[root] = root
        while stack:
            i = stack.pop()
            for j in dct[i]:
                if j != parent[i]:
                    stack.append(j)
                    parent[j] = i
        tree = UnionFindGetLCA(parent, root)

        diff = [0] * n
        for i in range(1, n):
            u, v = nums[i - 1], nums[i]
            ancestor = tree.get_lca(u, v)
            if u != ancestor:
                u = parent[u]
                diff[u] += 1
                diff[v] += 1
                diff[ancestor] -= 1
                if parent[ancestor] != ancestor:
                    diff[parent[ancestor]] -= 1
            else:
                diff[v] += 1
                diff[u] -= 1

        stack = [root]
        while stack:
            i = stack.pop()
            if i >= 0:
                stack.append(~i)
                for j in dct[i]:
                    if j != parent[i]:
                        stack.append(j)
            else:
                i = ~i
                for j in dct[i]:
                    if j != parent[i]:
                        diff[i] += diff[j]
        diff[nums[0]] += 1
        diff[nums[-1]] -= 1
        for a in diff:
            ac.st(a)
        return

    @staticmethod
    def abc_309e(ac=FastIO()):
        """
        url: https://atcoder.jp/contests/abc309/tasks/abc309_e
        tag: tree_diff_array|dfs_order
        """
        n, m = ac.read_list_ints()
        dct = [[] for _ in range(n)]
        p = [0] + ac.read_list_ints_minus_one()
        for i in range(1, n):
            dct[p[i]].append(i)
        buy = [0] * n
        for _ in range(m):
            x, y = ac.read_list_ints()
            x -= 1
            buy[x] = max(buy[x], y + 1)
        diff = [0] * (n + 2)
        pre = [0] * (n + 2)
        stack = [(0, 1)]
        cur = [0] * n
        while stack:
            x, d = stack.pop()
            if x >= 0:
                stack.append((~x, d))
                diff[d] += 1
                if d + buy[x] < n + 2:
                    diff[d + buy[x]] -= 1
                pre[d] = diff[d] + pre[d - 1]
                cur[x] = pre[d]
                for y in dct[x]:
                    stack.append((y, d + 1))
            else:
                x = ~x
                pre[d] = 0
                diff[d] -= 1
                if d + buy[x] < n + 2:
                    diff[d + buy[x]] += 1
        ans = sum(x > 0 for x in cur)
        ac.st(ans)
        return

    @staticmethod
    def cf_191c(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/191/C
        tag: tree_diff_array|tree_lca|implemention
        """
        class Graph(WeightedTree):
            def diff_array_with_edge(self):
                # differential summation from bottom to top
                stack = [self.root]
                while stack:
                    u = stack.pop()
                    if u >= 0:
                        stack.append(~u)
                        for v in self.get_to_nodes(u):
                            if v != self.parent[u]:
                                stack.append(v)
                    else:
                        u = ~u
                        for v in self.get_to_nodes(u):
                            if v != self.parent[u]:
                                diff[u] += diff[v]
                return

        n = ac.read_int()
        graph = Graph(n)
        edges = []
        for _ in range(n - 1):
            i, j = ac.read_list_ints_minus_one()
            edges.append((i, j))
            graph.add_undirected_edge(i, j)
        graph.lca_build_with_multiplication()
        diff = [0] * n
        for _ in range(ac.read_int()):
            i, j = ac.read_list_ints_minus_one()
            lca = graph.lca_get_lca_between_nodes(i, j)
            # update the edge on the path u to ancestor and v to ancestor
            diff[i] += 1
            diff[j] += 1
            # make the down node represent the edge count
            diff[lca] -= 2
        graph.diff_array_with_edge()
        ans = [diff[i] if graph.parent[i] == j else diff[j] for i, j in edges]
        ac.lst(ans)
        return