


class SegTreeBrackets:
    def __init__(self, n, s):
        self.n = n
        self.s = s
        self.a = [0] * (2 * self.n)
        self.b = [0] * (2 * self.n)
        self.c = [0] * (2 * self.n)

    def build(self):
        for i in range(self.n):
            self.a[i + self.n] = 0
            self.b[i + self.n] = 1 if self.s[i] == "(" else 0
            self.c[i + self.n] = 1 if self.s[i] == ")" else 0
        for i in range(self.n - 1, 0, -1):
            t = min(self.b[i << 1], self.c[i << 1 | 1])
            self.a[i] = self.a[i << 1] + self.a[i << 1 | 1] + 2 * t
            self.b[i] = self.b[i << 1] + self.b[i << 1 | 1] - t
            self.c[i] = self.c[i << 1] + self.c[i << 1 | 1] - t

    def query(self, low, r):
        left = []
        right = []
        low += self.n
        r += self.n
        while low <= r:
            if low & 1:
                left.append([self.a[low], self.b[low], self.c[low]])
                low += 1
            if not r & 1:
                right.append([self.a[r], self.b[r], self.c[r]])
                r -= 1
            low >>= 1
            r >>= 1
        a1 = b1 = c1 = 0
        for a2, b2, c2 in left + right[::-1]:
            t = min(b1, c2)
            a1 += a2 + 2 * t
            b1 += b2 - t
            c1 += c2 - t
        return a1


class SegmentTreeRangeAddMax:
    # 模板：线段树区间更新、持续增加最大值
    def __init__(self, n):
        self.floor = 0
        self.height = [self.floor] * (4 * n)
        self.lazy = [self.floor] * (4 * n)

    @staticmethod
    def max(a, b):
        return a if a > b else b

    def push_down(self, i):
        # 懒标记下放，注意取最大值
        if self.lazy[i]:
            self.height[2 * i] = self.max(self.height[2 * i], self.lazy[i])
            self.height[2 * i + 1] = self.max(self.height[2 * i + 1], self.lazy[i])
            self.lazy[2 * i] = self.max(self.lazy[2 * i], self.lazy[i])
            self.lazy[2 * i + 1] = self.max(self.lazy[2 * i + 1], self.lazy[i])
            self.lazy[i] = self.floor
        return

    def update(self, left, right, s, t, val, i):
        # 更新区间最大值
        stack = [[s, t, i]]
        while stack:
            a, b, i = stack.pop()
            if i >= 0:
                if left <= a and b <= right:
                    self.height[i] = self.max(self.height[i], val)
                    self.lazy[i] = self.max(self.lazy[i], val)
                    continue
                self.push_down(i)
                stack.append([a, b, ~i])
                m = a + (b - a) // 2
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([a, m, 2 * i])
                if right > m:
                    stack.append([m + 1, b, 2 * i + 1])
            else:
                i = ~i
                self.height[i] = self.max(self.height[2 * i], self.height[2 * i + 1])
        return

    def query(self, left, right, s, t, i):
        # 查询区间的最大值
        stack = [[s, t, i]]
        highest = self.floor
        while stack:
            a, b, i = stack.pop()
            if left <= a and b <= right:
                highest = self.max(highest, self.height[i])
                continue
            self.push_down(i)
            m = a + (b - a) // 2
            if left <= m:
                stack.append([a, m, 2 * i])
            if right > m:
                stack.append([m + 1, b, 2 * i + 1])
        return highest


class SegmentTreeUpdateQueryMin:
    # 模板：线段树区间更新、持续减小最小值
    def __init__(self, n):
        self.height = [inf] * (4 * n)
        self.lazy = [inf] * (4 * n)
        self.n = n

    def build(self, nums: List[int]):
        # 使用数组初始化线段树
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, ind = stack.pop()
            if ind >= 0:
                if s == t:
                    self.make_tag(ind, nums[s])
                else:
                    stack.append([s, t, ~ind])
                    m = s + (t - s) // 2
                    stack.append([s, m, 2 * ind])
                    stack.append([m + 1, t, 2 * ind + 1])
            else:
                ind = ~ind
                self.push_up(ind)
        return

    def get(self):
        # 查询区间的所有值
        stack = [[0, self.n - 1, 1]]
        nums = [inf] * self.n
        while stack:
            s, t, i = stack.pop()
            if s == t:
                nums[s] = self.height[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i)
            stack.append([s, m, 2 * i])
            stack.append([m + 1, t, 2 * i + 1])
        return nums

    @staticmethod
    def min(a, b):
        return a if a < b else b

    def push_down(self, i):
        # 懒标记下放，注意取最小值
        if self.lazy[i] != inf:
            self.height[2 * i] = self.min(self.height[2 * i], self.lazy[i])
            self.height[2 * i + 1] = self.min(self.height[2 * i + 1], self.lazy[i])

            self.lazy[2 * i] = self.min(self.lazy[2 * i], self.lazy[i])
            self.lazy[2 * i + 1] = self.min(self.lazy[2 * i + 1], self.lazy[i])

            self.lazy[i] = inf
        return

    def make_tag(self, i, val):
        self.height[i] = self.min(self.height[i], val)
        self.lazy[i] = self.min(self.lazy[i], val)
        return

    def push_up(self, i):
        self.height[i] = self.min(self.height[2 * i], self.height[2 * i + 1])
        return

    def update_range(self, left, right, s, t, val, i):
        # 更新区间最小值
        stack = [[s, t, i]]
        while stack:
            a, b, i = stack.pop()
            if i >= 0:
                if left <= a and b <= right:
                    self.make_tag(i, val)
                    continue

                self.push_down(i)
                stack.append([a, b, ~i])
                m = a + (b - a) // 2
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([a, m, 2 * i])
                if right > m:
                    stack.append([m + 1, b, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def update_point(self, left, right, s, t, val, i):
        # 更新单点最小值
        while True:
            if left <= s and t <= right:
                self.make_tag(i, val)
                break
            self.push_down(i)
            m = s + (t - s) // 2
            if left <= m:  # 注意左右子树的边界与范围
                s, t, i = s, m, 2 * i
            if right > m:
                s, t, i = m + 1, t, 2 * i + 1

        while i > 1:
            i //= 2
            self.push_up(i)
        return

    def query_range(self, left, right, s, t, i):
        # 查询区间的最小值
        stack = [[s, t, i]]
        floor = inf
        while stack:
            a, b, i = stack.pop()
            if left <= a and b <= right:
                floor = self.min(floor, self.height[i])
                continue
            self.push_down(i)
            m = a + (b - a) // 2
            if left <= m:
                stack.append([a, m, 2 * i])
            if right > m:
                stack.append([m + 1, b, 2 * i + 1])
        return floor

    def query_point(self, left, right, s, t, i):
        # 查询单点的最小值
        a, b, i = s, t, i
        while True:
            if left <= a and b <= right:
                ans = self.height[i]
                break
            self.push_down(i)
            m = a + (b - a) // 2
            if left <= m:
                a, b, i = a, m, 2 * i
            if right > m:
                a, b, i = m + 1, b, 2 * i + 1
        return ans


class SegmentTreeRangeUpdateQuerySumMinMax:
    def __init__(self, n) -> None:
        # 模板：区间值增减、区间和查询、区间最小值查询、区间最大值查询
        self.n = n
        self.cover = [0] * (4 * self.n)  # 区间和
        self.lazy = [0] * (4 * self.n)  # 懒标记只能初始化为0
        self.floor = [0] * (4 * self.n)  # 最小值也可初始化为inf
        self.ceil = [0] * (4 * self.n)  # 最大值也可初始化为-inf
        return

    @staticmethod
    def max(a: int, b: int) -> int:
        return a if a > b else b

    @staticmethod
    def min(a: int, b: int) -> int:
        return a if a < b else b

    def build(self, nums: List[int]) -> None:
        # 使用数组初始化线段树
        assert self.n == len(nums)
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, ind = stack.pop()
            if ind >= 0:
                if s == t:
                    self.make_tag(ind, s, t, nums[s])
                else:
                    stack.append([s, t, ~ind])
                    m = s + (t - s) // 2
                    stack.append([s, m, 2 * ind])
                    stack.append([m + 1, t, 2 * ind + 1])
            else:
                ind = ~ind
                self.push_up(ind)
        return

    def push_down(self, i: int, s: int, m: int, t: int) -> None:
        # 下放懒标记
        if self.lazy[i]:
            self.cover[2 * i] += self.lazy[i] * (m - s + 1)
            self.cover[2 * i + 1] += self.lazy[i] * (t - m)

            self.floor[2 * i] += self.lazy[i]
            self.floor[2 * i + 1] += self.lazy[i]

            self.ceil[2 * i] += self.lazy[i]
            self.ceil[2 * i + 1] += self.lazy[i]

            self.lazy[2 * i] += self.lazy[i]
            self.lazy[2 * i + 1] += self.lazy[i]

            self.lazy[i] = 0

    def push_up(self, i) -> None:
        self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        self.ceil[i] = self.max(self.ceil[2 * i], self.ceil[2 * i + 1])
        self.floor[i] = self.min(self.floor[2 * i], self.floor[2 * i + 1])
        return

    def make_tag(self, i, s, t, val) -> None:
        self.cover[i] += val * (t - s + 1)
        self.floor[i] += val
        self.ceil[i] += val
        self.lazy[i] += val
        return

    def update_range(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 增减区间值 left 与 right 取值为 0 到 n-1 而 i 从 1 开始
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.make_tag(i, s, t, val)
                    continue

                m = s + (t - s) // 2
                self.push_down(i, s, m, t)
                stack.append([s, t, ~i])

                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def update_point(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 增减单点值 left 与 right 取值为 0 到 n-1 而 i 从 1 开始

        while True:
            if left <= s and t <= right:
                self.make_tag(i, s, t, val)
                break
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:  # 注意左右子树的边界与范围
                s, t, i = s, m, 2 * i
            if right > m:
                s, t, i = m + 1, t, 2 * i + 1
        while i > 1:
            i //= 2
            self.push_up(i)
        return

    def query_sum(self, left: int, right: int, s: int, t: int, i: int) -> int:
        # 查询区间的和
        stack = [[s, t, i]]
        ans = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans += self.cover[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans

    def query_min(self, left: int, right: int, s: int, t: int, i: int) -> int:
        # 查询区间的最小值
        stack = [[s, t, i]]
        highest = inf
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                highest = self.min(highest, self.floor[i])
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return highest

    def query_max(self, left: int, right: int, s: int, t: int, i: int) -> int:

        # 查询区间的最大值
        stack = [[s, t, i]]
        highest = -inf
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                highest = self.max(highest, self.ceil[i])
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return highest

    def get_all_nums(self) -> List[int]:
        # 查询区间的所有值
        stack = [[0, self.n - 1, 1]]
        nums = [0] * self.n
        while stack:
            s, t, i = stack.pop()
            if s == t:
                nums[s] = self.cover[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            stack.append([s, m, 2 * i])
            stack.append([m + 1, t, 2 * i + 1])
        return nums


class SegmentTreeRangeChangeQuerySumMinMax:
    def __init__(self, nums):
        # 模板：区间值修改、区间和查询、区间最小值查询、区间最大值查询
        self.n = len(nums)
        self.nums = nums
        self.cover = [0] * (4 * self.n)  # 区间和
        self.lazy = [inf] * (4 * self.n)  # 懒标记只能初始化为inf
        self.floor = [0] * (4 * self.n)  # 最小值也可初始化为inf
        self.ceil = [0] * (4 * self.n)  # 最大值也可初始化为-inf
        self.build()  # 初始化数组

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a, b):
        return a if a < b else b

    def build(self):

        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, ind = stack.pop()
            if ind >= 0:
                if s == t:
                    self.make_tag(ind, s, t, self.nums[s])
                else:
                    stack.append([s, t, ~ind])
                    m = s + (t - s) // 2
                    stack.append([s, m, 2 * ind])
                    stack.append([m + 1, t, 2 * ind + 1])
            else:
                ind = ~ind
                self.push_up(ind)
        return

    def push_down(self, i, s, m, t):
        if self.lazy[i] != inf:
            self.cover[2 * i] = self.lazy[i] * (m - s + 1)
            self.cover[2 * i + 1] = self.lazy[i] * (t - m)

            self.floor[2 * i] = self.lazy[i]
            self.floor[2 * i + 1] = self.lazy[i]

            self.ceil[2 * i] = self.lazy[i]
            self.ceil[2 * i + 1] = self.lazy[i]

            self.lazy[2 * i] = self.lazy[i]
            self.lazy[2 * i + 1] = self.lazy[i]

            self.lazy[i] = inf

    def push_up(self, i) -> None:
        self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        self.ceil[i] = self.max(self.ceil[2 * i], self.ceil[2 * i + 1])
        self.floor[i] = self.min(self.floor[2 * i], self.floor[2 * i + 1])
        return

    def make_tag(self, i, s, t, val) -> None:
        self.cover[i] = val * (t - s + 1)
        self.floor[i] = val
        self.ceil[i] = val
        self.lazy[i] = val
        return

    def change(self, left, right, s, t, val, i):
        # 更新区间值
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.make_tag(i, s, t, val)
                    continue

                m = s + (t - s) // 2
                self.push_down(i, s, m, t)
                stack.append([s, t, ~i])

                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def change_point(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 增减单点值 left 与 right 取值为 0 到 n-1 而 i 从 1 开始

        while True:
            if left <= s and t <= right:
                self.make_tag(i, s, t, val)
                break
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:  # 注意左右子树的边界与范围
                s, t, i = s, m, 2 * i
            if right > m:
                s, t, i = m + 1, t, 2 * i + 1
        while i > 1:
            i //= 2
            self.push_up(i)
        return

    def query_sum(self, left, right, s, t, i):
        # 查询区间的和
        stack = [[s, t, i]]
        ans = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans += self.cover[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans

    def query_min(self, left, right, s, t, i):
        # 查询区间的最小值
        stack = [[s, t, i]]
        highest = inf
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                highest = self.min(highest, self.floor[i])
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return highest

    def query_max(self, left, right, s, t, i):

        # 查询区间的最大值
        stack = [[s, t, i]]
        highest = -inf
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                highest = self.max(highest, self.ceil[i])
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return highest

    def get_all_nums(self):
        # 查询区间的所有值
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, i = stack.pop()
            if s == t:
                self.nums[s] = self.cover[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            stack.append([s, m, 2 * i])
            stack.append([m + 1, t, 2 * i + 1])
        return


class SegmentTreeRangeChangeQuerySumMinMaxDefaultDict:
    def __init__(self):
        # 模板：区间值修改、区间和查询、区间最小值查询、区间最大值查询（动态开点线段树）
        self.cover = defaultdict(int)  # 区间和  # 注意初始化值
        self.lazy = defaultdict(int)  # 懒标记  # 注意初始化值
        self.floor = defaultdict(int)  # 最小值  # 注意初始化值
        self.ceil = defaultdict(int)  # 最大值  # 注意初始化值

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a, b):
        return a if a < b else b

    def push_down(self, i, s, m, t):
        if self.lazy[i]:
            self.cover[2 * i] = self.lazy[i] * (m - s + 1)
            self.cover[2 * i + 1] = self.lazy[i] * (t - m)

            self.floor[2 * i] = self.lazy[i]
            self.floor[2 * i + 1] = self.lazy[i]

            self.ceil[2 * i] = self.lazy[i]
            self.ceil[2 * i + 1] = self.lazy[i]

            self.lazy[2 * i] = self.lazy[i]
            self.lazy[2 * i + 1] = self.lazy[i]

            self.lazy[i] = 0

    def push_up(self, i) -> None:
        self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        self.ceil[i] = self.max(self.ceil[2 * i], self.ceil[2 * i + 1])
        self.floor[i] = self.min(self.floor[2 * i], self.floor[2 * i + 1])
        return

    def make_tag(self, i, s, t, val) -> None:
        self.cover[i] = val * (t - s + 1)
        self.floor[i] = val
        self.ceil[i] = val
        self.lazy[i] = val
        return

    def update_range(self, left, right, s, t, val, i):
        # 修改区间值
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.make_tag(i, s, t, val)
                    continue

                m = s + (t - s) // 2
                self.push_down(i, s, m, t)
                stack.append([s, t, ~i])

                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def update_point(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改单点值 left 与 right 取值为 0 到 n-1 而 i 从 1 开始

        while True:
            if left <= s and t <= right:
                self.make_tag(i, s, t, val)
                break
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:  # 注意左右子树的边界与范围
                s, t, i = s, m, 2 * i
            if right > m:
                s, t, i = m + 1, t, 2 * i + 1
        while i > 1:
            i //= 2
            self.push_up(i)
        return

    def query_sum(self, left, right, s, t, i):
        # 查询区间的和
        stack = [[s, t, i]]
        ans = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans += self.cover[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans

    def query_min(self, left, right, s, t, i):
        # 查询区间的最小值
        stack = [[s, t, i]]
        highest = inf
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                highest = self.min(highest, self.floor[i])
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return highest

    def query_max(self, left, right, s, t, i):

        # 查询区间的最大值
        stack = [[s, t, i]]
        highest = -inf
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                highest = self.max(highest, self.ceil[i])
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return highest


class SegmentTreeRangeUpdateQuerySum:
    def __init__(self, n) -> None:
        # 模板：区间修改、区间和查询
        self.n = n
        self.sum = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        return

    def push_up(self, i):
        # 合并区间的函数
        self.sum[i] = self.sum[2 * i] + self.sum[2 * i + 1]
        return

    def make_tag(self, s, t, i, val):
        self.sum[i] = val * (t - s + 1)
        self.lazy[i] = val
        return

    def push_down(self, i, s, m, t):
        if self.lazy[i]:
            self.make_tag(s, m, 2 * i, self.lazy[i])
            self.make_tag(m + 1, t, 2 * i + 1, self.lazy[i])
            self.lazy[i] = 0

    def update_range(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改点值 left == right 取值为 0 到 n-1 而 i 从 1 开始，直接修改到底
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.make_tag(s, t, i, val)
                    continue
                m = s + (t - s) // 2
                self.push_down(i, s, m, t)
                stack.append([s, t, ~i])
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def query_range(self, left: int, right: int, s: int, t: int, i: int):
        # 区间加和查询
        ans = 0
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans += self.sum[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:  # 注意左右子树的边界与范围
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans


class SegmentTreeRangeUpdateChangeQueryMax:
    def __init__(self, nums: List[int]) -> None:
        # 模板：区间值增减、区间值修改、区间最大值查询
        self.n = len(nums)
        self.nums = nums
        self.lazy = [[inf, 0]] * (4 * self.n)  # 懒标记
        self.ceil = [-inf] * (4 * self.n)  # 最大值
        self.build()  # 初始化线段树
        return

    @staticmethod
    def max(a: int, b: int) -> int:
        return a if a > b else b

    @staticmethod
    def min(a: int, b: int) -> int:
        return a if a < b else b

    def build(self) -> None:
        # 使用数组初始化线段树
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, ind = stack.pop()
            if ind >= 0:
                if s == t:
                    self.ceil[ind] = self.nums[s]
                else:
                    stack.append([s, t, ~ind])
                    m = s + (t - s) // 2
                    stack.append([s, m, 2 * ind])
                    stack.append([m + 1, t, 2 * ind + 1])
            else:
                ind = ~ind
                self.ceil[ind] = self.max(self.ceil[2 * ind], self.ceil[2 * ind + 1])
        return

    def push_down(self, i: int, s: int, m: int, t: int) -> None:
        # 下放懒标记
        if self.lazy[i] != [inf, 0]:
            a, b = self.lazy[i]  # 分别表示修改为 a 与 增加 b
            if a == inf:
                self.ceil[2 * i] += b
                self.ceil[2 * i + 1] += b
                self.lazy[2 * i] = [inf, self.lazy[2 * i][1] + b]
                self.lazy[2 * i + 1] = [inf, self.lazy[2 * i + 1][1] + b]
            else:
                self.ceil[2 * i] = a
                self.ceil[2 * i + 1] = a
                self.lazy[2 * i] = [a, 0]
                self.lazy[2 * i + 1] = [a, 0]
            self.lazy[i] = [inf, 0]

    def update(self, left: int, right: int, s: int, t: int, val: int, flag: int, i: int) -> None:
        # 增减区间值 left 与 right 取值为 0 到 n-1 而 i 从 1 开始
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    if flag == 1:
                        self.ceil[i] = val
                        self.lazy[i] = [val, 0]
                    elif self.lazy[i][0] != inf:
                        self.ceil[i] += val
                        self.lazy[i] = [self.lazy[i][0] + val, 0]
                    else:
                        self.ceil[i] += val
                        self.lazy[i] = [inf, self.lazy[i][1] + val]
                    continue

                m = s + (t - s) // 2
                self.push_down(i, s, m, t)
                stack.append([s, t, ~i])

                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.ceil[i] = self.max(self.ceil[2 * i], self.ceil[2 * i + 1])
        return

    def query_max(self, left: int, right: int, s: int, t: int, i: int) -> int:

        # 查询区间的最大值
        stack = [[s, t, i]]
        highest = -inf
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                highest = self.max(highest, self.ceil[i])
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return highest


class SegmentTreeOrUpdateAndQuery:
    def __init__(self):
        # 模板：区间按位或赋值、按位与查询
        self.cover = defaultdict(int)
        self.lazy = defaultdict(int)

    def push_down(self, i):
        if self.lazy[i]:
            self.cover[2 * i] |= self.lazy[i]
            self.cover[2 * i + 1] |= self.lazy[i]

            self.lazy[2 * i] |= self.lazy[i]
            self.lazy[2 * i + 1] |= self.lazy[i]

            self.lazy[i] = 0

    def update(self, left, r, s, t, val, i):
        if left <= s and t <= r:
            self.cover[i] |= val
            self.lazy[i] |= val
            return
        m = s + (t - s) // 2
        self.push_down(i)
        if left <= m:
            self.update(left, r, s, m, val, 2 * i)
        if r > m:
            self.update(left, r, m + 1, t, val, 2 * i + 1)
        self.cover[i] = self.cover[2 * i] & self.cover[2 * i + 1]
        return

    def query(self, left, r, s, t, i):
        if left <= s and t <= r:
            return self.cover[i]
        m = s + (t - s) // 2
        self.push_down(i)
        ans = (1 << 31) - 1
        if left <= m:
            ans &= self.query(left, r, s, m, 2 * i)
        if r > m:
            ans &= self.query(left, r, m + 1, t, 2 * i + 1)
        return ans


class SegmentTreeRangeUpdateXORSum:
    def __init__(self, n):
        # 模板：区间值01翻转与区间和查询
        self.n = n
        self.cover = [0] * (4 * self.n)  # 区间和
        self.lazy = [0] * (4 * self.n)  # 懒标记
        return

    def build(self, nums) -> None:
        # 使用数组初始化线段树
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    self.cover[i] = nums[s]
                else:
                    stack.append([s, t, ~i])
                    m = s + (t - s) // 2
                    stack.append([s, m, 2 * i])
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        return

    def push_down(self, i: int, s: int, m: int, t: int) -> None:
        if self.lazy[i]:
            self.cover[2 * i] = m - s + 1 - self.cover[2 * i]
            self.cover[2 * i + 1] = t - m - self.cover[2 * i + 1]

            self.lazy[2 * i] ^= self.lazy[i]  # 注意使用异或抵消查询
            self.lazy[2 * i + 1] ^= self.lazy[i]  # 注意使用异或抵消查询

            self.lazy[i] = 0
        return

    def update_range(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 增减区间值 left 与 right 取值为 0 到 n-1 而 i 从 1 开始
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.cover[i] = t - s + 1 - self.cover[i]
                    self.lazy[i] ^= val  # 注意使用异或抵消查询
                    continue

                m = s + (t - s) // 2
                self.push_down(i, s, m, t)
                stack.append([s, t, ~i])

                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        return

    def query_sum(self, left: int, right: int, s: int, t: int, i: int) -> int:
        # 查询区间的和
        stack = [[s, t, i]]
        ans = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans += self.cover[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans


class SegmentTreeRangeAddSum:
    def __init__(self):
        # 模板：区间值增减与区间和查询
        self.cover = defaultdict(int)
        self.lazy = defaultdict(int)

    def push_down(self, i, s, m, t):
        if self.lazy[i]:
            self.cover[2 * i] += self.lazy[i] * (m - s + 1)
            self.cover[2 * i + 1] += self.lazy[i] * (t - m)

            self.lazy[2 * i] += self.lazy[i]
            self.lazy[2 * i + 1] += self.lazy[i]

            self.lazy[i] = 0

    def update(self, left, r, s, t, val, i):
        if left <= s and t <= r:
            self.cover[i] += val * (t - s + 1)
            self.lazy[i] += val
            return
        m = s + (t - s) // 2
        self.push_down(i, s, m, t)
        if left <= m:
            self.update(left, r, s, m, val, 2 * i)
        if r > m:
            self.update(left, r, m + 1, t, val, 2 * i + 1)
        self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        return

    def query(self, left, r, s, t, i):
        if left <= s and t <= r:
            return self.cover[i]
        m = s + (t - s) // 2
        self.push_down(i, s, m, t)
        ans = 0
        if left <= m:
            ans += self.query(left, r, s, m, 2 * i)
        if r > m:
            ans += self.query(left, r, m + 1, t, 2 * i + 1)
        return ans


class SegmentTreeRangeAddMulSum:

    def __init__(self, p, n):
        self.p = p
        # 模板：区间值增减乘积与区间和查询
        self.cover = [0] * 4 * n
        self.lazy = [[] for _ in range(4 * n)]

    def push_down(self, i, s, m, t):

        if self.lazy[i]:
            for op, val in self.lazy[i]:
                if op == "add":
                    self.cover[2 * i] += val * (m - s + 1)
                    self.cover[2 * i + 1] += val * (t - m)

                    self.lazy[2 * i] += [[op, val]]
                    self.lazy[2 * i + 1] += [[op, val]]
                else:
                    self.cover[2 * i] *= val
                    self.cover[2 * i + 1] *= val

                    self.lazy[2 * i] += [[op, val]]
                    self.lazy[2 * i + 1] += [[op, val]]
                self.cover[2 * i] %= self.p
                self.cover[2 * i + 1] %= self.p

            self.lazy[i] = []

    def update(self, left, r, s, t, op, val, i):
        if left <= s and t <= r:
            if op == "add":
                self.cover[i] += val * (t - s + 1)
                self.lazy[i] += [["add", val]]
            else:
                self.cover[i] *= val
                self.lazy[i] += [["mul", val]]
            self.cover[i] %= self.p
            return
        m = s + (t - s) // 2
        self.push_down(i, s, m, t)
        if left <= m:
            self.update(left, r, s, m, op, val, 2 * i)
        if r > m:
            self.update(left, r, m + 1, t, op, val, 2 * i + 1)
        self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        self.cover[i] %= self.p
        return

    def query(self, left, r, s, t, i):
        if left <= s and t <= r:
            return self.cover[i]
        m = s + (t - s) // 2
        self.push_down(i, s, m, t)
        ans = 0
        if left <= m:
            ans += self.query(left, r, s, m, 2 * i)
        if r > m:
            ans += self.query(left, r, m + 1, t, 2 * i + 1)
        return ans


class SegmentTreeRangeUpdateSum:
    def __init__(self):
        # 模板：区间值修改与区间和查询
        self.cover = defaultdict(int)
        self.lazy = defaultdict(int)

    def push_down(self, i, s, m, t):
        if self.lazy[i]:
            self.cover[2 * i] = self.lazy[i] * (m - s + 1)
            self.cover[2 * i + 1] = self.lazy[i] * (t - m)

            self.lazy[2 * i] = self.lazy[i]
            self.lazy[2 * i + 1] = self.lazy[i]

            self.lazy[i] = 0

    def update(self, left, r, s, t, val, i):
        if left <= s and t <= r:
            self.cover[i] = val * (t - s + 1)
            self.lazy[i] = val
            return
        m = s + (t - s) // 2
        self.push_down(i, s, m, t)
        if left <= m:
            self.update(left, r, s, m, val, 2 * i)
        if r > m:
            self.update(left, r, m + 1, t, val, 2 * i + 1)
        self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        return

    def query(self, left, r, s, t, i):
        if left <= s and t <= r:
            return self.cover[i]
        m = s + (t - s) // 2
        self.push_down(i, s, m, t)
        ans = 0
        if left <= m:
            ans += self.query(left, r, s, m, 2 * i)
        if r > m:
            ans += self.query(left, r, m + 1, t, 2 * i + 1)
        return ans


class SegmentTreePointAddSumMaxMin:
    def __init__(self, n: int):
        # 索引从 1 开始
        self.n = n
        self.min = [0] * (n * 4)
        self.sum = [0] * (n * 4)
        self.max = [0] * (n * 4)

    # 将 idx 上的元素值增加 val
    def add(self, o: int, l: int, r: int, idx: int, val: int) -> None:
        # 索引从 1 开始
        if l == r:
            self.min[o] += val
            self.sum[o] += val
            self.max[o] += val
            return
        m = (l + r) // 2
        if idx <= m:
            self.add(o * 2, l, m, idx, val)
        else:
            self.add(o * 2 + 1, m + 1, r, idx, val)
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])
        self.max[o] = max(self.max[o * 2], self.max[o * 2 + 1])
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    # 返回区间 [L,R] 内的元素和
    def query_sum(self, o: int, l: int, r: int, L: int, R: int) -> int:
        # 索引从 1 开始
        if L <= l and r <= R:
            return self.sum[o]
        sum_ = 0
        m = (l + r) // 2
        if L <= m:
            sum_ += self.query_sum(o * 2, l, m, L, R)
        if R > m:
            sum_ += self.query_sum(o * 2 + 1, m + 1, r, L, R)
        return sum_

    # 返回区间 [L,R] 内的最小值
    def query_min(self, o: int, l: int, r: int, L: int, R: int) -> int:
        # 索引从 1 开始
        if L <= l and r <= R:
            return self.min[o]
        res = 10 ** 9 + 7
        m = (l + r) // 2
        if L <= m:
            res = min(res, self.query_min(o * 2, l, m, L, R))
        if R > m:
            res = min(res, self.query_min(o * 2 + 1, m + 1, r, L, R))
        return res

    # 返回区间 [L,R] 内的最大值
    def query_max(self, o: int, l: int, r: int, L: int, R: int) -> int:
        # 索引从 1 开始
        if L <= l and r <= R:
            return self.max[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res = max(res, self.query_max(o * 2, l, m, L, R))
        if R > m:
            res = max(res, self.query_max(o * 2 + 1, m + 1, r, L, R))
        return res


class SegmentTreeRangeChangeQueryOr:
    def __init__(self, n) -> None:
        # 模板：区间值与操作修改，区间值或查询
        self.n = n
        self.lazy = [0] * (4 * self.n)  # 懒标记与操作
        self.cover = [0] * (4 * self.n)  # 区间或操作初始值为 1
        return

    def make_tag(self, val: int, i: int) -> None:
        self.cover[i] = val
        self.lazy[i] = val
        return

    def push_down(self, i: int) -> None:
        # 下放懒标记
        if self.lazy[i]:
            self.make_tag(self.lazy[i], 2 * i)
            self.make_tag(self.lazy[i], 2 * i + 1)
            self.lazy[i] = 0

    def push_up(self, i: int) -> None:
        self.cover[i] = self.cover[2 * i] | self.cover[2 * i + 1]

    def update(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改区间值 left 与 right 取值为 0 到 n-1 而 i 从 1 开始
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.make_tag(val, i)
                    continue
                m = s + (t - s) // 2
                self.push_down(i)
                stack.append([s, t, ~i])

                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def query_or(self, left: int, right: int, s: int, t: int, i: int) -> int:
        # 查询区间的和
        stack = [[s, t, i]]
        ans = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans |= self.cover[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans


class SegmentTreeRangeUpdateMax:
    # 模板：持续修改区间值并求最大值，动态开点
    def __init__(self):
        self.height = defaultdict(lambda: float("-inf"))
        self.lazy = defaultdict(int)

    def push_down(self, i):
        # 懒标记下放，注意取最大值
        if self.lazy[i]:
            self.height[2 * i] = self.lazy[i]
            self.height[2 * i + 1] = self.lazy[i]

            self.lazy[2 * i] = self.lazy[i]
            self.lazy[2 * i + 1] = self.lazy[i]

            self.lazy[i] = 0
        return

    def update(self, l, r, s, t, val, i):
        # 更新区间最大值
        if l <= s and t <= r:
            self.height[i] = val
            self.lazy[i] = val
            return
        self.push_down(i)
        m = s + (t - s) // 2
        if l <= m:  # 注意左右子树的边界与范围
            self.update(l, r, s, m, val, 2 * i)
        if r > m:
            self.update(l, r, m + 1, t, val, 2 * i + 1)
        self.height[i] = self.height[2 * i] if self.height[2 * i] > self.height[2 * i + 1] else self.height[2 * i + 1]
        return

    def query(self, l, r, s, t, i):
        # 查询区间的最大值
        if l <= s and t <= r:
            return self.height[i]
        self.push_down(i)
        m = s + (t - s) // 2
        highest = float("-inf")
        if l <= m:
            cur = self.query(l, r, s, m, 2 * i)
            if cur > highest:
                highest = cur
        if r > m:
            cur = self.query(l, r, m + 1, t, 2 * i + 1)
            if cur > highest:
                highest = cur
        return highest


class SegmentTreeRangeUpdateMulQuerySum:
    def __init__(self, nums: List[int], p) -> None:
        # 模板：区间值增减、区间值乘法、区间值修改、区间最大值查询
        self.p = p
        self.n = len(nums)
        self.nums = nums
        self.lazy_add = [0] * (4 * self.n)  # 懒标记
        self.lazy_mul = [1] * (4 * self.n)  # 懒标记
        self.cover = [0] * (4 * self.n)  # 区间和
        self.build()  # 初始化线段树
        return

    @staticmethod
    def max(a: int, b: int) -> int:
        return a if a > b else b

    @staticmethod
    def min(a: int, b: int) -> int:
        return a if a < b else b

    def build(self) -> None:
        # 使用数组初始化线段树
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    self.cover[i] = self.nums[s]
                else:
                    stack.append([s, t, ~i])
                    m = s + (t - s) // 2
                    stack.append([s, m, 2 * i])
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        return

    def make_tag(self, s: int, t: int, x: int, flag: int, i: int) -> None:
        if flag == 1:  # 乘法
            self.lazy_mul[i] = (self.lazy_mul[i] * x) % self.p
            self.lazy_add[i] = (self.lazy_add[i] * x) % self.p
            self.cover[i] = (self.cover[i] * x) % self.p
        else:
            self.lazy_add[i] = (self.lazy_add[i] + x) % self.p
            self.cover[i] = (self.cover[i] + x * (t - s + 1)) % self.p
        return

    def push_down(self, i: int, s: int, m: int, t: int) -> None:
        # 下放懒标记
        if self.lazy_mul[i] != 1:
            self.make_tag(s, m, self.lazy_mul[i], 1, 2 * i)
            self.make_tag(m + 1, t, self.lazy_mul[i], 1, 2 * i + 1)
            self.lazy_mul[i] = 1

        if self.lazy_add[i] != 0:
            self.make_tag(s, m, self.lazy_add[i], 2, 2 * i)
            self.make_tag(m + 1, t, self.lazy_add[i], 2, 2 * i + 1)
            self.lazy_add[i] = 0

    def update(self, left: int, right: int, s: int, t: int, val: int, flag: int, i: int) -> None:
        # 增减区间值 left 与 right 取值为 0 到 n-1 而 i 从 1 开始
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    if flag == 1:
                        self.cover[i] = (self.cover[i] * val) % self.p
                        self.lazy_add[i] = (self.lazy_add[i] * val) % self.p
                        self.lazy_mul[i] = (self.lazy_mul[i] * val) % self.p
                    else:
                        self.cover[i] = (self.cover[i] + val * (t - s + 1)) % self.p
                        self.lazy_add[i] = (self.lazy_add[i] + val) % self.p
                    continue

                m = s + (t - s) // 2
                self.push_down(i, s, m, t)
                stack.append([s, t, ~i])

                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
                self.cover[i] %= self.p
        return

    def query_sum(self, left: int, right: int, s: int, t: int, i: int) -> int:
        # 查询区间的和
        stack = [[s, t, i]]
        ans = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans += self.cover[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans % self.p


class SegmentTreePointUpdateRangeMulQuery:
    def __init__(self, n, mod) -> None:
        # 模板：单点值修改、区间乘取模
        self.n = n
        self.mod = mod
        self.cover = [1] * (4 * self.n)  # 区间乘积取模
        return

    def update(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改单点值 left == right 取值为 0 到 n-1 而 i 从 1 开始
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.cover[i] = val
                    continue
                m = s + (t - s) // 2
                stack.append([s, t, ~i])
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.cover[i] = self.cover[2 * i] * self.cover[2 * i + 1]
                self.cover[i] %= self.mod
        return

    def query_mul(self, left: int, right: int, s: int, t: int, i: int) -> int:
        # 查询区间的乘积
        stack = [[s, t, i]]
        ans = 1
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans *= self.cover[i]
                ans %= self.mod
                continue
            m = s + (t - s) // 2
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans


class SegmentTreeRangeSubConSum:
    def __init__(self, nums: List[int]) -> None:
        # 模板：单点修改、区间最大连续子段和查询
        self.n = len(nums)
        self.nums = nums
        self.cover = [-inf] * (4 * self.n)
        self.left = [-inf] * (4 * self.n)
        self.right = [-inf] * (4 * self.n)
        self.sum = [0] * (4 * self.n)
        self.build()  # 初始化线段树
        return

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a: int, b: int) -> int:
        return a if a < b else b

    def check(self, a, b):
        if a >= 0 and b >= 0:
            return a + b
        return self.max(a, b)

    def push_up(self, i):
        # 合并区间的函数
        self.cover[i] = self.max(self.cover[2 * i], self.cover[2 * i + 1])
        self.cover[i] = self.max(self.cover[i], self.right[2 * i] + self.left[2 * i + 1])
        self.left[i] = self.max(self.left[2 * i], self.sum[2 * i] + self.left[2 * i + 1])
        self.right[i] = self.max(self.right[2 * i + 1], self.sum[2 * i + 1] + self.right[2 * i])
        self.sum[i] = self.sum[2 * i] + self.sum[2 * i + 1]
        return

    def build(self) -> None:
        # 使用数组初始化线段树
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    self.cover[i] = self.nums[s]
                    self.left[i] = self.nums[s]
                    self.right[i] = self.nums[s]
                    self.sum[i] = self.nums[s]
                    continue
                stack.append([s, t, ~i])
                m = s + (t - s) // 2
                stack.append([s, m, 2 * i])
                stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def update(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改点值 left == right 取值为 0 到 n-1 而 i 从 1 开始，直接修改到底
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.cover[i] = val
                    self.left[i] = val
                    self.right[i] = val
                    self.sum[i] = val
                    continue
                m = s + (t - s) // 2
                stack.append([s, t, ~i])
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def query_max(self, left: int, right: int, s: int, t: int, i: int):
        # 查询区间的最大连续和，注意这里是递归
        if left <= s and t <= right:
            return self.cover[i], self.left[i], self.right[i], self.sum[i]

        m = s + (t - s) // 2

        if right <= m:
            return self.query_max(left, right, s, m, 2 * i)
        if left > m:
            return self.query_max(left, right, m + 1, t, 2 * i + 1)

        res1 = self.query_max(left, right, s, m, 2 * i)
        res2 = self.query_max(left, right, m + 1, t, 2 * i + 1)

        # 参照区间递归方式
        res = [0] * 4
        res[0] = self.max(res1[0], res2[0])
        res[0] = self.max(res[0], res1[2] + res2[1])
        res[1] = self.max(res1[1], res1[3] + res2[1])
        res[2] = self.max(res2[2], res2[3] + res1[2])
        res[3] = res1[3] + res2[3]
        return res


class SegmentTreeRangeUpdateSubConSum:
    def __init__(self, nums: List[int]) -> None:
        # 模板：区间修改、区间最大连续子段和查询
        self.n = len(nums)
        self.nums = nums
        self.cover = [-inf] * (4 * self.n)
        self.left = [-inf] * (4 * self.n)
        self.right = [-inf] * (4 * self.n)
        self.sum = [0] * (4 * self.n)
        self.lazy = [inf] * (4 * self.n)
        self.build()  # 初始化线段树
        return

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a: int, b: int) -> int:
        return a if a < b else b

    def check(self, a, b):
        if a >= 0 and b >= 0:
            return a + b
        return self.max(a, b)

    def push_up(self, i):
        # 合并区间的函数
        self.cover[i] = self.max(self.cover[2 * i], self.cover[2 * i + 1])
        self.cover[i] = self.max(self.cover[i], self.right[2 * i] + self.left[2 * i + 1])
        self.left[i] = self.max(self.left[2 * i], self.sum[2 * i] + self.left[2 * i + 1])
        self.right[i] = self.max(self.right[2 * i + 1], self.sum[2 * i + 1] + self.right[2 * i])
        self.sum[i] = self.sum[2 * i] + self.sum[2 * i + 1]
        return

    def make_tag(self, s, t, i, val):
        self.sum[i] = val * (t - s + 1)
        self.cover[i] = val if val < 0 else val * (t - s + 1)
        self.left[i] = val if val < 0 else val * (t - s + 1)
        self.right[i] = val if val < 0 else val * (t - s + 1)
        self.lazy[i] = val
        return

    def push_down(self, i, s, m, t):
        if self.lazy[i] != inf:
            self.make_tag(s, m, 2 * i, self.lazy[i])
            self.make_tag(m + 1, t, 2 * i + 1, self.lazy[i])
            self.lazy[i] = inf

    def build(self) -> None:
        # 使用数组初始化线段树
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    self.cover[i] = self.nums[s]
                    self.left[i] = self.nums[s]
                    self.right[i] = self.nums[s]
                    self.sum[i] = self.nums[s]
                    continue
                stack.append([s, t, ~i])
                m = s + (t - s) // 2
                stack.append([s, m, 2 * i])
                stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def update(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改点值 left == right 取值为 0 到 n-1 而 i 从 1 开始，直接修改到底
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.cover[i] = val if val < 0 else val * (t - s + 1)
                    self.left[i] = val if val < 0 else val * (t - s + 1)
                    self.right[i] = val if val < 0 else val * (t - s + 1)
                    self.sum[i] = val * (t - s + 1)
                    self.lazy[i] = val
                    continue
                m = s + (t - s) // 2
                self.push_down(i, s, m, t)
                stack.append([s, t, ~i])
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def query_max(self, left: int, right: int, s: int, t: int, i: int):
        # 查询区间的最大连续和，注意这里是递归
        if left <= s and t <= right:
            return [self.cover[i], self.left[i], self.right[i], self.sum[i]]

        m = s + (t - s) // 2
        self.push_down(i, s, m, t)

        if right <= m:
            return self.query_max(left, right, s, m, 2 * i)
        if left > m:
            return self.query_max(left, right, m + 1, t, 2 * i + 1)

        res1 = self.query_max(left, right, s, m, 2 * i)
        res2 = self.query_max(left, right, m + 1, t, 2 * i + 1)

        # 参照区间递归方式
        res = [0] * 4
        res[0] = self.max(res1[0], res2[0])
        res[0] = self.max(res[0], res1[2] + res2[1])
        res[1] = self.max(res1[1], res1[3] + res2[1])
        res[2] = self.max(res2[2], res2[3] + res1[2])
        res[3] = res1[3] + res2[3]
        return res


class SegmentTreeRangeUpdateMin:
    # 模板：持续修改区间值并求最小值
    def __init__(self):
        self.height = defaultdict(lambda: float("inf"))
        self.lazy = defaultdict(int)

    def push_down(self, i):
        # 懒标记下放，注意取最大值
        if self.lazy[i]:
            self.height[2 * i] = self.lazy[i]
            self.height[2 * i + 1] = self.lazy[i]

            self.lazy[2 * i] = self.lazy[i]
            self.lazy[2 * i + 1] = self.lazy[i]

            self.lazy[i] = 0
        return

    def update(self, l, r, s, t, val, i):
        # 更新区间最大值
        if l <= s and t <= r:
            self.height[i] = val
            self.lazy[i] = val
            return
        self.push_down(i)
        m = s + (t - s) // 2
        if l <= m:  # 注意左右子树的边界与范围
            self.update(l, r, s, m, val, 2 * i)
        if r > m:
            self.update(l, r, m + 1, t, val, 2 * i + 1)
        self.height[i] = self.height[2 * i] if self.height[2 * i] < self.height[2 * i + 1] else self.height[2 * i + 1]
        return

    def query(self, l, r, s, t, i):
        # 查询区间的最大值
        if l <= s and t <= r:
            return self.height[i]
        self.push_down(i)
        m = s + (t - s) // 2
        highest = inf
        if l <= m:
            cur = self.query(l, r, s, m, 2 * i)
            if cur < highest:
                highest = cur
        if r > m:
            cur = self.query(l, r, m + 1, t, 2 * i + 1)
            if cur < highest:
                highest = cur
        return highest


class SegmentTreeRangeUpdateQuery:
    def __init__(self, n) -> None:
        # 模板：区间修改、单点值查询
        self.n = n
        self.lazy = [0] * (4 * self.n)
        return

    def push_down(self, i):
        if self.lazy[i]:
            self.lazy[2 * i] = self.lazy[2 * i + 1] = self.lazy[i]
            self.lazy[i] = 0

    def update(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改点值 left == right 取值为 0 到 n-1 而 i 从 1 开始
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                self.lazy[i] = val
                continue
            m = s + (t - s) // 2
            self.push_down(i)
            if left <= m:  # 注意左右子树的边界与范围
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return

    def query(self, left: int, right: int, s: int, t: int, i: int):
        # 查询单点值
        while not (left <= s and t <= right):
            m = s + (t - s) // 2
            self.push_down(i)
            if right <= m:
                s, t, i = s, m, 2 * i
            elif left > m:
                s, t, i = m + 1, t, 2 * i + 1
        return self.lazy[i]


class SegmentTreeRangeUpdateAvgDev:
    def __init__(self, n) -> None:
        # 模板：区间增减、区间平均值与区间方差
        self.n = n
        self.cover = [0] * (4 * self.n)
        self.cover_2 = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        return

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a: int, b: int) -> int:
        return a if a < b else b

    def push_up(self, i):
        # 合并区间的函数
        self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        self.cover_2[i] = self.cover_2[2 * i] + self.cover_2[2 * i + 1]
        return

    def make_tag(self, s, t, i, val):
        self.cover_2[i] += self.cover[i] * 2 * val + (t - s + 1) * val * val
        self.cover[i] += val * (t - s + 1)
        self.lazy[i] += val
        return

    def push_down(self, i, s, m, t):
        if self.lazy[i]:
            self.make_tag(s, m, 2 * i, self.lazy[i])
            self.make_tag(m + 1, t, 2 * i + 1, self.lazy[i])
            self.lazy[i] = 0

    def build(self, nums) -> None:
        # 使用数组初始化线段树
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    self.cover[i] = nums[s]
                    self.cover_2[i] = nums[s] * nums[s]
                    continue
                stack.append([s, t, ~i])
                m = s + (t - s) // 2
                stack.append([s, m, 2 * i])
                stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def update(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改点值 [left  right] 取值为 0 到 n-1 增加 val 而 i 从 1 开始，直接修改到底
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.make_tag(s, t, i, val)
                    continue
                m = s + (t - s) // 2
                self.push_down(i, s, m, t)
                stack.append([s, t, ~i])
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def query(self, left: int, right: int, s: int, t: int, i: int):
        # 查询区间和，与数组平方的区间和
        stack = [[s, t, i]]
        ans1 = ans2 = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans1 += self.cover[i]
                ans2 += self.cover_2[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return [ans1, ans2]


class SegmentTreePointChangeLongCon:
    def __init__(self, n) -> None:
        # 模板：单点修改，查找最长的01交替字符子串连续区间
        self.n = n
        self.cover = [0] * (4 * self.n)
        self.left_0 = [0] * (4 * self.n)
        self.left_1 = [0] * (4 * self.n)
        self.right_0 = [0] * (4 * self.n)
        self.right_1 = [0] * (4 * self.n)
        self.build()
        return

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a: int, b: int) -> int:
        return a if a < b else b

    def push_up(self, i, s, m, t):
        # 合并区间的函数
        self.cover[i] = self.max(self.cover[2 * i], self.cover[2 * i + 1])
        self.cover[i] = self.max(self.cover[i], self.right_0[2 * i] + self.left_1[2 * i + 1])
        self.cover[i] = self.max(self.cover[i], self.right_1[2 * i] + self.left_0[2 * i + 1])

        self.left_0[i] = self.left_0[2 * i]
        if self.left_0[2 * i] == m - s + 1:
            self.left_0[i] += self.left_0[2 * i + 1] if (m - s + 1) % 2 == 0 else self.left_1[2 * i + 1]

        self.left_1[i] = self.left_1[2 * i]
        if self.left_1[2 * i] == m - s + 1:
            self.left_1[i] += self.left_1[2 * i + 1] if (m - s + 1) % 2 == 0 else self.left_0[2 * i + 1]

        self.right_0[i] = self.right_0[2 * i + 1]
        if self.right_0[2 * i + 1] == t - m:
            self.right_0[i] += self.right_0[2 * i] if (t - m) % 2 == 0 else self.right_1[2 * i]

        self.right_1[i] = self.right_1[2 * i + 1]
        if self.right_1[2 * i + 1] == t - m:
            self.right_1[i] += self.right_1[2 * i] if (t - m) % 2 == 0 else self.right_0[2 * i]
        return

    def build(self) -> None:
        # 使用数组初始化线段树
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    self.cover[i] = 1
                    self.left_0[i] = 1
                    self.right_0[i] = 1
                    continue
                stack.append([s, t, ~i])
                m = s + (t - s) // 2
                stack.append([s, m, 2 * i])
                stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                m = s + (t - s) // 2
                self.push_up(i, s, m, t)
        return

    def update(self, left: int, right: int, s: int, t: int, i: int) -> None:
        # 修改点值 [left  right] 取值为 0 到 n-1 增加 val 而 i 从 1 开始，直接修改到底
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if left <= s and t <= right:
                    self.left_0[i] = 1 - self.left_0[i]
                    self.right_0[i] = 1 - self.right_0[i]
                    self.left_1[i] = 1 - self.left_1[i]
                    self.right_1[i] = 1 - self.right_1[i]
                    self.cover[i] = 1
                    continue
                m = s + (t - s) // 2
                stack.append([s, t, ~i])
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                m = s + (t - s) // 2
                self.push_up(i, s, m, t)
        return

    def query(self):
        return self.cover[1]


class SegmentTreeRangeAndOrXOR:
    def __init__(self, n) -> None:
        # 模板：区间修改成01或者翻转，区间查询最多有多少连续的1，以及总共有多少1
        self.n = n
        self.cover_1 = [0] * (4 * self.n)
        self.cover_0 = [0] * (4 * self.n)
        self.sum = [0] * (4 * self.n)
        self.left_1 = [0] * (4 * self.n)
        self.right_1 = [0] * (4 * self.n)
        self.left_0 = [0] * (4 * self.n)
        self.right_0 = [0] * (4 * self.n)
        self.lazy = [inf] * (4 * self.n)
        return

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a: int, b: int) -> int:
        return a if a < b else b

    def push_up(self, i, s, m, t):
        # 合并区间的函数
        self.cover_1[i] = self.max(self.cover_1[2 * i], self.cover_1[2 * i + 1])
        self.cover_1[i] = self.max(self.cover_1[i], self.right_1[2 * i] + self.left_1[2 * i + 1])

        self.cover_0[i] = self.max(self.cover_0[2 * i], self.cover_0[2 * i + 1])
        self.cover_0[i] = self.max(self.cover_0[i], self.right_0[2 * i] + self.left_0[2 * i + 1])

        self.sum[i] = self.sum[2 * i] + self.sum[2 * i + 1]

        self.left_1[i] = self.left_1[2 * i]
        if self.left_1[i] == m - s + 1:
            self.left_1[i] += self.left_1[2 * i + 1]

        self.left_0[i] = self.left_0[2 * i]
        if self.left_0[i] == m - s + 1:
            self.left_0[i] += self.left_0[2 * i + 1]

        self.right_1[i] = self.right_1[2 * i + 1]
        if self.right_1[i] == t - m:
            self.right_1[i] += self.right_1[2 * i]

        self.right_0[i] = self.right_0[2 * i + 1]
        if self.right_0[i] == t - m:
            self.right_0[i] += self.right_0[2 * i]

        return

    def make_tag(self, s, t, i, val):
        if val == 0:
            self.cover_1[i] = 0
            self.sum[i] = 0
            self.cover_0[i] = t - s + 1
            self.left_1[i] = self.right_1[i] = 0
            self.right_0[i] = self.left_0[i] = t - s + 1
        elif val == 1:
            self.cover_1[i] = t - s + 1
            self.cover_0[i] = 0
            self.sum[i] = t - s + 1
            self.left_1[i] = self.right_1[i] = t - s + 1
            self.right_0[i] = self.left_0[i] = 0
        else:
            self.cover_1[i], self.cover_0[i] = self.cover_0[i], self.cover_1[i]
            self.sum[i] = t - s + 1 - self.sum[i]
            self.left_0[i], self.left_1[i] = self.left_1[i], self.left_0[i]
            self.right_0[i], self.right_1[i] = self.right_1[i], self.right_0[i]
        self.lazy[i] = val
        return

    def push_down(self, i, s, m, t):
        if self.lazy[i] != inf:
            self.make_tag(s, m, 2 * i, self.lazy[i])
            self.make_tag(m + 1, t, 2 * i + 1, self.lazy[i])
            self.lazy[i] = inf

    def build(self, nums) -> None:
        # 使用数组初始化线段树
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if s == t:
                    if nums[s] == 0:
                        self.cover_1[i] = 0
                        self.sum[i] = 0
                        self.cover_0[i] = 1
                        self.left_1[i] = self.right_1[i] = 0
                        self.left_0[i] = self.right_0[i] = 1
                    else:
                        self.cover_1[i] = 1
                        self.sum[i] = 1
                        self.cover_0[i] = 0
                        self.left_1[i] = self.right_1[i] = 1
                        self.left_0[i] = self.right_0[i] = 0
                    continue
                stack.append([s, t, ~i])
                m = s + (t - s) // 2
                stack.append([s, m, 2 * i])
                stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                m = s + (t - s) // 2
                self.push_up(i, s, m, t)
        return

    def update(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改点值 [left  right] 取值为 0 到 n-1 增加 val 而 i 从 1 开始，直接修改到底
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                m = s + (t - s) // 2
                if s < t:
                    self.push_down(i, s, m, t)
                if left <= s and t <= right:
                    self.make_tag(s, t, i, val)
                    continue

                stack.append([s, t, ~i])
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                m = s + (t - s) // 2
                self.push_up(i, s, m, t)
        return

    def query_sum(self, left: int, right: int, s: int, t: int, i: int):
        # 查询区间和，与数组平方的区间和
        stack = [[s, t, i]]
        ans = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans += self.sum[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i, s, m, t)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans

    def query_max_length(self, left: int, right: int, s: int, t: int, i: int):
        # 查询区间的最大连续和，注意这里是递归
        if left <= s and t <= right:
            return self.cover_1[i], self.left_1[i], self.right_1[i]

        m = s + (t - s) // 2
        self.push_down(i, s, m, t)

        if right <= m:
            return self.query_max_length(left, right, s, m, 2 * i)
        if left > m:
            return self.query_max_length(left, right, m + 1, t, 2 * i + 1)

        res1 = self.query_max_length(left, right, s, m, 2 * i)
        res2 = self.query_max_length(left, right, m + 1, t, 2 * i + 1)

        # 参照区间递归方式
        res = [0] * 3
        res[0] = self.max(res1[0], res2[0])
        res[0] = self.max(res[0], res1[2] + res2[1])

        res[1] = res1[1]
        if res[1] == m - s + 1:
            res[1] += res2[1]

        res[2] = res2[2]
        if res[2] == t - m:
            res[2] += res1[2]
        return res


class SegmentTreeLongestSubSame:
    # 模板：单点字母更新，最长具有相同字母的连续子数组查询
    def __init__(self, n, lst):
        self.n = n
        self.lst = lst
        self.pref = [0] * 4 * n
        self.suf = [0] * 4 * n
        self.ceil = [0] * 4 * n
        self.build()
        return

    def build(self):
        # 使用数组初始化线段树
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, ind = stack.pop()
            if ind >= 0:
                if s == t:
                    self.make_tag(ind)
                else:
                    stack.append([s, t, ~ind])
                    m = s + (t - s) // 2
                    stack.append([s, m, 2 * ind])
                    stack.append([m + 1, t, 2 * ind + 1])
            else:
                ind = ~ind
                self.push_up(ind, s, t)
        return

    def make_tag(self, i):
        # 只有此时 i 对应的区间 s==t 才打标记
        self.pref[i] = 1
        self.suf[i] = 1
        self.ceil[i] = 1
        return

    def push_up(self, i, s, t):
        m = s + (t - s) // 2
        # 左右区间段分别为 [s, m] 与 [m+1, t] 保证 s < t
        self.pref[i] = self.pref[2 * i]
        if self.pref[2 * i] == m - s + 1 and self.lst[m] == self.lst[m + 1]:
            self.pref[i] += self.pref[2 * i + 1]

        self.suf[i] = self.suf[2 * i + 1]
        if self.suf[2 * i + 1] == t - m and self.lst[m] == self.lst[m + 1]:
            self.suf[i] += self.suf[2 * i]

        a = -inf
        for b in [self.pref[i], self.suf[i], self.ceil[2 * i], self.ceil[2 * i + 1]]:
            a = a if a > b else b
        if self.lst[m] == self.lst[m + 1]:
            b = self.suf[2 * i] + self.pref[2 * i + 1]
            a = a if a > b else b
        self.ceil[i] = a
        return

    def update_point(self, left, right, s, t, val, i):
        # 更新单点最小值
        self.lst[left] = val
        stack = []
        while True:
            stack.append([s, t, i])
            if left <= s <= t <= right:
                self.make_tag(i)
                break
            m = s + (t - s) // 2
            if left <= m:  # 注意左右子树的边界与范围
                s, t, i = s, m, 2 * i
            if right > m:
                s, t, i = m + 1, t, 2 * i + 1
        stack.pop()
        while stack:
            s, t, i = stack.pop()
            self.push_up(i, s, t)
        assert i == 1
        # 获取当前最大的连续子串
        return self.ceil[1]


class SegmentTreeRangeXORQuery:
    def __init__(self, n) -> None:
        # 模板：区间异或修改、单点异或查询
        self.n = n
        self.cover = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        return

    def push_up(self, i):
        # 合并区间的函数
        self.cover[i] = self.cover[2 * i] ^ self.cover[2 * i + 1]
        return

    def make_tag(self, i, val):
        self.cover[i] ^= val
        self.lazy[i] ^= val
        return

    def push_down(self, i):
        if self.lazy[i]:
            self.make_tag(2 * i, self.lazy[i])
            self.make_tag(2 * i + 1, self.lazy[i])
            self.lazy[i] = 0

    def update_range(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改点值 [left  right] 取值为 0 到 n-1 异或 val 而 i 从 1 开始
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                m = s + (t - s) // 2
                if left <= s and t <= right:
                    self.make_tag(i, val)
                    continue
                self.push_down(i)
                stack.append([s, t, ~i])
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.push_up(i)
        return

    def update_point(self, left: int, right: int, s: int, t: int, val: int, i: int) -> None:
        # 修改点值 [left  right] 取值为 0 到 n-1 异或 val 而 i 从 1 开始
        assert left == right
        while True:
            if left <= s and t <= right:
                self.make_tag(i, val)
                break
            self.push_down(i)
            m = s + (t - s) // 2
            if left <= m:  # 注意左右子树的边界与范围
                s, t, i = s, m, 2 * i
            if right > m:
                s, t, i = m + 1, t, 2 * i + 1
        while i > 1:
            i //= 2
            self.push_up(i)
        return

    def query(self, left: int, right: int, s: int, t: int, i: int):
        # 查询区间和，与数组平方的区间和
        stack = [[s, t, i]]
        ans = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans ^= self.cover[i]
                continue
            m = s + (t - s) // 2
            self.push_down(i)
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans

    def query_point(self, left: int, right: int, s: int, t: int, i: int):
        # 查询区间和，与数组平方的区间和
        assert left == right
        ans = 0
        while True:
            if left <= s and t <= right:
                ans ^= self.cover[i]
                break
            m = s + (t - s) // 2
            self.push_down(i)
            if left <= m:
                s, t, i = s, m, 2 * i
            if right > m:
                s, t, i = m + 1, t, 2 * i + 1
        return ans


class SegmentTreeRangeSqrtSum:
    def __init__(self, n):
        # 模板：区间值开方向下取整，区间和查询
        self.n = n
        self.cover = [0] * (4 * self.n)  # 区间和
        self.lazy = [inf] * (4 * self.n)  # 懒标记

    def build(self, nums):
        stack = [[0, self.n - 1, 1]]
        while stack:
            s, t, ind = stack.pop()
            if ind >= 0:
                if s == t:
                    self.cover[ind] = nums[s]
                else:
                    stack.append([s, t, ~ind])
                    m = s + (t - s) // 2
                    stack.append([s, m, 2 * ind])
                    stack.append([m + 1, t, 2 * ind + 1])
            else:
                ind = ~ind
                self.cover[ind] = self.cover[2 * ind] + self.cover[2 * ind + 1]
        return

    def change(self, left, right, s, t, i):
        # 更新区间值
        stack = [[s, t, i]]
        while stack:
            s, t, i = stack.pop()
            if i >= 0:
                if self.cover[i] == t - s + 1:
                    continue
                if s == t:
                    self.cover[i] = int(self.cover[i] ** 0.5)
                    continue
                stack.append([s, t, ~i])
                m = s + (t - s) // 2
                if left <= m:  # 注意左右子树的边界与范围
                    stack.append([s, m, 2 * i])
                if right > m:
                    stack.append([m + 1, t, 2 * i + 1])
            else:
                i = ~i
                self.cover[i] = self.cover[2 * i] + self.cover[2 * i + 1]
        return

    def query_sum(self, left, right, s, t, i):
        # 查询区间的和
        stack = [[s, t, i]]
        ans = 0
        while stack:
            s, t, i = stack.pop()
            if left <= s and t <= right:
                ans += self.cover[i]
                continue
            m = s + (t - s) // 2
            if left <= m:
                stack.append([s, m, 2 * i])
            if right > m:
                stack.append([m + 1, t, 2 * i + 1])
        return ans


