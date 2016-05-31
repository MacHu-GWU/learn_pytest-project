Welcome to the learn_pytest Documentation
=========================================
pytest support two way of testing:

**Run test from command line**

1. `Choose a project layout <https://pytest.org/latest/goodpractices.html#choosing-a-test-layout-import-rules>`_.
2. Run ``cd <path-to-project-directory>``, then ``py.test``. This follows `Conventions for Python test discovery <https://pytest.org/latest/goodpractices.html#conventions-for-python-test-discovery>`_.

**Run your test script as main script**

Do this:

.. code-block:: python

	def add_two(a, b):
	    return a + b

	def test_add_two():
	    assert add_two(1, 2) == 3
	
	if __name__ == "__main__"    :
	    import py
	    py.test.cmdline.main("")

For more example, read `THIS <https://github.com/MacHu-GWU/learn_pytest-project/blob/master/tests>`_


Appendix
--------
- `pytest document <https://pytest.org/latest/contents.html>`_
- `py.test command line options <https://pytest.org/latest/usage.html>`_, of course you can call help information via: ``py.test -h``.