#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
you can run this script as main script.
"""

from __future__ import print_function
import pytest


def add_two(a, b):
    return a + b


def test_add_two():
    assert add_two(1, 2) == 3


def add_three(a, b, c):
    return a + b + c


def test_add_three():
    assert add_three(1, 2, 3) == 6


def test_raise_exception():
    """使用 ``with pytest.raise(Exception) as excinfo:`` Context Manage语法测试
    代码块中的代码是否raise指定的异常。在代码块外, 你可以使用 
    
    - ``excinfo.value`` 访问异常变量 ``e``
    - ``excinfo.type`` 访问异常类型
    - ``excinfo.traceback`` 访问异常的traceback
    
    ref: https://pytest.org/latest/assert.html#assertions-about-expected-exceptions 
    """
    with pytest.raises(IndexError) as excinfo:
        array = [1, 2, 3]
        i = array[3]


def test_print_to_console():
    """默认设置中, 所有的print到console中的文本, 以及sys.stdout, sys.stderr都会
    被pytest所capture, 所以不会被显示。若你想要显示所有输出到console的内容, 可以
    使用 ``-s`` 参数, 等效于 ``--capture=no``。
    """
    print("Hello Pytest!")
    

def test 


if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native -s") # use native python trace back