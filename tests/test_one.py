#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
you can run this script as main script.
"""

def add_two(a, b):
    return a + b

def test_add_two():
    assert add_two(1, 2) == 0

def add_three(a, b, c):
    return a + b + c

def test_add_three():
    assert add_three(1, 2, 3) == 0

if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native") # use native python trace back