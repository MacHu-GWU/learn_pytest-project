#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
运行此脚本将会测试此目录下, 包括子目录下的所有测试。
"""

if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native -s")