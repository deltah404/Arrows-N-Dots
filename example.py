from arrows_n_dots import Interpreter

i = Interpreter()

scr = """
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^.^^^^^^^^^^^^^.vvvvvvvvvv.
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv.^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
^.^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^.vvvvvvvvvvvvvvvvvvvvvvv.
^^^^^^^^^^^^.^^^.vvvv.vvvvvvv.>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^.>^:
"""
i.evaluate(scr)
