#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest


def test():
    assert 1 + 2 == 3


if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])
