
from collections import Counter
from algorithm.src.fast_io import FastIO


"""

算法：贪心、逆向思维、抽屉原理、鸽巢原理、容斥原理、自定义排序、思维、脑筋急转弯
功能：各种可证明不可证明的头脑风暴
题目：

===================================力扣===================================
2499. 让数组不相等的最小总代价（https://leetcode.cn/problems/minimum-total-cost-to-make-arrays-unequal/）利用鸽巢原理贪心计算最小代价
2449. 使数组相似的最少操作次数（https://leetcode.cn/problems/minimum-total-cost-to-make-arrays-unequal/）转换题意进行排序后用奇偶数贪心变换得到
2448. 使数组相等的最小开销（https://leetcode.cn/problems/minimum-cost-to-make-array-equal/）利用中位数的特点变换到带权重广义下中位数的位置是最优的贪心进行增减
2412. 完成所有交易的初始最少钱数（https://leetcode.cn/problems/minimum-money-required-before-transactions/）根据交易增长特点进行自定义排序
2366. 将数组排序的最少替换次数（https://leetcode.cn/problems/minimum-replacements-to-sort-the-array/）倒序贪心不断分解得到满足要求且尽可能大的值
2350. 不可能得到的最短骰子序列（https://leetcode.cn/problems/shortest-impossible-sequence-of-rolls/）脑筋急转弯本质上是求全排列出现的轮数
2344. 使数组可以被整除的最少删除次数（https://leetcode.cn/problems/minimum-deletions-to-make-array-divisible/）利用最大公约数贪心删除最少的元素
2136. 全部开花的最早一天（https://leetcode.cn/problems/earliest-possible-day-of-full-bloom/）贪心安排成长时间最长的先种
2071. 你可以安排的最多任务数目（https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/）使用贪心加二分进行极值判断
517. 超级洗衣机（https://leetcode.cn/problems/super-washing-machines/）类似上题，计算最小的左右移动次数以及往左右的移动次数
1798. 你能构造出连续值的最大数目（https://leetcode.cn/problems/maximum-number-of-consecutive-values-you-can-make/）看似背包实则贪心
625. 最小因式分解（https://leetcode.cn/problems/minimum-factorization/）贪心进行因式分解，类似质因数分解
6360. 最小无法得到的或值（https://leetcode.cn/problems/minimum-impossible-or/）脑筋急转弯贪心，可以根据暴力打表观察规律
6361. 修改两个元素的最小分数（https://leetcode.cn/problems/minimum-score-by-changing-two-elements/）脑筋急转弯贪心
6316. 重排数组以得到最大前缀分数（https://leetcode.cn/contest/weekly-contest-336/problems/rearrange-array-to-maximize-prefix-score/）贪心，加前缀和
2436. 使子数组最大公约数大于一的最小分割数（https://leetcode.cn/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/）贪心计算
1029. 两地调度（https://leetcode.cn/problems/two-city-scheduling/）经典贪心题目，可使用举例两个计算、再进行归纳确定排序规则

===================================洛谷===================================
P1031 均分纸牌（https://www.luogu.com.cn/problem/P1031）贪心计算每个点的前缀和流量，需要补齐或者输出时进行计数
P1684 考验（https://www.luogu.com.cn/problem/P1684）线性贪心满足条件即增加计数
P1658 购物（https://www.luogu.com.cn/problem/P1658）看似背包实则贪心
P2001 硬币的面值（https://www.luogu.com.cn/problem/P2001）看似背包实则贪心
P1620 漂亮字串（https://www.luogu.com.cn/problem/P1620）分类讨论进行贪心
P2773 漂亮字串（https://www.luogu.com.cn/problem/P2773）分类讨论进行贪心
P2255 [USACO14JAN]Recording the Moolympics S（https://www.luogu.com.cn/problem/P2255）两个指针进行贪心
P2327 [SCOI2005]扫雷（https://www.luogu.com.cn/problem/P2327）脑筋急转弯进行枚举
P2777 [AHOI2016初中组]自行车比赛（https://www.luogu.com.cn/problem/P2777）贪心枚举最佳得分组合，加前后缀记录最大值
P2649 游戏预言（https://www.luogu.com.cn/problem/P2649）贪心，输的时候输最惨，赢的时候微弱优势
P1367 蚂蚁（https://www.luogu.com.cn/problem/P1367）脑筋急转弯，蚂蚁的相对移动位置排序还是不变
P1362 兔子数（https://www.luogu.com.cn/problem/P1362）找规律之后，进行广度优先搜索枚举
P1090 [NOIP2004 提高组] 合并果子 / [USACO06NOV] Fence Repair G（https://www.luogu.com.cn/record/list?user=739032&status=12&page=11）从小到大贪心合并
P1334 瑞瑞的木板（https://www.luogu.com.cn/problem/P1334）逆向思维的合并果子，从小到大合并
P1325 雷达安装（https://www.luogu.com.cn/problem/P1325）排序后进行贪心修建更新
P1250 种树（https://www.luogu.com.cn/problem/P1250）区间的贪心题，使用线段树修改区间与查询和，以及二分进行计算
P1230 智力大冲浪（https://www.luogu.com.cn/problem/P1230）排序后进行选取贪心
P1159 排行榜（https://www.luogu.com.cn/problem/P1159）使用队列贪心进行模拟
P1095 [NOIP2007 普及组] 守望者的逃离（https://www.luogu.com.cn/problem/P1095）贪心模拟也可以理解为动态规划转移
P1056 [NOIP2008 普及组] 排座椅（https://www.luogu.com.cn/record/list?user=739032&status=12&page=14）根据题意进行计数排序贪心选择
P8847 [JRKSJ R5] 1-1 A（https://www.luogu.com.cn/problem/P8847）分类讨论和贪心进行
P8845 [传智杯 #4 初赛] 小卡和质数（https://www.luogu.com.cn/problem/solution/P8845）脑筋急转弯，只有2是偶数质数
P2772 寻找平面上的极大点（https://www.luogu.com.cn/problem/P2772）按照两个维度排序，再按照其中一个维度顺序比较最大值
P2878 [USACO07JAN] Protecting the Flowers S（https://www.luogu.com.cn/problem/P2878）经典贪心题目，可使用举例两个计算、再进行归纳确定排序规则
P2920 [USACO08NOV]Time Management S（https://www.luogu.com.cn/problem/P2920）排序后进行贪心计算
P2983 [USACO10FEB]Chocolate Buying S（https://www.luogu.com.cn/problem/P2983）看起来是背包其实是贪心优先选择最便宜的奶牛满足
P3173 [HAOI2009]巧克力（https://www.luogu.com.cn/problem/P3173）从大到小排序进行贪心计算
P5098 [USACO04OPEN]Cave Cows 3（https://www.luogu.com.cn/problem/P5098）贪心按照一个维度排序后再按照另一个维度分类讨论，记录前缀最小值
P5159 WD与矩阵（https://www.luogu.com.cn/problem/P5159）利用异或的特点枚举计数并进行快速幂计算
P5497 [LnOI2019SP]龟速单项式变换(SMT)（https://www.luogu.com.cn/problem/P5497）抽屉原理进行分类讨论
P5682 [CSP-J2019 江西] 次大值（https://www.luogu.com.cn/problem/P5682）脑筋急转弯进行排序后贪心枚举确定
P5804 [SEERC2019]Absolute Game（https://www.luogu.com.cn/problem/P5804）排序贪心枚举和二分查找优化
P5963 [BalticOI ?] Card 卡牌游戏【来源请求】（https://www.luogu.com.cn/problem/P5963）经典贪心题目，可使用举例两个计算、再进行归纳确定排序规则
P6023 走路（https://www.luogu.com.cn/problem/P6023）可证明集中在某天是最佳结果，然后使用指针进行模拟计算
P6243 [USACO06OPEN]The Milk Queue G（https://www.luogu.com.cn/problem/P6243）经典贪心举例之后进行优先级比较，再自定义排序
P6179 [USACO15DEC]High Card Wins S（https://www.luogu.com.cn/problem/list?difficulty=3&page=13）经典贪心
P6380 『MdOI R2』Mayuri（https://www.luogu.com.cn/problem/P6380）贪心模拟进行赋值
P6446 [COCI2010-2011#1] TABOVI（https://www.luogu.com.cn/problem/P6446）贪心进行操作，经典使得数组所有值相等的最少操作次数变形题目，每次操作可以使得连续区间加1或者减1
P5019 [NOIP2018 提高组] 铺设道路（https://www.luogu.com.cn/problem/P5019）贪心进行操作，经典使得数组所有值相等的最少操作次数变形题目，每次操作可以使得连续区间加1或者减1
P6462 [传智杯 #2 决赛] 补刀（https://www.luogu.com.cn/problem/P6462）贪心进行分类计算
P6549 [COCI2010-2011#2] KNJIGE（https://www.luogu.com.cn/problem/P6549）逆向思维，使用插入排序的思想进行模拟
P6785 「EZEC-3」排列（https://www.luogu.com.cn/problem/P6785）脑筋急转弯进行，条件判断与贪心计数
P6851 onu（https://www.luogu.com.cn/problem/P6851）贪心模拟，均从大到小排序，先选择赢的牌，再计算输的牌
P7176 [COCI2014-2015#4] PRIPREME（https://www.luogu.com.cn/problem/P7176）贪心策略，结论题
P7228 [COCI2015-2016#3] MOLEKULE（https://www.luogu.com.cn/problem/P7228）脑筋急转弯贪心加树形dfs计算
P7260 [COCI2009-2010#3] RAZGOVOR（https://www.luogu.com.cn/problem/P7260）贪心与动态规划，经典使得数组所有值从0变化等于给定升序数组的最少操作次数，每次操作可以使得连续区间加1
P7319 「PMOI-4」生成树（https://www.luogu.com.cn/problem/P7319）公式变形后使用排序不等式进行贪心计算
P7412 [USACO21FEB] Year of the Cow S（https://www.luogu.com.cn/problem/P7412）贪心，将问题转换为去掉最长的k-1个非零距离
P7522 ⎌ Nurture ⎌（https://www.luogu.com.cn/problem/P7522）进行分类贪心讨论
P7633 [COCI2010-2011#5] BRODOVI（https://www.luogu.com.cn/problem/P7633）使用埃氏筛法思想，进行模拟贪心计算
P7714 「EZEC-10」排列排序（https://www.luogu.com.cn/problem/P7714）经典子序列排序使得整体有序，使用前缀最大值与指针计数确认子数组分割点
P7787 [COCI2016-2017#6] Turnir（https://www.luogu.com.cn/problem/P7787）脑筋急转弯，借助完全二叉树的思想
P7813 谜（https://www.luogu.com.cn/problem/P7813）贪心计算最大选取值
P1031 [NOIP2002 提高组] 均分纸牌（https://www.luogu.com.cn/problem/P1031）经典线性均分纸牌问题
P2512 [HAOI2008]糖果传递（https://www.luogu.com.cn/problem/P2512）经典线性环形均分纸牌问题
122. 糖果传递（https://www.acwing.com/problem/content/124/）经典线性环形均分纸牌问题

================================CodeForces================================
https://codeforces.com/problemset/problem/1186/D（贪心取floor，再根据加和为0的特质进行补充加1成为ceil）
https://codeforces.com/contest/792/problem/C（分类进行贪心取数比较，取最长的返回结果）
https://codeforces.com/problemset/problem/166/E（思维模拟DP）
https://codeforces.com/problemset/problem/1025/C（脑筋急转弯）
https://codeforces.com/problemset/problem/1042/C（贪心分类模拟）
https://codeforces.com/problemset/problem/439/C（贪心分类讨论）
https://codeforces.com/problemset/problem/1283/E（贪心分类讨论）
https://codeforces.com/contest/1092/problem/C（脑筋急转弯思维分类题）
https://codeforces.com/problemset/problem/1280/B（脑筋急转弯思维分类题）
https://codeforces.com/problemset/problem/723/C（贪心模拟构造）
https://codeforces.com/problemset/problem/712/C（逆向思维反向模拟）
https://codeforces.com/problemset/problem/747/D（贪心模拟求解）
https://codeforces.com/problemset/problem/1148/D（贪心，自定义排序选择构造）
https://codeforces.com/contest/792/problem/C（分类进行贪心讨论）
https://codeforces.com/problemset/problem/830/A （按照影响区间排序，然后贪心分配时间）
C. Table Decorations（https://codeforces.com/problemset/problem/478/C）贪心结论题a<=b<=c则有min((a+b+c)//3, a+b)
A. Dreamoon Likes Coloring（https://codeforces.com/problemset/problem/1329/A）贪心+指针+模拟
D. Maximum Distributed Tree（https://codeforces.com/problemset/problem/1401/D）贪心dfs枚举经过边的路径计数
C. Make Palindrome（https://codeforces.com/problemset/problem/600/C）回文子串计数贪心
D. Slime（https://codeforces.com/problemset/problem/1038/D）贪心模拟，分类讨论
B. Color the Fence（https://codeforces.com/problemset/problem/349/B）贪心模拟
C. Number Game（https://codeforces.com/problemset/problem/1370/C）贪心模拟必胜态
E. Making Anti-Palindromes（https://codeforces.com/contest/1822/problem/E）贪心进行模拟计数


104. 货仓选址（https://www.acwing.com/problem/content/106/）中位数贪心
1536. 均分纸牌（https://www.acwing.com/problem/content/description/1538/）贪心均分纸牌
105. 七夕祭（https://www.acwing.com/problem/content/description/1538/）经典环形均分纸牌问题

参考：OI WiKi（xx）
"""

import math
import unittest


class Solution:
    def __int__(self):
        return

    @staticmethod
    def cf_1038d(ac=FastIO()):
        # 模板：分类讨论贪心模拟
        n = ac.read_int()
        nums = ac.read_list_ints()
        if n == 1:
            ac.st(nums[0])
            return
        if n == 2:
            ac.st(ac.max(nums[0] - nums[1], nums[1] - nums[0]))
            return
        zero = nums.count(0)
        if zero >= 2:
            ac.st(sum(abs(num) for num in nums))
        elif zero == 1:
            ac.st(sum(abs(num) for num in nums))
        else:
            if all(num > 0 for num in nums):
                ac.st(sum(nums) - 2 * min(nums))
            elif all(num < 0 for num in nums):
                ac.st(sum(abs(num) for num in nums) - 2 * min(abs(num) for num in nums))
            else:
                ac.st(sum(abs(num) for num in nums))
        return

    @staticmethod
    def main(ac=FastIO()):
        s = ac.read_str()
        cnt = Counter(s)
        n = len(s)
        double = []
        single = []
        for w in cnt:
            if cnt[w] % 2 == 0:
                x = cnt[w] // 2
                double.append([w, x])
            else:
                x = cnt[w] // 2
                if x:
                    double.append([w, x])
                single.append(w)
        if n % 2 == 0:
            single.sort()
            m = len(single)
            for i in range(m // 2):
                double.append([single[i], 1])
            double.sort(key=lambda it: it[0])
            ans = ""
            for w, c in double:
                ans += w * c
            ac.st(ans + ans[::-1])

        else:
            single.sort()
            m = len(single)
            for i in range(m // 2):
                double.append([single[i], 1])
            double.sort(key=lambda it: it[0])
            ans = ""
            for w, c in double:
                ans += w * c
            ac.st(ans + single[m // 2] + ans[::-1])
        return

    @staticmethod
    def lg_p2512(ac=FastIO()):
        # 模板：经典环形均分纸牌问题
        n = ac.read_int()
        nums = [ac.read_int() for _ in range(n)]
        m = sum(nums)//n
        x = 0
        pre = []
        for i in range(n):
            x += m - nums[i]
            pre.append(x)
        pre.sort()
        y = pre[n//2]
        ans = sum(abs(num-y) for num in pre)
        ac.st(ans)
        return

    @staticmethod
    def ac_105(ac=FastIO()):

        def check(nums):
            # 环形均分纸牌
            nn = len(nums)
            s = sum(nums)
            if s % nn:
                return -1
            mm = s // nn
            x = 0
            pre = []
            for i in range(nn):
                x += mm - nums[i]
                pre.append(x)
            pre.sort()
            y = pre[nn // 2]
            ans = sum(abs(num - y) for num in pre)
            return ans

        m, n, t = ac.read_ints()
        row = [0] * m
        col = [0] * n
        for _ in range(t):
            xx, yy = ac.read_ints_minus_one()
            row[xx] += 1
            col[yy] += 1
        ans1 = check(row)
        ans2 = check(col)
        if ans1 != -1 and ans2 != -1:
            ac.lst(["both", ans1 + ans2])
        elif ans1 != -1:
            ac.lst(["row", ans1])
        elif ans2 != -1:
            ac.lst(["column", ans2])
        else:
            ac.st("impossible")
        return


class BrainStorming:
    def __init__(self):
        return

    @staticmethod
    def minimal_coin_need(n, m, nums):

        nums += [m + 1]
        nums.sort()
        # 有 n 个可选取且无限的硬币，为了形成 1-m 所有组合需要的最少硬币个数
        if nums[0] != 1:
            return -1
        ans = sum_ = 0
        for i in range(n):
            nex = nums[i + 1] - 1
            nex = nex if nex < m else m
            x = math.ceil((nex - sum_) / nums[i])
            x = x if x >= 0 else 0
            ans += x
            sum_ += x * nums[i]
            if sum_ >= m:
                break
        return ans


class TestGeneral(unittest.TestCase):

    def test_brain_storming(self):
        bs = BrainStorming()
        n, m = 4, 20
        nums = [1, 2, 5, 10]
        assert bs.minimal_coin_need(n, m, nums) == 5
        return


if __name__ == '__main__':
    unittest.main()
