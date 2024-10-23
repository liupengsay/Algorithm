import random
import unittest

from src.string.manacher_palindrome.template import ManacherPlindrome


class TestGeneral(unittest.TestCase):

    def test_manacher_palindrome_count_start_end(self):
        mp = ManacherPlindrome()
        for x in range(4):
            n = 10 ** x
            for _ in range(10):
                nums = [random.randint(0, x) for _ in range(n)]
                start = [0] * n
                end = [0] * n
                cnt = [0] * (n + 1)
                start_odd = [0]*n
                end_odd = [0]*n
                for i in range(n):
                    for j in range(i, n):
                        if nums[i:j + 1] == nums[i:j + 1][::-1]:
                            start[i] += 1
                            end[j] += 1
                            cnt[j - i + 1] += 1
                            if (j-i+1) % 2:
                                start_odd[i] += 1
                                end_odd[j] += 1
                assert start, end == mp.palindrome_count_start_end("".join(chr(x + ord("a")) for x in nums))
                assert cnt == mp.palindrome_length_count("".join(chr(x + ord("a")) for x in nums))
                assert sum(cnt) == mp.palindrome_count("".join(chr(x + ord("a")) for x in nums))
                assert start_odd, end_odd == mp.palindrome_count_start_end_odd("".join(chr(x + ord("a")) for x in nums))

        return


if __name__ == '__main__':
    unittest.main()
