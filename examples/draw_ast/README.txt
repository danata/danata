---------------
Description
---------------

This example, print_ast, automatically generates range of input values for functions in the given source files

---------------
Usage
---------------

>>> print_ast python_source_file.py

---------------
Syntax
---------------

print_ast [options] file.py [file.py ...]


---------------
Output
---------------

Generated test cases will be added in docstring of each functions as below.

def func(a, b, c):
	"""
	Original docstring content

	TestCaseGen
	----------
	a = { x | None, Inf, 1 < x < 2 }
	b = { x | None, Inf, 2 < x < 4 }
	c = { x | None, Inf, 3 < x < 6 }
	d = { x | None, Inf, 4 < x < 8 }
	"""

