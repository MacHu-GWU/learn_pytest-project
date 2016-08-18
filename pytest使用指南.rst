Pytest使用指南
=============
在开始写一个比较大的项目的代码前, 我们首先要规划整个项目要分多少个模块, 类和方法; 他们如何互相组织起来。而当我们开始为每一个模块写代码前, **就需要写简单的单元测试**, 设定好你预期的input/output。在开发过程中, **为了方便起见, 可以将测试代码直接写在模块中**, 方便你调试, 开发。但当你完成好一个模块的设计和测试之后, 即需要将测试代码移动到专门的代码测试目录下, 用于在当你做了任何修改之后, 验证原有的功能是否还能正确的运行。下面, 根据个人的开发经验, 介绍一下在这个流程中, **测试代码应该怎样写, 文件结构应该怎样组织**。


模块的开发过程中, 写单元测试代码
--------------------------------
在功能代码的开发过程中, 为了方便, 我们会想要将功能代码和测试代码放在一个文件中, 免除来回切换的烦恼。而在开发完毕后, 将测试代码移动到专门的测试文件中时, 我们想直接将功能代码后的测试代码拷贝过去即可。那么, 你需要这么写:

请观察这一段示例代码, ``addition.py``:

.. code-block:: python

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	def add_two(a, b):
	    return a + b


	#--- Unittest ---
	def test_add_two():
	    assert add_two(1, 2) == 3
	    

	if __name__ == "__main__":
	    import py
	    import os
	    
	    py.test.cmdline.main(os.path.basename(__file__))


在 ``#--- Unittest ---`` 之上的是开发代码, 之下的是测试代码。而最后一段代码中的 ``os.path.basename(__file__)`` 使得pytest只运行本文件中的测试代码。 而当你完成了这些功能之后, 你可直接将 ``#--- Unittest ---`` 以下的代码全部拷贝到你的测试文件中即可。


如何组织测试代码文件夹
----------------------
一个好的测试代码文件结构需要满足:

- 能够对每一个文件进行单元测试
- 能够对每一个文件夹下的, 包含子文件夹中的文件进行单元测试
- 能够对整个测试目录进行单元测试。
- **测试代码不要从其他测试代码中import东西**, 这样会导致结构紊乱。

``pytest`` 支持 `两种风格 <http://doc.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules>`_ 的文件目录结构。


风格1: 将功能代码和测试代码分离
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

	xxx-project
	|--- xxx # your package code directory
	|--- tests # pytest directory
		|--- test_all.py # test everything
		|--- test_module.py # create test script for each module
		|--- ...

``test_all.py``:

.. code-block:: python

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	if __name__ == "__main__":
	    import py
	    
	    py.test.cmdline.main("")

``test_module.py``:

.. code-block:: python

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-

	if __name__ == "__main__":
	    import py
	    import os
	    py.test.cmdline.main("%s --tb=native -s" % os.path.basename(__file__))

你的项目开发完成后, 所有的测试代码都将放在 ``tests`` 目录下。 而你可以为你的包中的所有模块都加上前缀 ``test`` 创建一个测试模块, 并保持同样的目录组织结构。 在这些文件中, 最后调用测试的命令行都使用 ``py.test.cmdline.main(os.path.basename(__file__))`` 以保证每个文件都可以单独运行。 而 ``test_all.py`` 文件能运行该目录下的所有测试文件。**这样做是我所推荐的**


风格2: 将测试代码包含在功能代码中
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

	xxx-project
	|--- xxx # your package code directory
		|--- tests # pytest directory
			|--- test_all.py # test everything
			|--- test_module.py # create test script for each module
			|--- ...
		|--- __init__.py
		|--- ...

这样做的唯一好处就是可以让用户能从功能代码中执行全部单元测试。具体方法还有待研究。