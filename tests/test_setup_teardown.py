#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ref: http://doc.pytest.org/en/latest/xunit_setup.html
"""

import pytest


def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    with open("data.txt", "wb") as f:
        f.write("Hello".encode("utf-8"))


def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    import os
    try:
        os.remove("data.txt")
    except:
        pass


def test():
    with open("data.txt", "r") as f:
        assert f.read() == "Hello"


class TestClass:
    """Similarly, the following methods are called at class level
    before and after all test methods of the class are called:
    """

    def setup_method(self):
        """setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        self.status = "setup"

    def teardown_method(self):
        """teardown any state that was previously setup with a setup_method
        call.
        """
        self.status = "tear down"

    def test(self):
        assert self.status == "setup"


if __name__ == "__main__":
    import os

    pytest.main([os.path.basename(__file__), "--tb=native", "-s"])
