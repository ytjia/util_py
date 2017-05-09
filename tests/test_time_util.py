#!/usr/bin/python
# -*- coding: utf-8 -*-

# Authors: Y. Jia <ytjia.zju@gmail.com>

import unittest

from utils_py import time_util


class TestTimeUtil(unittest.TestCase):
    def test_today_dt_str(self):
        print(time_util.today_dt_str())


if __name__ == '__main__':
    unittest.main()
