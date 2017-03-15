#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fixture可以起到unittest中setUp和tearDown类似的功能, 但是功能更强大。只不过我
还没有透彻地研究。

ref: http://doc.pytest.org/en/latest/fixture.html
"""
import pytest

if __name__ == "__main__":
    import os

    pytest.main([os.path.basename(__file__), "--tb=native", "-s"])
