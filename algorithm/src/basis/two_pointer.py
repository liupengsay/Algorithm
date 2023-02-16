import unittest

"""
算法：双指针、快慢指针、先后指针、桶计数
功能：通过相对移动，来减少计算复杂度，分为同向双指针，相反双指针，以及中心扩展法

题目：

===================================力扣===================================
259. 较小的三数之和（https://leetcode.cn/problems/3sum-smaller/）使用双指针或者计数枚举的方式
2444. 统计定界子数组的数目（https://leetcode.cn/problems/count-subarrays-with-fixed-bounds/）通向双指针的移动来根据两个指针的位置来进行计数
2398. 预算内的最多机器人数目（https://leetcode.cn/problems/maximum-number-of-robots-within-budget/）同向双指针移动的条件限制有两个需要用有序集合来维护滑动窗口过程
2302. 统计得分小于 K 的子数组数目（https://leetcode.cn/problems/count-subarrays-with-score-less-than-k/）同向双指针维护指针位置与计数
2301. 替换字符后匹配（https://leetcode.cn/problems/match-substring-after-replacement/）枚举匹配字符起点并使用双指针维护可行长度
2106. 摘水果（https://leetcode.cn/problems/maximum-fruits-harvested-after-at-most-k-steps/）巧妙利用行走距离的计算更新双指针
6293. 统计好子数组的数目（https://leetcode.cn/problems/count-the-number-of-good-subarrays/）双指针计数

===================================洛谷===================================
P2381 圆圆舞蹈（https://www.luogu.com.cn/problem/P2381）环形数组，滑动窗口双指针
P3353 在你窗外闪耀的星星（https://www.luogu.com.cn/problem/P3353）滑动窗口加双指针
P3662 [USACO17FEB]Why Did the Cow Cross the Road II S（https://www.luogu.com.cn/problem/P3662）滑动子数组和
P4995 跳跳！（https://www.luogu.com.cn/problem/P4995）排序后利用贪心与双指针进行模拟
P2207 Photo（https://www.luogu.com.cn/problem/P2207）贪心加同向双指针
P7542 [COCI2009-2010#1] MALI（https://www.luogu.com.cn/problem/P7542）桶计数加双指针进行计算

================================CodeForces================================
D. Carousel（https://codeforces.com/problemset/problem/1328/D）环形数组滑动窗口，记录变化次数并根据奇偶变换次数与环形首尾元素确定染色数量

参考：OI WiKi（xx）
"""


class TwoPointer:
    def __init__(self):
        return

    @staticmethod
    def circle_array(arr):
        # 模板：环形数组指针移动
        n = len(arr)
        ans = 0
        for i in range(n):
            ans = max(ans, arr[i]+arr[(i+n-1)%n])
        return ans

    @staticmethod
    def fast_and_slow(head):
        # 模板：快慢指针判断链表是否存在环
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    @staticmethod
    def same_direction(nums):
        # 模板: 相同方向双指针（寻找最长不含重复元素的子序列）
        n = len(nums)
        ans = j = 0
        pre = set()
        for i in range(n):
            # 特别注意指针的移动情况
            while j < n and nums[j] not in pre:
                pre.add(nums[j])
                j += 1
            # 视情况更新返回值
            ans = ans if ans > j - i else j - i
            pre.discard(nums[i])
        return ans

    @staticmethod
    def opposite_direction(nums, target):
        # 模板: 相反方向双指针（寻找升序数组是否存在两个数和为target）
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            cur = nums[i] + nums[j]
            if cur > target:
                j -= 1
            elif cur < target:
                i += 1
            else:
                return True
        return False


class TestGeneral(unittest.TestCase):

    def test_two_pointer(self):
        nt = TwoPointer()
        nums = [1, 2, 3, 4, 4, 3, 3, 2, 1, 6, 3]
        assert nt.same_direction(nums) == 4

        nums = [1, 2, 3, 4, 4, 5, 6, 9]
        assert nt.opposite_direction(nums, 9)
        nums = [1, 2, 3, 4, 4, 5, 6, 9]
        assert not nt.opposite_direction(nums, 16)
        return


if __name__ == '__main__':
    unittest.main()
