#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref: http://doc.pytest.org/en/latest/usage.html
"""

import pytest


def add_two(a, b):
    return a + b


def test_add_two():
    assert add_two(1, 2) == 3
    assert add_two(0.1, 0.2) == pytest.approx(0.3)
    

"""
下面的代码能运行脚本内的test, 而不需要使用到外部命令行。

pytest的一些参数的解释:

- ``--tb=native``: 使用Python原生的traceback捕捉器, 使得可以通过点击跳转到错误行。
- ``-s``: 使pytest不捕捉输出在console上的内容, 也就是允许打印文本到console。
- ``test_basic.py``: pytest所测试的脚本, 只有在脚本中的测试代码将被运行。
"""
if __name__ == "__main__":
    import os

    pytest.main([os.path.basename(__file__), "--tb=native", "-s"])
