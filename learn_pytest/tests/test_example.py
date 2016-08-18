#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test():
    assert 1 + 2 == 3


if __name__ == "__main__":
    import py
    import os
    py.test.cmdline.main("%s --tb=native -s" % os.path.basename(__file__))
