"""

Algorithm：floyd|several_source_shortest_path|undirected_graph|directed_graph|pos_weight|neg_weight|negative_circle
Description：shortest_path|longest_path|necessary_point_on_shortest_path|necessary_point_on_longest_path|necessary_edge
specific_plan： floyd need dp[i][j] where pre[i][j] = k, and bellman-ford dijkstra need pre[v] = u

====================================LeetCode====================================
2642（https://leetcode.cn/problems/design-graph-with-shortest-path-calculator/）floyd|dynamic_graph|shortest_path
1462（https://leetcode.cn/problems/course-schedule-iv/）transitive_closure|floyd

=====================================LuoGu======================================
P1119（https://www.luogu.com.cn/problem/P1119）offline_query|floyd|dynamic_graph
P1476（https://www.luogu.com.cn/problem/P1476）floyd|longest_path|specific_plan
P3906（https://www.luogu.com.cn/problem/P3906）floyd|shortest_path|specific_plan

P2009（https://www.luogu.com.cn/problem/P2009）floyd|shortest_path
P2419（https://www.luogu.com.cn/problem/P2419）floyd|topological_sort
P2910（https://www.luogu.com.cn/problem/P2910）shortest_path|floyd
P6464（https://www.luogu.com.cn/problem/P6464）brute_force|floyd|dynamic_graph
P6175（https://www.luogu.com.cn/problem/P6175）floyd|brute_force|O(n^3)|bfs|dijkstra
B3611（https://www.luogu.com.cn/problem/B3611）transitive_closure|floyd
P1613（https://www.luogu.com.cn/problem/P1613）floyd|several_floyd|shortest_path
P8312（https://www.luogu.com.cn/problem/P8312）limited_floyd|shortest_path|several_floyd
P8794（https://www.luogu.com.cn/problem/P8794）binary_search|floyd


===================================CodeForces===================================
472D（https://codeforces.com/problemset/problem/472/D）floyd|construction|shortest_path

====================================AtCoder=====================================
D - Candidates of No Shortest Paths（https://atcoder.jp/contests/abc051/tasks/abc051_d）floyd|shortest_path|necessary_edge|classical
D - Restoring Road Network（https://atcoder.jp/contests/abc074/tasks/arc083_b）shortest_path_spanning_tree|floyd|dynamic_graph
E - Travel by Car（https://atcoder.jp/contests/abc143/tasks/abc143_e）floyd|build_graph|shortest_path|several_floyd

=====================================AcWing=====================================
4872（https://www.acwing.com/problem/content/submission/4875/）floyd|reverse_thinking|shortest_path|reverse_graph

"""
from heapq import heappop, heappush
from math import inf
from typing import List

from src.basis.binary_search.template import BinarySearch
from src.graph.dijkstra.template import Dijkstra
from src.utils.fast_io import FastIO


class Solution:
    def __init__(self):
        return

    @staticmethod
    def lg_p1613(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1613
        tag: floyd|several_floyd|shortest_path
        """
        # Floyd动态规划，两遍shortest_path综合
        n, m = ac.read_list_ints()

        # dp[i][j][k] 表示 i 到 j 有无花费为 k 秒即距离为 2**k 的的路径
        dp = [[[0] * 32 for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            u, v = ac.read_list_ints_minus_one()
            dp[u][v][0] = 1
        for x in range(1, 32):
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if dp[i][k][x - 1] and dp[k][j][x - 1]:
                            dp[i][j][x] = 1

        # 建立距离二进制 1 的个数为 1 的有向图
        dis = [[inf] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for x in range(32):
                    if dp[i][j][x]:
                        dis[i][j] = 1
                        break

        # 第二遍 Floyd 求新距离意义上的shortest_path
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = ac.min(dis[i][j], dis[i][k] + dis[k][j])
        ac.st(dis[0][n - 1])

        return

    @staticmethod
    def ac_4872(ac=FastIO()):
        """
        url: https://www.acwing.com/problem/content/submission/4875/
        tag: floyd|reverse_thinking|shortest_path|reverse_graph
        """
        # Floyd逆序reverse_thinking更新shortest_path对
        n = ac.read_int()
        dp = [ac.read_list_ints() for _ in range(n)]
        a = ac.read_list_ints_minus_one()
        node = []
        ans = []
        for ind in range(n - 1, -1, -1):
            x = a[ind]
            node.append(x)
            cur = 0
            for i in node:
                for j in node:
                    dp[i][x] = ac.min(dp[i][x], dp[i][j] + dp[j][x])
                    dp[x][i] = ac.min(dp[x][i], dp[x][j] + dp[j][i])

            for i in node:
                for j in node:
                    dp[i][j] = ac.min(dp[i][j], dp[i][x] + dp[x][j])
                    cur += dp[i][j]
            ans.append(cur)

        ac.lst(ans[::-1])
        return

    @staticmethod
    def lg_p1119(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1119
        tag: offline_query|floyd|dynamic_graph
        """
        # 利用 Floyd 算法特点和修复的中转站更新最短距离（无向图）
        n, m = ac.read_list_ints()
        repair = ac.read_list_ints()
        # 设置初始值距离
        dis = [[inf] * n for _ in range(n)]
        for i in range(m):
            a, b, c = ac.read_list_ints()
            dis[a][b] = dis[b][a] = c
        for i in range(n):
            dis[i][i] = 0

        # 修复村庄之后用Floyd算法更新以该村庄为中转的距离
        k = 0
        for _ in range(ac.read_int()):
            x, y, t = ac.read_list_ints()
            # 离线算法
            while k < n and repair[k] <= t:
                # k修复则更新以k为中转站的距离
                for a in range(n):
                    for b in range(a + 1, n):
                        dis[a][b] = dis[b][a] = ac.min(dis[a][k] + dis[k][b], dis[b][a])
                k += 1
            if dis[x][y] < inf and x < k and y < k:
                ac.st(dis[x][y])
            else:
                ac.st(-1)
        return

    @staticmethod
    def lg_p1476(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1476
        tag: floyd|longest_path|specific_plan
        """
        # Floyd 求索引从 1 到 n 的最长路并求所有在最长路上的点（有向图）
        n = ac.read_int() + 1
        m = ac.read_int()
        dp = [[-inf] * (n + 1) for _ in range(n + 1)]
        for _ in range(m):
            i, j, k = ac.read_list_ints()
            dp[i][j] = k
        for i in range(n + 1):
            dp[i][i] = 0

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for k in range(1, n + 1):
                    if dp[i][j] < dp[i][k] + dp[k][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]

        length = dp[1][n]
        path = []
        for i in range(1, n + 1):
            if dp[1][i] + dp[i][n] == dp[1][n]:
                path.append(i)
        ac.st(length)
        ac.lst(path)
        return

    @staticmethod
    def lg_p3906(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P3906
        tag: floyd|shortest_path|specific_plan
        """
        # Floyd 求索引从 u 到 v 的shortest_path并求所有在shortest_path上的点（无向图）
        n, m = ac.read_list_ints()
        dp = [[inf] * (n + 1) for _ in range(n + 1)]
        for _ in range(m):
            i, j = ac.read_list_ints()
            dp[i][j] = dp[j][i] = 1
        for i in range(1, n + 1):
            dp[i][i] = 0

        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(i + 1, n + 1):  # 无向图这里就可以优化
                    dp[j][i] = dp[i][j] = ac.min(dp[i][j], dp[i][k] + dp[k][j])

        for _ in range(ac.read_int()):
            u, v = ac.read_list_ints()
            dis = min(dp[u][k] + dp[k][v] for k in range(1, n + 1))
            ac.lst([x for x in range(1, n + 1) if dp[u][x] + dp[x][v] == dis])
        return

    @staticmethod
    def lg_b3611(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/B3611
        tag: transitive_closure|floyd
        """
        # transitive_closure模板题
        n = ac.read_int()
        dp = [ac.read_list_ints() for _ in range(n)]
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][k] and dp[k][j]:
                        dp[i][j] = 1
        for g in dp:
            ac.lst(g)
        return

    @staticmethod
    def abc_51d_1(ac=FastIO()):
        # brain_teaserFloydshortest_path的必经边，也可直接Dijkstra
        n, m = ac.read_list_ints()
        dp = [[inf] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        edges = [ac.read_list_ints() for _ in range(m)]
        for i, j, w in edges:
            i -= 1
            j -= 1
            dp[i][j] = dp[j][i] = w

        for k in range(n):  # 中间节点
            for i in range(n):  # 起始节点
                for j in range(i + 1, n):  # 结束节点
                    a, b = dp[i][j], dp[i][k] + dp[k][j]
                    dp[i][j] = dp[j][i] = a if a < b else b
        ans = 0
        for i, j, w in edges:
            i -= 1
            j -= 1
            if dp[i][j] < w:  # 如果最短距离小于该边则必然不经过该边
                ans += 1
        ac.st(ans)
        return

    @staticmethod
    def abc_51d_2(ac=FastIO()):
        # brain_teaserFloydshortest_path的必经边，也可直接Dijkstra
        n, m = ac.read_list_ints()
        edges = [ac.read_list_ints() for _ in range(m)]
        dct = [[] for _ in range(n)]
        for i, j, w in edges:
            i -= 1
            j -= 1
            dct[i].append([j, w])
            dct[j].append([i, w])
        dis = []
        for i in range(n):
            dis.append(Dijkstra().get_dijkstra_result(dct, i))
        ans = 0
        for i, j, w in edges:
            i -= 1
            j -= 1
            if dis[i][j] < w:
                ans += 1
        ac.st(ans)
        return

    @staticmethod
    def abc_74d(ac=FastIO()):
        # shortest_path生成图，Floyd维护最小生成图
        n = ac.read_int()
        grid = [ac.read_list_ints() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] != grid[j][i]:
                    ac.st(-1)
                    return
            if grid[i][i]:
                ac.st(-1)
                return

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([i, j, grid[i][j]])
        edges.sort(key=lambda it: it[2])
        ans = 0
        dis = [[inf] * n for _ in range(n)]
        for i in range(n):
            dis[i][i] = 0
        # 逐渐更新最短距离
        for i, j, w in edges:
            if dis[i][j] < grid[i][j]:
                ac.st(-1)
                return
            if dis[i][j] == w:
                continue
            ans += w
            for x in range(n):
                for y in range(x + 1, n):
                    a, b = dis[x][y], dis[x][i] + w + dis[j][y]
                    a = a if a < b else b
                    b = dis[x][j] + w + dis[i][y]
                    a = a if a < b else b
                    dis[x][y] = dis[y][x] = a
        ac.st(ans)
        return

    @staticmethod
    def abc_143e(ac=FastIO()):
        # Floydbuild_graph|shortest_path，两种shortest_path，建两次图
        n, m, ll = ac.read_list_ints()
        dct = [[] for _ in range(n)]
        dis = [[inf] * n for _ in range(n)]
        for i in range(n):
            dis[i][i] = 0
        for _ in range(m):
            x, y, z = ac.read_list_ints()
            x -= 1
            y -= 1
            dct[x].append([y, z])
            dct[y].append([x, z])
            a, b = dis[x][y], z
            dis[x][y] = dis[y][x] = a if a < b else b

        for k in range(n):
            for i in range(n):
                for j in range(i + 1, n):
                    cur = dis[i][k] + dis[k][j]
                    if cur < dis[i][j]:
                        dis[i][j] = dis[j][i] = cur

        dp = [[inf] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
            for j in range(i + 1, n):
                if dis[i][j] <= ll:
                    dp[i][j] = dp[j][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(i + 1, n):
                    cur = dp[i][k] + dp[k][j] + 1
                    if cur < dp[i][j]:
                        dp[i][j] = dp[j][i] = cur

        for _ in range(ac.read_int()):
            x, y = ac.read_list_ints_minus_one()
            ans = dp[x][y]
            ac.st(ans if ans < inf else -1)
        return

    @staticmethod
    def cf_472d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/472/D
        tag: floyd|construction|shortest_path
        """
        #  Floyd 的思想判断shortest_path矩阵是否合理存在
        n = ac.read_int()
        grid = [ac.read_list_ints() for _ in range(n)]
        for i in range(n):
            if grid[i][i]:
                ac.st("NO")
                return
            for j in range(i + 1, n):
                if grid[i][j] != grid[j][i] or not grid[i][j]:
                    ac.st("NO")
                    return
        if n == 1:
            ac.st("YES")
            return
        for i in range(n):
            r = 1 if not i else 0
            for j in range(n):
                if grid[i][j] < grid[i][r] and i != j:
                    r = j
            for k in range(n):
                if abs(grid[i][k] - grid[r][k]) != grid[i][r]:
                    ac.st("NO")
                    return
        ac.st("YES")
        return

    @staticmethod
    def lg_p1613(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P1613
        tag: floyd|several_floyd|shortest_path
        """
        # 建立新图Floydshortest_path
        n, m = ac.read_list_ints()

        # 表示节点i与j之间距离为2^k的路径是否存在
        dp = [[[0] * 32 for _ in range(n)] for _ in range(n)]
        for _ in range(m):
            u, v = ac.read_list_ints_minus_one()
            dp[u][v][0] = 1

        # 结合倍增思想Floyd建新图
        for x in range(1, 32):
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if dp[i][k][x - 1] and dp[k][j][x - 1]:
                            dp[i][j][x] = 1

        dis = [[inf] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for x in range(32):
                    if dp[i][j][x]:
                        dis[i][j] = 1
                        break

        # Floyd新图shortest_path
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = ac.min(dis[i][j], dis[i][k] + dis[k][j])
        ac.st(dis[0][n - 1])
        return

    @staticmethod
    def lg_p8312(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8312
        tag: limited_floyd|shortest_path|several_floyd
        """
        # 最多k条边的shortest_path跑k遍Floyd
        n, m = ac.read_list_ints()
        dis = [[inf] * n for _ in range(n)]
        for i in range(n):
            dis[i][i] = 0

        for _ in range(m):
            a, b, c = ac.read_list_ints_minus_one()
            c += 1
            dis[a][b] = ac.min(dis[a][b], c)

        dct = [d[:] for d in dis]
        k, q = ac.read_list_ints()
        nums = [ac.read_list_ints_minus_one() for _ in range(q)]
        k = ac.min(k, n)
        for _ in range(k - 1):
            cur = [d[:] for d in dis]
            for p in range(n):
                for i in range(n):
                    for j in range(n):
                        cur[i][j] = ac.min(cur[i][j], dis[i][p] + dct[p][j])
            dis = [d[:] for d in cur]

        for c, d in nums:
            res = dis[c][d]
            ac.st(res if res < inf else -1)
        return

    @staticmethod
    def lg_p8794(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P8794
        tag: binary_search|floyd
        """

        # binary_search|Floyd

        def get_dijkstra_result_mat(mat: List[List[int]], src: int) -> List[float]:
            # 模板: Dijkstra求shortest_path，变成负数求可以求最长路（还是正权值）
            len(mat)
            dis = [inf] * n
            stack = [[0, src]]
            dis[src] = 0
            visit = set(list(range(n)))
            while stack:
                d, ii = heappop(stack)
                if dis[ii] < d:
                    continue
                visit.discard(ii)
                for j in visit:
                    dj = mat[ii][j] + d
                    if dj < dis[j]:
                        dis[j] = dj
                        heappush(stack, [dj, j])
            return dis

        n, q = ac.read_list_ints()
        grid = [ac.read_list_ints() for _ in range(n)]
        lower = [ac.read_list_ints() for _ in range(n)]
        ans = 0
        for i in range(n):
            ans += sum(get_dijkstra_result_mat(lower, i))
        if ans > q:
            ac.st(-1)
            return

        ans = 0
        for i in range(n):
            ans += sum(get_dijkstra_result_mat(grid, i))
        if ans <= q:
            ac.st(0)
            return

        def check(x):
            cnt = [x // n] * n
            for y in range(x % n):
                cnt[y] += 1
            cur = [[0] * n for _ in range(n)]
            for a in range(n):
                for b in range(n):
                    cur[a][b] = ac.max(lower[a][b], grid[a][b] - cnt[a] - cnt[b])
            dis = 0
            for y in range(n):
                dis += sum(get_dijkstra_result_mat(cur, y))
            return dis <= q

        def check2(x):
            cnt = [x // n] * n
            for y in range(x % n):
                cnt[y] += 1
            cur = [[0] * n for _ in range(n)]
            for a in range(n):
                for b in range(n):
                    cur[a][b] = ac.max(lower[a][b], grid[a][b] - cnt[a] - cnt[b])
            # Floyd全源shortest_path
            for k in range(n):
                for a in range(n):
                    for b in range(a + 1, n):
                        cur[a][b] = cur[b][a] = ac.min(cur[a][b], cur[a][k] + cur[k][b])
            return sum(sum(c) for c in cur) <= q

        low = 1
        high = n * 10 ** 5
        BinarySearch().find_int_left(low, high, check)
        ans = BinarySearch().find_int_left(low, high, check2)
        ac.st(ans)
        return
