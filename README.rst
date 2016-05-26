Welcome to the learn_pytest Documentation
=========================================
pytest主要支持两种自动化测试方案:


**从命令行运行测试**

1. `Choose a project layout <https://pytest.org/latest/goodpractices.html#choosing-a-test-layout-import-rules>`_
2. Run ``cd <path-to-project-directory>``, then ``py.test``. This follows `Conventions for Python test discovery <https://pytest.org/latest/goodpractices.html#conventions-for-python-test-discovery>`_


**将测试脚本作为主脚本运行**

在你的测试脚本中插入如下代码, 即可运行此脚本而执行其中的测试。

.. code-block:: python

	def add_two(a, b):
	    return a + b

	def test_add_two():
	    assert add_two(1, 2) == 3
	
	if __name__ == "__main__"    :
	    import py
	    py.test.cmdline.main("--tb=native") # use native python trace back


附录
----
- `py.test的命令行参数大全 <https://pytest.org/latest/usage.html>`_, 当然你也可以使用 ``py.test -h`` 呼出帮助信息。