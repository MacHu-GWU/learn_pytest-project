#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
注意: Pytest明确 `指出 <http://doc.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules>`_
了, 不要再tests目录下包含 ``__init__.py`` 文件。这样做是不可取的。

换言之, 你可以从测试代码中导入内容, 但是你一旦这么做了, 那么该脚本就不能再使用
pytest了。请看下面的例子。
"""

import pytest
from learn_pytest.tests.test_example import test


if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])
