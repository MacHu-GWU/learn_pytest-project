#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
从pytest 3.0开始, 添加了新的approx方法, 可以用于比较浮点数。

ref: http://doc.pytest.org/en/latest/builtin.html#comparing-floating-point-numbers
"""
import pytest


def add_two(a, b):
    return a + b


def test_add_two():
    if pytest.__version__.startswith("3"):
        assert add_two(0.1, 0.2) == pytest.approx(0.3)
        assert (0.1, 0.2) == pytest.approx((0.1, 0.2))


if __name__ == "__main__":
    import os
    
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
