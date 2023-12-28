"""

Algorithm：dinic_max_flow
Description：dinic_max_flow

====================================LeetCode====================================

=====================================LuoGu======================================
P3376（https://www.luogu.com.cn/problem/P3376）dinic_max_flow
P1343（https://www.luogu.com.cn/problem/P1343）dinic_max_flow
P2740（https://www.luogu.com.cn/problem/P2740）dinic_max_flow
P1361（https://www.luogu.com.cn/problem/P1361）dinic_max_flow|min_cut
P2057（https://www.luogu.com.cn/problem/P2057）dinic_max_flow|min_cut
P1344（https://www.luogu.com.cn/problem/P1344）dinic_max_flow|min_cut
P1345（https://www.luogu.com.cn/problem/P1345）dinic_max_flow|min_cut
P2762（https://www.luogu.com.cn/problem/P2762）dinic_max_flow|min_cut|specific_plan
P3381（https://www.luogu.com.cn/problem/P3381）dinic_max_flow|min_cost
P4452（https://www.luogu.com.cn/problem/P4452）dinic_max_flow|min_cost
P2153（https://www.luogu.com.cn/problem/P2153）dinic_max_flow|min_cost
P2053（https://www.luogu.com.cn/problem/P2053）dinic_max_flow|min_cost
P2050（https://www.luogu.com.cn/problem/P2050）dinic_max_flow|min_cost

===================================CodeForces===================================


"""
import math
from collections import defaultdict

from src.graph.network_flow.template import DinicMaxflowMinCut, DinicMaxflowMinCost
from src.utils.fast_io import FastIO, inf


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lg_p3376(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3376
        tag: dinic_max_flow
        """
        n, m, s, t = ac.read_list_ints()
        flow = DinicMaxflowMinCut(n)
        graph = [defaultdict(int) for _ in range(n)]
        for _ in range(m):
            u, v, w = ac.read_list_ints()
            graph[u - 1][v - 1] += w
        for u in range(n):
            for v in graph[u]:
                flow.add_edge(u + 1, v + 1, graph[u][v])
        ans = flow.max_flow_min_cut(s, t)
        ac.st(ans)
        return

    @staticmethod
    def lg_p1343(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1343
        tag: dinic_max_flow
        """
        n, m, x = ac.read_list_ints()
        s, t = 1, n
        flow = DinicMaxflowMinCut(n)
        graph = [defaultdict(int) for _ in range(n)]
        for _ in range(m):
            u, v, w = ac.read_list_ints()
            graph[u - 1][v - 1] += w
        for u in range(n):
            for v in graph[u]:
                flow.add_edge(u + 1, v + 1, graph[u][v])
        ans = flow.max_flow_min_cut(s, t)
        if ans < 1:
            ac.st("Orz Ni Jinan Saint Cow!")
        else:
            ac.lst([ans, math.ceil(x / ans)])
        return

    @staticmethod
    def lg_p2740(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2740
        tag: dinic_max_flow
        """
        m, n = ac.read_list_ints()
        s, t = 1, n
        flow = DinicMaxflowMinCut(n)
        graph = [defaultdict(int) for _ in range(n)]
        for _ in range(m):
            u, v, w = ac.read_list_ints()
            graph[u - 1][v - 1] += w
        for u in range(n):
            for v in graph[u]:
                flow.add_edge(u + 1, v + 1, graph[u][v])
        ans = flow.max_flow_min_cut(s, t)
        ac.st(ans)
        return

    @staticmethod
    def lg_p1361(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1361
        tag: dinic_max_flow|min_cut
        """
        n = ac.read_int()
        a = ac.read_list_ints()
        b = ac.read_list_ints()
        s, t = 1, n + 2
        m = ac.read_int()
        flow = DinicMaxflowMinCut(n + 2 + m * 2)
        for i in range(n):
            flow.add_edge(s, i + 2, a[i])
            flow.add_edge(i + 2, t, b[i])
        ans = sum(a) + sum(b)
        for i in range(m):
            nums = ac.read_list_ints()
            c1, c2 = nums[1], nums[2]
            ans += c1 + c2
            flow.add_edge(s, n + 1 + i * 2 + 1 + 1, c1)
            flow.add_edge(n + 1 + i * 2 + 2 + 1, t, c2)
            for j in nums[3:]:
                flow.add_edge(n + 1 + i * 2 + 1 + 1, j + 1, inf)
                flow.add_edge(j + 1, n + 1 + i * 2 + 2 + 1, inf)
        ac.st(ans - flow.max_flow_min_cut(s, t))
        return

    @staticmethod
    def lg_p2057(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2057
        tag: dinic_max_flow|min_cut
        """
        n, m = ac.read_list_ints()
        s, t = 1, n + 2
        a = ac.read_list_ints()
        flow = DinicMaxflowMinCut(n + 2)
        for i in range(n):
            if a[i]:
                flow.add_edge(s, i + 2, 1)
            else:
                flow.add_edge(i + 2, t, 1)

        for _ in range(m):
            x, y = ac.read_list_ints()
            flow.add_edge(x + 1, y + 1, 1)
            flow.add_edge(y + 1, x + 1, 1)
        ac.st(flow.max_flow_min_cut(s, t))
        return

    @staticmethod
    def lg_p1344(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1344
        tag: dinic_max_flow|min_cut
        """
        n, m = ac.read_list_ints()
        flow = DinicMaxflowMinCut(n)
        mod = 2023
        for _ in range(m):
            s, e, c = ac.read_list_ints()
            flow.add_edge(s, e, c * mod + 1)
        ans = flow.max_flow_min_cut(1, n)
        ac.lst([ans // mod, ans % mod])
        return

    @staticmethod
    def lg_p1345(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1345
        tag: dinic_max_flow|min_cut
        """
        n, m, s, t = ac.read_list_ints()
        flow = DinicMaxflowMinCut(n * 2)
        for i in range(1, n + 1):
            flow.add_edge(i * 2 - 1, i * 2, 1)
        for _ in range(m):
            x, y = ac.read_list_ints()
            flow.add_edge(x * 2, y * 2 - 1, inf)
            flow.add_edge(y * 2, x * 2 - 1, inf)
        ans = flow.max_flow_min_cut(2 * s, 2 * t - 1)
        ac.st(ans)
        return

    @staticmethod
    def lg_p2762(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2762
        tag: dinic_max_flow|min_cut|specific_plan
        """
        m, n = ac.read_list_ints()
        flow = DinicMaxflowMinCut(m + n + 2)
        ans = 0
        for i in range(1, m + 1):
            nums = ac.read_list_ints()
            ans += nums[0]
            flow.add_edge(1, i + 1, nums[0])
            for j in nums[1:]:
                flow.add_edge(i + 1, m + 1 + j, inf)
        cost = ac.read_list_ints()
        for j in range(1, n + 1):
            flow.add_edge(m + j + 1, m + n + 2, cost[j - 1])
        ans -= flow.max_flow_min_cut(1, m + n + 2)
        ac.lst([i - 1 for i in range(2, m + 2) if flow.depth[i] != -1])
        ac.lst([j - m - 1 for j in range(m + 2, m + n + 2) if flow.depth[j] != -1])
        ac.st(ans)
        return

    @staticmethod
    def lg_p3381(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3381
        tag: dinic_max_flow|min_cost
        """
        n, m, s, t = ac.read_list_ints()
        flow = DinicMaxflowMinCost(n)
        for i in range(1, m + 1):
            u, v, w, c = ac.read_list_ints()
            flow.add_edge(u, v, w, c)
        ac.lst(flow.max_flow_min_cost(s, t))
        return

    @staticmethod
    def lg_p4452(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4452
        tag: dinic_max_flow|min_cost
        """
        n, m, k, end = ac.read_list_ints()
        tt = [ac.read_list_ints() for _ in range(n)]
        f = [ac.read_list_ints() for _ in range(n)]
        queries = [ac.read_list_ints() for _ in range(m)]
        source, target, original = m * 2 + 1, m * 2 + 2, m * 2 + 3
        flow = DinicMaxflowMinCost(m * 2 + 3)
        flow.add_edge(original, source, k, 0)
        for i in range(1, m + 1):
            a, b, s, t, c = queries[i - 1]
            flow.add_edge(2 * i - 1, 2 * i, 1, -c)
            if tt[0][a] <= s:
                flow.add_edge(source, 2 * i - 1, inf, f[0][a])
            if t + tt[b][0] <= end:
                flow.add_edge(2 * i, target, inf, f[b][0])
        for i in range(1, m + 1):
            a1, b1, s1, t1, c1 = queries[i - 1]
            for j in range(1, m + 1):
                a2, b2, s2, t2, c2 = queries[j - 1]
                if t1 + tt[b1][a2] <= s2:
                    flow.add_edge(2 * i, 2 * j - 1, inf, f[b1][a2])
        _, min_cost = flow.max_flow_min_cost(original, target)
        ac.st(-min_cost)
        return

    @staticmethod
    def lg_p2153(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2153
        tag: dinic_max_flow|min_cost
        """
        n, m = ac.read_list_ints()
        flow = DinicMaxflowMinCost(n * 2)
        for _ in range(m):
            a, b, c = ac.read_list_ints()
            if a == 1 and b == n:
                flow.add_edge(a * 2, b * 2 - 1, 1, c)
            else:
                flow.add_edge(a * 2, b * 2 - 1, inf, c)
        for i in range(2, n):
            flow.add_edge(i * 2 - 1, i * 2, 1, 0)
        ac.lst(flow.max_flow_min_cost(2, 2 * n - 1))
        return

    @staticmethod
    def lg_p2053(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2053
        tag: dinic_max_flow|min_cost
        """
        m, n = ac.read_list_ints()
        flow = DinicMaxflowMinCost(m * n + n + 2)
        for i in range(1, n + 1):
            flow.add_edge(m * n + n + 1, m * n + i, 1, 0)
            cost = ac.read_list_ints()
            for j in range(1, m + 1):
                for k in range(1, n + 1):
                    flow.add_edge(m * n + i, (j - 1) * n + k, 1, k * cost[j - 1])
        for j in range(1, m + 1):
            for k in range(1, n + 1):
                flow.add_edge((j - 1) * n + k, m * n + n + 2, 1, 0)

        max_flow, min_cost = flow.max_flow_min_cost(m * n + n + 1, m * n + n + 2)
        assert max_flow == n
        ac.st("%.2f" % (min_cost / n))
        return

    @staticmethod
    def lg_p2050(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P2050
        tag: dinic_max_flow|min_cost
        """
        n, m = ac.read_list_ints()
        p = ac.read_list_ints()
        np = sum(p)
        flow = DinicMaxflowMinCost(m * np + n + 2)

        for i in range(1, n + 1):
            flow.add_edge(m * np + n + 1, m * np + i, p[i - 1], 0)
            cost = ac.read_list_ints()
            for j in range(1, m + 1):
                for k in range(1, np + 1):
                    flow.add_edge(m * np + i, (j - 1) * np + k, 1, k * cost[j - 1])
        for j in range(1, m + 1):
            for k in range(1, np + 1):
                flow.add_edge((j - 1) * np + k, m * np + n + 2, 1, 0)

        max_flow, min_cost = flow.max_flow_min_cost(m * np + n + 1, m * np + n + 2)
        assert max_flow == np
        ac.st(min_cost)
        return