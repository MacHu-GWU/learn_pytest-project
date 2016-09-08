#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
运行此脚本将测试folder1目录下的所有测试。
"""

if __name__ == "__main__":
    import pytest
    pytest.main(["--tb=native", "-s", ])