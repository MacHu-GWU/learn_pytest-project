#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
you can run this script as main script.
"""

from __future__ import print_function
import os
import pytest


def add_two(a, b):
    return a + b


def test_add_two():
    assert add_two(1, 2) == 0


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
    

def test_create_file(tmpdir):
    """pytest能够帮你虚拟一个临时的文件目录。你可以使用面向对象的API接口创建
    这些文件以及写入内容。然后对其进行测试。在测试结束后pytest会自动将其销毁。
    
    对于比较复杂的文件结构, 我建议用os模块手动实现这部分测试。
    
    ref: https://pytest.org/latest/tmpdir.html
    """
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1


"""
下面的代码能让pytest从脚本内运行, 而不需要使用到命令行。

pytest的一些参数的解释:

- ``--tb=native``: 使用Python原生的traceback捕捉器, 使得可以通过点击跳转到错误行。
- ``-s``: 使pytest不捕捉输出在console上的内容, 也就是允许打印文本到console。
"""
if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native -s")