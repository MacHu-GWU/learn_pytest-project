#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add_two(a, b):
    return a + b


def test_add_two():
    assert add_two(1, 2) == 3


"""
下面的代码能让pytest从脚本内运行, 而不需要使用到命令行。

pytest的一些参数的解释:

- ``test_basic.py``: pytest所测试的脚本, 只有在脚本中的测试代码将被运行。
- ``--tb=native``: 使用Python原生的traceback捕捉器, 使得可以通过点击跳转到错误行。
- ``-s``: 使pytest不捕捉输出在console上的内容, 也就是允许打印文本到console。
"""
if __name__ == "__main__":
    import py
    import os
    py.test.cmdline.main("%s --tb=native -s" % os.path.basename(__file__))