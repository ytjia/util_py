#!/usr/bin/python
# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from utils_py.TimeRange import TimeRange


class TestTimeRange(unittest.TestCase):
    def test_lie_between(self):
        print(TimeRange('09:00-10:00', '%H:%M').lie_between(
                TimeRange('09:01-10:00', '%H:%M')))


if __name__ == '__main__':
    unittest.main()
