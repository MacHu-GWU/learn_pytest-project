#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref: https://docs.pytest.org/en/latest/fixture.html
"""

import os
import pytest


@pytest.fixture
def one():
    return 1


@pytest.fixture(scope="module")
def two():
    return 2


@pytest.fixture
def setup_and_teardown():
    """
    Everything before yield is setUp, after yield is tearDown.
    """
    with open("temp.txt", "w", encoding="utf-8") as f:
        f.write("hello")
    yield
    try:
        os.remove("temp.txt")
    except:
        pass