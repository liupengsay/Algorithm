"""

Algorithm：scc|2-sat|largest_circle|smallest_circle
Description：scc|dag|shrink_point|topological_sort|strongly_connected_component
Example：path pass the most points which can be duplicated
2-SAT：giving n sets, each with two elements, in which (a, b) indicating that a and b are contradictory (where a and b belong to different sets), then select an element from each set and determine if a total of n pairwise non-contradictory elements can be selected

====================================LeetCode====================================

=====================================LuoGu======================================
P4782（https://www.luogu.com.cn/problem/P4782）2-sat|scc|classical
P5782（https://www.luogu.com.cn/problem/P5782）2-sat|scc|classical
P4171（https://www.luogu.com.cn/problem/P4171）2-sat|scc|classical

===================================CodeForces===================================
1438C（https://codeforces.com/problemset/problem/1438/C）2-sat|scc|classical
776D（https://codeforces.com/problemset/problem/776/D）union_find|classical|2-sat


"""

from src.graph.tarjan.template import Tarjan
from src.util.fast_io import FastIO


class TwoSAT:
    def __init__(self):
        return

    @staticmethod
    def lg_p4782(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4782
        tag: 2-sat|scc|classical
        """
        n, m = ac.read_list_ints()
        edge = [set() for _ in range(2 * n)]
        for _ in range(m):
            i, a, j, b = ac.read_list_ints()
            i -= 1
            j -= 1
            if i * 2 + 1 - a != j * 2 + b:
                edge[i * 2 + 1 - a].add(j * 2 + b)
            if j * 2 + 1 - b != i * 2 + a:
                edge[j * 2 + 1 - b].add(i * 2 + a)

        _, scc_node_id, _ = Tarjan().get_scc(2 * n, [list(s) for s in edge])
        for s in scc_node_id:
            pre = set()
            for node in s:
                if node // 2 in pre:
                    ac.st("IMPOSSIBLE")
                    return
                pre.add(node // 2)

        ac.st("POSSIBLE")
        ans = [0] * n
        pre = set()
        for s in scc_node_id:
            for node in s:
                i = node // 2
                if i not in pre:
                    ans[i] = node % 2
                pre.add(i)
        ac.lst(ans)
        return

    @staticmethod
    def lg_p5782(ac=FastIO()):
        """
        url:https://www.luogu.com.cn/problem/P5782
        tag: 2-sat|scc|classical
        """
        n, m = ac.read_list_ints()
        edge = [set() for _ in range(4 * n)]
        for _ in range(m):
            a, b = ac.read_list_ints_minus_one()
            edge[a * 2 + 1].add(b * 2)
            edge[b * 2 + 1].add(a * 2)

        for i in range(n):
            a, b = 2 * i, 2 * i + 1
            edge[a * 2 + 1].add(b * 2)
            edge[a * 2].add(b * 2 + 1)
            edge[b * 2 + 1].add(a * 2)
            edge[b * 2].add(a * 2 + 1)

        _, scc_node_id, _ = Tarjan().get_scc(4 * n, [list(s) for s in edge])
        for s in scc_node_id:
            pre = set()
            for node in s:
                if node // 2 in pre:
                    ac.st("NIE")
                    return
                pre.add(node // 2)

        ans = [0] * 2 * n
        pre = set()
        for s in scc_node_id:
            for node in s:
                i = node // 2
                if i not in pre:
                    ans[i] = node % 2
                pre.add(i)
        for i in range(2 * n):
            if ans[i]:
                ac.st(i + 1)
        return

    @staticmethod
    def lg_p4171(ac=FastIO()):
        """
        url: https://www.luogu.com.cn/problem/P4171
        tag: 2-sat|scc|classical
        """
        for _ in range(ac.read_int()):
            n, m = ac.read_list_ints()
            edge = [set() for _ in range(2 * n)]
            for _ in range(m):
                lst = ac.read_list_strs()
                i = int(lst[0][1:]) - 1
                j = int(lst[1][1:]) - 1
                a = 1 if lst[0][0] == "h" else 0
                b = 1 if lst[1][0] == "h" else 0
                if i * 2 + (1 - a) != j * 2 + b:
                    edge[i * 2 + (1 - a)].add(j * 2 + b)
                if j * 2 + (1 - b) != i * 2 + a:
                    edge[j * 2 + (1 - b)].add(i * 2 + a)

            _, scc_node_id, _ = Tarjan().get_scc(2 * n, [list(s) for s in edge])

            ans = True
            for s in scc_node_id:
                pre = set()
                for node in s:
                    if node // 2 in pre:
                        ans = False
                    pre.add(node // 2)
            ac.st("GOOD" if ans else "BAD")
        return

    @staticmethod
    def cf_1438c(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/1438/C
        tag: 2-sat|scc|classical
        """
        for _ in range(ac.read_int()):
            m, n = ac.read_list_ints()
            grid = [ac.read_list_ints() for _ in range(m)]
            edge = [set() for _ in range(2 * m * n)]
            for i in range(m):
                for j in range(n):
                    if i + 1 < m:
                        x, y = i * n + j, i * n + n + j
                        for a, b in [[0, 0], [0, 1], [1, 0], [1, 1]]:
                            if grid[i][j] + a == grid[i + 1][j] + b:
                                edge[x * 2 + a].add(y * 2 + 1 - b)
                                edge[y * 2 + b].add(x * 2 + 1 - a)
                    if j + 1 < n:
                        x, y = i * n + j, i * n + 1 + j
                        for a, b in [[0, 0], [0, 1], [1, 0], [1, 1]]:
                            if grid[i][j] + a == grid[i][j + 1] + b:
                                edge[x * 2 + a].add(y * 2 + 1 - b)
                                edge[y * 2 + b].add(x * 2 + 1 - a)
            for i in range(2 * m * n):
                if i in edge[i]:
                    edge[i].discard(i)
            _, scc_node_id, _ = Tarjan().get_scc(2 * m * n, [list(s) for s in edge])

            ans = [0] * m * n
            pre = set()
            for sc in scc_node_id:
                for node in sc:
                    i = node // 2
                    if i not in pre:
                        ans[i] = node % 2
                    pre.add(i)

            for x in range(m * n):
                grid[x // n][x % n] += ans[x]
            for g in grid:
                ac.lst(g)
        return

    @staticmethod
    def cf_776d(ac=FastIO()):
        """
        url: https://codeforces.com/problemset/problem/776/D
        tag: union_find|classical|2-sat
        """
        n, m = ac.read_list_ints()
        nums = ac.read_list_ints()
        key = [[] for _ in range(n)]
        dct = [set() for _ in range(2 * m)]
        for i in range(m):
            lst = ac.read_list_ints_minus_one()
            for x in lst[1:]:
                key[x].append(i)
        for x in range(n):
            a, b = key[x][0], key[x][1]
            if nums[x]:
                dct[a + m].add(b + m)
                dct[a].add(b)
                dct[b].add(a)
                dct[b + m].add(a + m)
            else:
                dct[a].add(b + m)
                dct[a + m].add(b)
                dct[b].add(a + m)
                dct[b + m].add(a)

        _, scc_node_id, _ = Tarjan().get_scc(2 * m, [list(e) for e in dct])
        for s in scc_node_id:
            pre = set()
            for node in s:
                if node - m in pre or node + m in pre:
                    ac.no()
                    return
                pre.add(node)
        ac.yes()
        return