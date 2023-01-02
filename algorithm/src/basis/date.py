"""
算法：xxx
功能：xxx
题目：
Lxxxx xxxx（https://leetcode.cn/problems/shortest-palindrome/）xxxx

参考：OI WiKi（xx）
"""
import datetime
import unittest


class DateTime:
    def __init__(self):
        return

    @staticmethod
    def is_leap_year(yy):
        # 判断是否为闰年
        # 闰年天数
        leap_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        not_leap_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        assert sum(leap_month) == 366
        assert sum(not_leap_month) == 365
        return yy % 400 == 0 or (yy % 4 == 0 and yy % 100 != 0)

    @staticmethod
    def get_n_days(yy, mm, dd, n):
        # 获取当前日期往后天数的日期
        now = datetime.datetime(yy, mm, dd, 0, 0, 0, 0)
        delta = datetime.timedelta(days=n)
        n_days = now + delta
        return n_days.strftime("%Y-%m-%d")

    @staticmethod
    def is_valid_date(date_str):
        # 判断日期是否合法
        try:
            datetime.date.fromisoformat(date_str)
        except ValueError as _:
            return False
        else:
            return True

    def all_palidrome_date(self):
        # 枚举出所有的八位回文日期 1000-01-01到9999-12-31
        ans = []
        for y in range(1000, 10000):
            yy = str(y)
            mm = str(y)[::-1][:2]
            dd = str(y)[::-1][2:]
            if self.is_valid_date(f"{yy}-{mm}-{dd}"):
                ans.append(f"{yy}-{mm}-{dd}")
        return ans


class TestGeneral(unittest.TestCase):

    def test_date_time(self):
        dt = DateTime()
        assert dt.get_n_days(2023, 1, 2, 1) == "2023-01-03"

        assert dt.is_valid_date("2023-02-29") is False
        assert dt.is_valid_date("2023-02-28") is True
        assert dt.is_valid_date("0001-02-27") is True

        res = dt.all_palidrome_date()
        assert len(res) == 331

        assert dt.is_leap_year(2000) is True
        assert dt.is_leap_year(2100) is False
        return


if __name__ == '__main__':
    unittest.main()
