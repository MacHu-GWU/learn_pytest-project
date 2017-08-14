#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fixture可以起到unittest中setUp和tearDown类似的功能, 但是功能更强大。只不过我
还没有透彻地研究。

ref: http://doc.pytest.org/en/latest/fixture.html
"""
import pytest


def test_one(one):
    assert one == 1


def test_two(two):
    assert two == 2


def test_setup_and_teardown(setup_and_teardown):
    with open("temp.txt", "r", encoding="utf-8") as f:
        assert f.read() == "hello"


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
