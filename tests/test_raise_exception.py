#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用 ``with pytest.raise(Exception) as excinfo:`` Context Manage语法测试
代码块中的代码是否raise指定的异常。在代码块外, 你可以使用 

- ``excinfo.value`` 访问异常变量 ``e``
- ``excinfo.type`` 访问异常类型
- ``excinfo.traceback`` 访问异常的traceback

ref: https://pytest.org/latest/assert.html#assertions-about-expected-exceptions 
"""
    
import pytest


def test_raise_exception():
    with pytest.raises(IndexError) as excinfo:
        array = [1, 2, 3]
        i = array[3]


if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])
