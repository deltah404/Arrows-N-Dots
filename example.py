from arrows_n_dots import Interpreter

i = Interpreter()

scr = """
^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^.^^^^^^^^^^^^^.v
vvvvvvvvv.vvvvvvvvvvvvvvvvv
vvvvvvvvvvvvvvvvvvv.^^^^^^^
^^^^^^^^^^^^^^^^^^^^^^^^^^^
^^^.^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^^^^^^^^^^^^
^.vvvvvvvvvvvvvvvvvvvvvvv.^
^^^^^^^^^^^.^^^.vvvv.vvvvvv
v.>^^^^^^^^^^^^^^^^^^^^^^^^
^^^^^^^^.>^:>^^^^-
"""
i.evaluate(scr)
