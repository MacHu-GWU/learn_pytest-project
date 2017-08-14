#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

def test_create_file(tmpdir):
    """pytest能够帮你虚拟一个临时的文件目录。你可以使用面向对象的API接口创建
    这些文件以及写入内容。然后对其进行测试。在测试结束后pytest会自动将其销毁。

    对于比较复杂的文件结构, 我建议用os模块手动实现这部分测试。

    ref: https://pytest.org/latest/tmpdir.html
    """
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1


if __name__ == "__main__":
    import os
    
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
